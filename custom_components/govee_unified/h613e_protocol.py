"""H613E's bounded legacy-0D compatibility transform.

The generated H600A whole-bulb grammar has the same 20-byte 0D static
envelope as H613E.  H613E's APK, however, supplies a curve-derived RGB
companion for Kelvin rather than H600A's discrete table.  This module changes
only that companion field and re-signs the frame; it deliberately does not
claim a status or effects grammar for H613E.
"""

from __future__ import annotations

import math

from .transport import xor_checksum


def _kelvin_companion_rgb(kelvin: int) -> tuple[int, int, int]:
    """Return the APK-matching legacy Bk companion colour."""
    temp = max(1000, min(40000, kelvin)) / 100.0
    red = 255 if temp <= 66 else round(329.698727446 * ((temp - 60) ** -0.1332047592))
    green = (
        round(99.4708025861 * math.log(temp) - 161.1195681661)
        if temp <= 66
        else round(288.1221695283 * ((temp - 60) ** -0.0755148492))
    )
    blue = (
        255
        if temp >= 66
        else 0
        if temp <= 19
        else round(138.5177312231 * math.log(temp - 10) - 305.0447927307)
    )
    return tuple(max(0, min(255, value)) for value in (red, green, blue))  # type: ignore[return-value]


def transform_h613e_static_packet(packet: bytes) -> bytes:
    """Apply H613E's Kelvin companion rule to an otherwise shared 0D frame."""
    if len(packet) != 20 or packet[:3] != b"\x33\x05\x0d" or packet[3:6] != b"\xff\xff\xff":
        return packet
    kelvin = int.from_bytes(packet[6:8], "big")
    if not kelvin:
        return packet
    transformed = bytearray(packet)
    transformed[8:11] = bytes(_kelvin_companion_rgb(kelvin))
    transformed[19] = xor_checksum(transformed[:19])
    return bytes(transformed)
