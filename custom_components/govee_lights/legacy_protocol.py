"""Pure helpers for Govee's unencrypted 20-byte legacy BLE frames.

This module deliberately contains no Home Assistant or BLE-client imports so
the byte-level protocol can be regression tested independently. It covers
only the shared legacy frame envelope; model-specific payload selection stays
in the BLE coordinator until it has model-specific evidence.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import array

LEGACY_FRAME_LENGTH = 20
LEGACY_PAYLOAD_LENGTH = 17
LEGACY_FRAME_PREFIX = 0x33


def sign_payload(data: bytes | bytearray | array.array[int]) -> int:
    """Return the legacy XOR checksum for an unsigned frame."""
    checksum = 0
    for value in data:
        checksum ^= value
    return checksum & 0xFF


def build_single_packet(cmd: int, payload: bytes | list[int]) -> bytes:
    """Build a signed 20-byte legacy command frame.

    ``payload`` is bounded to the 17 bytes available after the frame prefix
    and command. The final byte is always the XOR of the preceding 19 bytes.
    """
    if len(payload) > LEGACY_PAYLOAD_LENGTH:
        raise ValueError("Payload too long")

    frame = bytes([LEGACY_FRAME_PREFIX, cmd & 0xFF]) + bytes(payload)
    frame += bytes(LEGACY_FRAME_LENGTH - 1 - len(frame))
    return frame + bytes([sign_payload(frame)])


def build_h617a_segment_color_packet(red: int, green: int, blue: int, mask: int) -> bytes:
    """Build the shared H617A-family segmented RGB command.

    The H617A grammar uses mode ``0x15``, static-colour selector ``0x01``,
    and a little-endian segment bitmask. The packet form is also used by the
    experimentally profiled H6076, H617F, H1A42, and H61F5 models.
    """
    if not 0 <= mask <= 0x7FFF:
        raise ValueError("Segment mask must fit the 15-bit legacy protocol")
    return build_single_packet(
        0x05,
        [0x15, 0x01, red, green, blue, 0x00, 0x00, 0x00, 0x00, 0x00, mask & 0xFF, mask >> 8],
    )


def build_h617a_segment_color_temp_packet(
    kelvin: int, red: int, green: int, blue: int, mask: int
) -> bytes:
    """Build the H617A-family segmented native-white command."""
    if not 0 <= kelvin <= 0xFFFF:
        raise ValueError("Kelvin value must fit the legacy protocol")
    if not 0 <= mask <= 0x7FFF:
        raise ValueError("Segment mask must fit the 15-bit legacy protocol")
    return build_single_packet(
        0x05,
        [
            0x15,
            0x01,
            0xFF,
            0xFF,
            0xFF,
            kelvin >> 8,
            kelvin & 0xFF,
            red,
            green,
            blue,
            mask & 0xFF,
            mask >> 8,
        ],
    )
