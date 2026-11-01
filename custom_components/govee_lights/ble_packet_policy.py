"""Pure policy for selecting a local legacy BLE colour-temperature packet."""

from __future__ import annotations

from .legacy_protocol import build_h617a_segment_color_temp_packet, build_single_packet


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
