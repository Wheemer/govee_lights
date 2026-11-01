"""
Bundled device model quirks.

Only models that need non-default BLE handling are listed in
``_DEVICE_FEATURES`` below; a model absent from it is assumed to be a plain
device (solid-colour mode 0x02, brightness as a raw 0-255 byte, no segments,
no passive advert state) - which is the common case, so the dict holds
exceptions, not a whitelist of supported models. Nothing else in the
codebase should hard-code model IDs or per-model behaviour; import these
helpers instead so this stays the one source of truth.

Per-model flags:

- ``segmented``: device has individually addressable LED segments and needs
  segment-aware color commands.
- ``h617a_segment_grammar``: model uses the documented H617A segmented static
  colour/white packet form, including its whole-device bitmask.
- ``segments``: number of individually addressable segments (only meaningful
  for segmented models). Defaults to :data:`DEFAULT_SEGMENT_COUNT`.
- ``segment_readback_group_size``: number of segments in each ``0xA5`` state
  response. The H617A legacy default is three; some newer siblings use four.
- ``brightness_percent``: device expects brightness as a percentage (0-100)
  instead of a raw byte (0-255).
- ``brightness_wire_range``: percentage brightness is re-encoded into this
  inclusive device-register range before sending.
- ``colour_d``: device uses BLE mode byte ``0x0D`` instead of ``0x02`` for
  colour/color-temperature packets.
- ``color_command_ack_state``: device reports color-command acceptance as ``AA <command>
  00``; preserve the command's optimistic state instead of immediately
  querying and applying a potentially stale report.
- ``connection_settle``: wait for the control service to settle after a fresh
  connection before sending the first control frame.
- ``color_write_with_response``: the app writes the legacy colour frame using
  a GATT write request. This is deliberately scoped to COLOR here; POWER
  retains this integration's established write-without-response behavior.
- ``advert_state``: device broadcasts on/off state in its BLE advertisement
  (as ``ec 00 0a 01 <state>``), so power state can be tracked passively
  without an open GATT connection.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import re
from types import MappingProxyType
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Mapping

# Fallback used when a segmented model does not declare a segment count. The
# segment bitmask in the protocol covers 15 segments.
DEFAULT_SEGMENT_COUNT = 15

# Largest addressable segment count supported by the mask protocol.
MAX_SEGMENT_COUNT = 15


class SupportQuality(StrEnum):
    """How much wire-level evidence exists for a model profile."""

    GENERIC = "generic"
    EXPERIMENTAL = "experimental"
    VERIFIED = "verified"


@dataclass(frozen=True, slots=True)
class ModelProfile:
    """Model identity plus the evidence level for its local BLE behavior.

    Feature flags remain the single command-policy input for now.  This
    immutable wrapper is deliberately small: future BLE, LAN, cloud, and
    appliance adapters can share a model identity without pretending that one
    transport's packet grammar is valid on another transport.
    """

    model: str
    support_quality: SupportQuality
    family: str
    features: Mapping[str, bool | int]

# Govee model IDs look like ``H6006``, ``H617C`` or ``H61A0`` and appear
# inside BLE advertisement names (e.g. ``Govee_H617C_2482``).
_MODEL_PATTERN = re.compile(r"[Hh]\d{2,4}[A-Za-z]?\d?")

_DEVICE_FEATURES: dict[str, dict[str, bool | int]] = {
    "H6005": {"colour_d": True},
    "H6052": {"colour_d": True},
    "H6053": {"segmented": True, "segments": 12},
    "H6058": {"colour_d": True},
    "H6072": {"segmented": True},
    # H6076 (Lyra) uses the H617A command grammar but has its own status
    # grammar. The upstream packet-tested profile confirms seven logical
    # segments; expose only the compatible write path until this project ports
    # and verifies H6076's status decoder and advanced effects.
    "H6076": {
        "segmented": True,
        "segments": 7,
        "brightness_percent": True,
        "h617a_segment_grammar": True,
        "segment_readback_group_size": 4,
    },
    "H6102": {
        "segmented": True,
        "colour_d": True,
        "h617a_segment_grammar": True,
        "brightness_wire_range": (20, 254),
        "segment_brightness": True,
    },
    "H613A": {"brightness_percent": True},
    "H613B": {"colour_d": True},
    "H613D": {"colour_d": True},
    # This H613E reports its active colour layout as 0x0D. The old app's
    # H6138-family code has the matching SubModeColor4Bk serializer.
    "H613E": {
        "colour_d": True,
        "color_command_ack_state": True,
        "connection_settle": True,
        "color_write_with_response": True,
    },
    "H617A": {
        "segmented": True,
        "brightness_percent": True,
        "advert_state": True,
        "h617a_segment_grammar": True,
    },
    "H617C": {
        "segmented": True,
        "brightness_percent": True,
        "advert_state": True,
        "h617a_segment_grammar": True,
    },
    "H617E": {
        "segmented": True,
        "brightness_percent": True,
        "colour_d": True,
        "h617a_segment_grammar": True,
    },
    # Teh-Hippo's MIT-licensed, packet-tested profile defines H617F as a
    # direct H617A command/status grammar sibling.  Keep it experimental here
    # until this integration has an independent device trace, but use the
    # same established segmented/percent-brightness policy as H617A rather
    # than falling through to the unsafe single-zone generic encoder.
    "H617F": {
        "segmented": True,
        "brightness_percent": True,
        "advert_state": True,
        "h617a_segment_grammar": True,
    },
    "H618C": {"segmented": True, "brightness_percent": True},
    "H6199": {"segmented": True, "brightness_percent": True},
    # H1A42 (Strip Light 2) and H61F5 (Strip Light 2 Pro) both have the
    # H617A command grammar, while their status/music grammars differ.  Their
    # explicitly documented logical geometries make the basic write path safer
    # than the generic one-zone fallback, but they remain experimental until
    # the distinct response codecs are implemented and verified here.
    "H1A42": {
        "segmented": True,
        "segments": 5,
        "brightness_percent": True,
        "h617a_segment_grammar": True,
        "segment_readback_group_size": 4,
    },
    "H61F5": {
        "segmented": True,
        "segments": 10,
        "brightness_percent": True,
        "h617a_segment_grammar": True,
        "segment_readback_group_size": 4,
    },
}

# Profiles with a known wire family. A feature entry not present here remains
# usable through the established generic path, but must not be advertised as a
# verified per-model protocol implementation merely because its name matches.
_MODEL_PROFILE_METADATA: Final[dict[str, tuple[SupportQuality, str]]] = {
    "H613E": (SupportQuality.VERIFIED, "legacy_0d_bk"),
    "H6076": (SupportQuality.EXPERIMENTAL, "legacy_h617a"),
    "H617F": (SupportQuality.EXPERIMENTAL, "legacy_h617a"),
    "H1A42": (SupportQuality.EXPERIMENTAL, "legacy_h617a"),
    "H61F5": (SupportQuality.EXPERIMENTAL, "legacy_h617a"),
}


def detect_model(device_name: str) -> str | None:
    """Return the model ID embedded in an advertisement name, if any.

    Govee names typically look like ``Govee_H617C_2482``; the first token
    shaped like a model ID is returned, uppercased. This is a best-effort
    guess for pre-filling the config flow - it does not check the result
    against :data:`_DEVICE_FEATURES`, since an unlisted model works fine
    with the default (no-quirks) behaviour above. Returns None when no such
    token appears at all.
    """
    if not device_name:
        return None
    match = _MODEL_PATTERN.search(device_name)
    return match.group(0).upper() if match else None


def _model_features(model: str) -> dict[str, bool | int]:
    """Return *model*'s raw feature entry from :data:`_DEVICE_FEATURES`
    (never raises; ``{}`` for an unlisted model)."""
    return _DEVICE_FEATURES.get(model, {})


def get_model_profile(model: str) -> ModelProfile:
    """Return the evidence-qualified local BLE profile for ``model``.

    Unknown model names retain the integration's current generic behavior. The
    profile makes that fallback explicit so callers can avoid presenting an
    inferred command grammar as verified device support.
    """

    normalized = model.upper()
    quality, family = _MODEL_PROFILE_METADATA.get(
        normalized,
        (
            SupportQuality.EXPERIMENTAL
            if normalized in _DEVICE_FEATURES
            else SupportQuality.GENERIC,
            "legacy_default",
        ),
    )
    return ModelProfile(
        model=normalized,
        support_quality=quality,
        family=family,
        features=MappingProxyType(_model_features(normalized)),
    )


def is_segmented_model(model: str) -> bool:
    """Return True when *model* uses individually addressable segments."""
    return bool(_model_features(model).get("segmented", False))


def uses_percent_brightness(model: str) -> bool:
    """Return True when *model* expects brightness as a percentage."""
    return bool(_model_features(model).get("brightness_percent", False))


def get_brightness_wire_range(model: str) -> tuple[int, int] | None:
    """Return an optional post-percentage brightness register range."""
    value = _model_features(model).get("brightness_wire_range")
    return value if isinstance(value, tuple) else None


def uses_colour_d_mode(model: str) -> bool:
    """Return True when *model* uses mode byte 0x0D instead of 0x02."""
    return bool(_model_features(model).get("colour_d", False))


def uses_h617a_segment_grammar(model: str) -> bool:
    """Return True when segmented static colours use H617A packet grammar."""
    return bool(_model_features(model).get("h617a_segment_grammar", False))


def uses_color_command_ack_state(model: str) -> bool:
    """Return whether COLOR command replies acknowledge writes rather than state."""

    return bool(_model_features(model).get("color_command_ack_state", False))


def uses_connection_settle(model: str) -> bool:
    """Return whether a fresh BLE connection needs a control-service settle delay."""

    return bool(_model_features(model).get("connection_settle", False))


def uses_color_write_with_response(model: str) -> bool:
    """Return whether plain COLOR frames use a GATT write request."""

    return bool(_model_features(model).get("color_write_with_response", False))


def has_advert_state(model: str) -> bool:
    """Return True when *model* broadcasts on/off state in its BLE advert."""
    return bool(_model_features(model).get("advert_state", False))


def get_segment_count(model: str) -> int:
    """Return the number of addressable segments for *model*.

    Defaults to :data:`DEFAULT_SEGMENT_COUNT` when the model does not declare
    one and is capped at :data:`MAX_SEGMENT_COUNT`, the protocol limit.
    """
    return min(
        int(_model_features(model).get("segments", DEFAULT_SEGMENT_COUNT)),
        MAX_SEGMENT_COUNT,
    )


def get_segment_readback_group_size(model: str) -> int:
    """Return segment records in one 0xA5 status response for *model*."""
    return int(_model_features(model).get("segment_readback_group_size", 3))


def supports_segment_brightness(model: str) -> bool:
    """Return whether the model has a native per-segment brightness command."""
    return bool(_model_features(model).get("segment_brightness", False))
