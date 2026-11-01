"""Pure policy for selecting a local legacy BLE colour-temperature packet."""

from __future__ import annotations

from .legacy_protocol import build_h617a_segment_color_temp_packet, build_single_packet

# Govee's whole-bulb H600A protocol uses this discrete 100 K companion RGB
# table with the native Kelvin field.  It is not interchangeable with the
# curve-fit preview used by legacy strip families.
_TABLE_KELVIN_RGB = {
    1000 + index * 100: bytes.fromhex(rgb)
    for index, rgb in enumerate(
        ["ff3300", "ff4500", "ff5200", "ff5d00", "ff6600", "ff6f00", "ff7600", "ff7c00", "ff8200", "ff8700", "ff8d0b", "ff921d", "ff9829", "ff9d33", "ffa23c", "ffa645", "ffaa4d", "ffae54", "ffb25b", "ffb662", "ffb969", "ffbd6f", "ffc076", "ffc37c", "ffc682", "ffc987", "ffcb8d", "ffce92", "ffd097", "ffd39c", "ffd5a1", "ffd7a6", "ffd9ab", "ffdbaf", "ffddb4", "ffdfb8", "ffe1bc", "ffe2c0", "ffe4c4", "ffe5c8", "ffe7cc", "ffe8d0", "ffead3", "ffebd7", "ffedda", "ffeede", "ffefe1", "fff0e4", "fff1e7", "fff3ea", "fff4ed", "fff5f0", "fff6f3", "fff7f7", "fff8f8", "fff9fb", "fff9fd", "fefaff", "fcf8ff", "faf7ff", "f7f5ff", "f5f4ff", "f3f3ff", "f1f1ff", "eff0ff", "eeefff", "eceeff", "eaedff", "e9ecff", "e7eaff", "e5e9ff", "e4e9ff", "e3e8ff", "e1e7ff", "e0e6ff", "dfe5ff", "dde4ff", "dce3ff", "dbe2ff", "dae2ff", "d9e1ff", "d8e0ff", "d7dfff", "d6dfff", "d5deff", "d4ddff", "d3ddff", "d2dcff", "d1dcff", "d0dbff", "cfdaff"]
    )
}


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


def decode_device_brightness(
    register: int, *, percentage: bool, wire_range: tuple[int, int] | None = None
) -> int:
    """Convert a device brightness register to Home Assistant's 0..255 scale."""
    if not 0 <= register <= 255:
        raise ValueError("Device brightness register must be from 0 to 255")
    if register == 0:
        return 0
    if wire_range is not None:
        low, high = wire_range
        clamped = min(max(register, low), high)
        percent = max(1, min(100, 1 - (-((clamped - low) * 100) // (high - low + 3))))
        return round(percent * 255 / 100)
    if percentage:
        return round(register * 255 / 100)
    return register


def decode_segment_brightness_percent(percent: int) -> int:
    """Convert an H617A segment-status percentage to HA's 0..255 scale.

    Segment status records carry their own 0..100 brightness byte before the
    RGB triplet. Unlike the whole-device register, zero is valid here and
    represents an explicitly dark segment.
    """
    if not 0 <= percent <= 100:
        raise ValueError("Segment brightness percentage must be from 0 to 100")
    return round(percent * 255 / 100)


def decode_h617a_segment_status_record(record: bytes) -> tuple[int, tuple[int, int, int]]:
    """Decode one H617A status record: percent followed by RGB."""
    if len(record) != 4:
        raise ValueError("H617A segment status record must contain four bytes")
    return decode_segment_brightness_percent(record[0]), (record[1], record[2], record[3])


def decode_version_reply(payload: bytes, *, hardware: bool) -> str:
    """Decode the shared AA 06/07 NUL-terminated version reply.

    Hardware replies prefix the text with selector 03.  The H6125 APK reads
    both fields before it chooses a revision-specific control grammar.
    """
    if hardware:
        if not payload or payload[0] != 0x03:
            raise ValueError("Hardware version reply is missing selector 03")
        payload = payload[1:]
    text = payload.split(b"\0", 1)[0]
    if not text:
        raise ValueError("Version reply is empty")
    try:
        value = text.decode("ascii")
    except UnicodeDecodeError as err:
        raise ValueError("Version reply is not ASCII") from err
    if not all(part.isdecimal() and part for part in value.split(".")):
        raise ValueError("Version reply is not a dotted numeric version")
    return value


def table_kelvin_rgb(kelvin: int) -> tuple[int, int, int]:
    """Return Govee's discrete companion RGB for an exact 100 K point."""
    try:
        red, green, blue = _TABLE_KELVIN_RGB[kelvin]
    except KeyError as err:
        raise ValueError("Kelvin value is not in Govee's 100 K companion table") from err
    return red, green, blue


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
