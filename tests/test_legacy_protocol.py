"""Regression tests for observed, unencrypted Govee BLE command frames."""

import importlib.util
from pathlib import Path
import sys

import pytest

_MODULE_PATH = Path(__file__).parents[1] / "custom_components" / "govee_lights" / "legacy_protocol.py"
_SPEC = importlib.util.spec_from_file_location("govee_lights_legacy_protocol", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_PROTOCOL = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _PROTOCOL
_SPEC.loader.exec_module(_PROTOCOL)

build_single_packet = _PROTOCOL.build_single_packet
sign_payload = _PROTOCOL.sign_payload


def test_h613e_green_frame_matches_observed_local_control() -> None:
    """H613E accepts 0D RGB packets in the legacy Bk packet family."""
    frame = build_single_packet(0x05, [0x0D, 0x00, 0xFF, 0x00])

    assert frame.hex() == "33050d00ff0000000000000000000000000000c4"
    assert sign_payload(frame[:-1]) == frame[-1]


def test_h613e_5000k_frame_matches_observed_native_payload() -> None:
    """H613E uses a Bk 0D payload with Kelvin encoded big-endian."""
    frame = build_single_packet(
        0x05, [0x0D, 0xFF, 0xFF, 0xFF, 0x13, 0x88, 0xFF, 0xE4, 0xCE]
    )

    assert frame.hex() == "33050dffffff1388ffe4ce00000000000000008a"
    assert sign_payload(frame[:-1]) == frame[-1]


def test_packet_rejects_payload_that_cannot_fit_the_legacy_envelope() -> None:
    with pytest.raises(ValueError, match="Payload too long"):
        build_single_packet(0x05, [0] * 18)
