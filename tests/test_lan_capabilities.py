"""Regression tests for the govee-local-api to HA LAN capability boundary."""

import importlib.util
from pathlib import Path
import sys

_MODULE_PATH = Path(__file__).parents[1] / "custom_components" / "govee_lights" / "lan_capabilities.py"
_SPEC = importlib.util.spec_from_file_location("govee_lights_lan_capabilities", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_CAPABILITIES = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _CAPABILITIES
_SPEC.loader.exec_module(_CAPABILITIES)

LanLightFeature = _CAPABILITIES.LanLightFeature
get_lan_capability_profile = _CAPABILITIES.get_lan_capability_profile


def test_unknown_lan_sku_remains_on_off_only() -> None:
    profile = get_lan_capability_profile(0, 0, (2000, 9000))

    assert not profile.supports_rgb
    assert not profile.supports_color_temp
    assert not profile.supports_brightness
    assert profile.segment_count == 0
    assert profile.min_color_temp_kelvin is None
    assert profile.max_color_temp_kelvin is None


def test_known_lan_profile_preserves_feature_bits_and_model_temperature_range() -> None:
    profile = get_lan_capability_profile(
        int(
            LanLightFeature.RGB
            | LanLightFeature.COLOR_TEMPERATURE
            | LanLightFeature.BRIGHTNESS
            | LanLightFeature.SEGMENT_CONTROL
        ),
        7,
        (2700, 6500),
    )

    assert profile.supports_rgb
    assert profile.supports_color_temp
    assert profile.supports_brightness
    assert profile.segment_count == 7
    assert (profile.min_color_temp_kelvin, profile.max_color_temp_kelvin) == (2700, 6500)


def test_segments_are_not_exposed_without_the_dependency_feature_bit() -> None:
    profile = get_lan_capability_profile(int(LanLightFeature.RGB), 15, (2000, 9000))

    assert profile.segment_count == 0
