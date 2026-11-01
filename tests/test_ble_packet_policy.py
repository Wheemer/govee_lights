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


@pytest.mark.parametrize(("ha_brightness", "register"), [(26, 41), (128, 136), (255, 254)])
def test_h6102_brightness_uses_its_documented_register_range(
    ha_brightness: int, register: int
) -> None:
    assert encode_ha_brightness(
        ha_brightness, percentage=True, wire_range=(20, 254)
    ) == register
