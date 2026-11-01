"""Small, dependency-free view of govee-local-api LAN capabilities.

The integer values intentionally match ``govee_local_api.GoveeLightFeatures``.
Keeping the conversion here lets this integration test its Home Assistant
surface without maintaining a competing SKU registry.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntFlag


class LanLightFeature(IntFlag):
    """Feature bits supplied by govee-local-api for a LAN SKU."""

    RGB = 0x01
    COLOR_TEMPERATURE = 0x02
    BRIGHTNESS = 0x04
    SEGMENT_CONTROL = 0x08
    SCENES = 0x10


@dataclass(frozen=True, slots=True)
class LanCapabilityProfile:
    """Capabilities safe to expose in Home Assistant for one local LAN SKU."""

    supports_rgb: bool
    supports_color_temp: bool
    supports_brightness: bool
    segment_count: int
    min_color_temp_kelvin: int | None
    max_color_temp_kelvin: int | None


def get_lan_capability_profile(
    features: int, segment_count: int, temperature_range: tuple[int, int]
) -> LanCapabilityProfile:
    """Translate a govee-local-api capability record without an SKU lookup."""
    enabled = LanLightFeature(features)
    supports_color_temp = bool(enabled & LanLightFeature.COLOR_TEMPERATURE)
    minimum, maximum = temperature_range
    return LanCapabilityProfile(
        supports_rgb=bool(enabled & LanLightFeature.RGB),
        supports_color_temp=supports_color_temp,
        supports_brightness=bool(enabled & LanLightFeature.BRIGHTNESS),
        segment_count=segment_count if enabled & LanLightFeature.SEGMENT_CONTROL else 0,
        min_color_temp_kelvin=minimum if supports_color_temp else None,
        max_color_temp_kelvin=maximum if supports_color_temp else None,
    )
