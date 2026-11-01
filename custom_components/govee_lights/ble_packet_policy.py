"""Pure policy for selecting a local legacy BLE colour-temperature packet."""

from __future__ import annotations

from .legacy_protocol import build_h617a_segment_color_temp_packet, build_single_packet


def encode_ha_brightness(
    brightness: int, *, percentage: bool, wire_range: tuple[int, int] | None = None
) -> int:
    """Convert HA's 0..255 brightness into the declared device register."""
    if not 0 <= brightness <= 255:
        raise ValueError("Home Assistant brightness must be from 0 to 255")
    if not percentage and wire_range is None:
        return brightness
    percent = max(1, round(brightness * 100 / 255))
    if wire_range is None:
        return percent
    low, high = wire_range
    return (low * 100 + (percent - 1) * (high - low + 3)) // 100


def build_color_temp_packet(
    *,
    kelvin: int,
    rgb: tuple[int, int, int],
    segment_count: int,
    h617a_segment_grammar: bool,
    colour_d: bool,
) -> bytes:
    """Return the documented native-white packet for the selected BLE family."""
    red, green, blue = rgb
    if h617a_segment_grammar:
        return build_h617a_segment_color_temp_packet(
            kelvin, red, green, blue, (1 << segment_count) - 1
        )
    if colour_d:
        return build_single_packet(
            0x05,
            [0x0D, 0xFF, 0xFF, 0xFF, kelvin >> 8, kelvin & 0xFF, red, green, blue],
        )
    return build_single_packet(0x05, [0x02, 0xFF, 0xFF, 0xFF, 0x01, red, green, blue])
