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


def transform_legacy_generic_rgb_raw_brightness(packet: bytes) -> bytes:
    """Port the portable integration's 02/RGB and raw-level legacy family.

    The shared serializer supplies an H617A-shaped static frame.  This family
    instead uses the older ``33 05 02 RR GG BB`` body and stores brightness as
    an unsigned 0..255 byte. Power frames already share the same envelope.
    """
    if len(packet) == 20 and packet[:3] == b"\x33\x05\x15":
        frame = bytearray(packet)
        red, green, blue = frame[4:7]
        frame[2:19] = bytes((0x02, red, green, blue)) + bytes(13)
        return _resign(frame)
    return _scale_brightness_to_255(packet)


def transform_h3001_encrypted_static(packet: bytes) -> bytes:
    """H3001's encrypted RGBIC static frame has an FF/00 mask tail."""
    if len(packet) == 20 and packet[:4] == b"\x33\x05\x15\x01":
        frame = bytearray(packet)
        frame[13] = 0
        return _resign(frame)
    return packet
