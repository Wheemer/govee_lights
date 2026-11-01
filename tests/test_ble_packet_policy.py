"""Regression tests for BLE native-white packet family selection."""

import importlib.util
from pathlib import Path
import sys
import types

import pytest

_PACKAGE_ROOT = Path(__file__).parents[1] / "custom_components" / "govee_lights"
_PACKAGE = types.ModuleType("govee_lights")
_PACKAGE.__path__ = [str(_PACKAGE_ROOT)]
sys.modules.setdefault("govee_lights", _PACKAGE)

for _module_name in ("legacy_protocol", "ble_packet_policy"):
    _spec = importlib.util.spec_from_file_location(
        f"govee_lights.{_module_name}", _PACKAGE_ROOT / f"{_module_name}.py"
    )
    assert _spec is not None and _spec.loader is not None
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_spec.name] = _module
    _spec.loader.exec_module(_module)

build_color_temp_packet = sys.modules["govee_lights.ble_packet_policy"].build_color_temp_packet
encode_ha_brightness = sys.modules["govee_lights.ble_packet_policy"].encode_ha_brightness
decode_device_brightness = sys.modules["govee_lights.ble_packet_policy"].decode_device_brightness
decode_segment_brightness_percent = sys.modules[
    "govee_lights.ble_packet_policy"
].decode_segment_brightness_percent
decode_h617a_segment_status_record = sys.modules[
    "govee_lights.ble_packet_policy"
].decode_h617a_segment_status_record


def test_h617a_packet_takes_priority_over_colour_d_for_segmented_models() -> None:
    packet = build_color_temp_packet(
        kelvin=4000,
        rgb=(255, 213, 161),
        segment_count=15,
        h617a_segment_grammar=True,
        colour_d=True,
    )

    assert packet.hex() == "33051501ffffff0fa0ffd5a1ff7f000000000079"


def test_h613e_bk_packet_is_used_when_the_h617a_grammar_does_not_apply() -> None:
    packet = build_color_temp_packet(
        kelvin=5000,
        rgb=(255, 228, 206),
        segment_count=0,
        h617a_segment_grammar=False,
        colour_d=True,
    )

    assert packet.hex() == "33050dffffff1388ffe4ce00000000000000008a"


def test_generic_legacy_packet_remains_available_for_plain_ble_lights() -> None:
    packet = build_color_temp_packet(
        kelvin=4000,
        rgb=(255, 213, 161),
        segment_count=0,
        h617a_segment_grammar=False,
        colour_d=False,
    )

    assert packet.hex() == "330502ffffff01ffd5a100000000000000000041"


@pytest.mark.parametrize(
    ("ha_brightness", "register", "percent"),
    [(26, 41, 10), (128, 136, 50), (255, 254, 100)],
)
def test_h6102_brightness_uses_its_documented_register_range(
    ha_brightness: int, register: int, percent: int
) -> None:
    assert encode_ha_brightness(
        ha_brightness, percentage=True, wire_range=(20, 254)
    ) == register
    assert decode_device_brightness(
        register, percentage=True, wire_range=(20, 254)
    ) == round(percent * 255 / 100)


def test_h6102_brightness_decoder_treats_zero_as_off_and_clamps_registers() -> None:
    assert decode_device_brightness(0, percentage=True, wire_range=(20, 254)) == 0
    assert decode_device_brightness(1, percentage=True, wire_range=(20, 254)) == round(255 / 100)


@pytest.mark.parametrize(
    ("percent", "ha_brightness"),
    [(0, 0), (1, 3), (50, 128), (100, 255)],
)
def test_h617a_segment_status_brightness_is_a_zero_to_hundred_percent_field(
    percent: int, ha_brightness: int
) -> None:
    assert decode_segment_brightness_percent(percent) == ha_brightness


@pytest.mark.parametrize("percent", [-1, 101])
def test_h617a_segment_status_rejects_out_of_range_brightness(percent: int) -> None:
    with pytest.raises(ValueError, match="percentage"):
        decode_segment_brightness_percent(percent)


def test_h6102_segment_status_record_preserves_native_brightness_separately_from_rgb() -> None:
    # The H6102 upstream fixture's first record is [0, 0, 0, 0]: it is an
    # explicit off segment, not an omitted colour record.
    assert decode_h617a_segment_status_record(bytes([0, 0, 0, 0])) == (0, (0, 0, 0))
    assert decode_h617a_segment_status_record(bytes([50, 32, 64, 96])) == (128, (32, 64, 96))


@pytest.mark.parametrize("record", [b"", b"\x32\x20\x40", b"\x32\x20\x40\x60\x00"])
def test_h617a_segment_status_record_requires_exact_wire_length(record: bytes) -> None:
    with pytest.raises(ValueError, match="four bytes"):
        decode_h617a_segment_status_record(record)
