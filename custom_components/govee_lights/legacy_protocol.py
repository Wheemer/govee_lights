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
