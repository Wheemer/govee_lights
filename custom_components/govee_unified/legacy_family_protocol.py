"""Bounded legacy RGB family transforms.

The generated H600A and H617A serializers provide the shared 20-byte command
envelopes. These transforms retain the distinct mode and brightness rules
ported from Homebridge Govee's MIT-licensed device capability table. They do
not establish native-white, effects, or status-readback support.
"""

from __future__ import annotations

from .transport import xor_checksum


def _resign(frame: bytearray) -> bytes:
    frame[19] = xor_checksum(frame[:19])
    return bytes(frame)


def _scale_brightness_to_255(packet: bytes) -> bytes:
    """Convert generated 0..100 brightness to a legacy 0..255 register."""
    if len(packet) != 20 or packet[:2] != b"\x33\x04":
        return packet
    frame = bytearray(packet)
    frame[2] = frame[2] * 255 // 100
    return _resign(frame)


def transform_legacy_0d_raw_brightness(packet: bytes) -> bytes:
    """H6005: 0D RGB envelope with a 0..255 brightness register."""
    return _scale_brightness_to_255(packet)


def transform_legacy_0d_percent_brightness(packet: bytes) -> bytes:
    """0D RGB envelope whose brightness register already carries percent."""
    return packet


def transform_extended_rgb_raw_brightness(packet: bytes) -> bytes:
    """H6053: 15/01 extended RGB envelope and 0..255 brightness register."""
    return _scale_brightness_to_255(packet)
