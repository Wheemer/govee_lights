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
build_h617a_segment_color_packet = _PROTOCOL.build_h617a_segment_color_packet
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


def test_h617a_segment_rgb_frame_matches_upstream_packet_fixture() -> None:
    """Shared H617A grammar: RGB followed by a little-endian 15-bit mask."""
    frame = build_h617a_segment_color_packet(10, 20, 30, 0x7FFF)

    assert frame.hex() == "330515010a141e0000000000ff7f0000000000a2"
    assert sign_payload(frame[:-1]) == frame[-1]


def test_h617a_segment_rgb_uses_only_the_declared_five_segment_mask() -> None:
    """H1A42's whole-device mask is 0x001F, not the generic 0x7FFF."""
    frame = build_h617a_segment_color_packet(10, 20, 30, 0x001F)

    assert frame.hex() == "330515010a141e00000000001f0000000000003d"
    assert sign_payload(frame[:-1]) == frame[-1]


def test_h617a_segment_packet_rejects_masks_outside_the_legacy_protocol() -> None:
    with pytest.raises(ValueError, match="15-bit"):
        build_h617a_segment_color_packet(1, 2, 3, 0x8000)


def test_packet_rejects_payload_that_cannot_fit_the_legacy_envelope() -> None:
    with pytest.raises(ValueError, match="Payload too long"):
        build_single_packet(0x05, [0] * 18)
