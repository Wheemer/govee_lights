"""LAN-local packet helpers shared with the original Govee Lights transport."""

from __future__ import annotations


def _sign(frame: bytes) -> int:
    checksum = 0
    for value in frame:
        checksum ^= value
    return checksum & 0xFF


def _segment_color_packet(red: int, green: int, blue: int, mask: int) -> bytes:
    if not 0 <= mask <= 0x7FFF:
        raise ValueError("Segment mask must fit the 15-bit legacy protocol")
    body = bytes((0x33, 0x05, 0x15, 0x01, red, green, blue)) + bytes(5) + bytes((mask & 0xFF, mask >> 8))
    body = body.ljust(19, b"\0")
    return body + bytes((_sign(body),))


class GoveeBLE:
    """Compatibility surface used by the LAN ptReal segment writer."""

    @staticmethod
    def build_segment_packets(
        colors: dict[int, tuple[int, int, int]], count: int, device: str
    ) -> list[bytes]:
        if count == 0:
            raise ValueError(f"Govee {device} has no segment control")
        masks: dict[tuple[int, int, int], int] = {}
        for index, color in colors.items():
            if not 0 <= index < count:
                raise ValueError(f"Segment {index + 1} out of range for Govee {device} (1-{count})")
            masks[color] = masks.get(color, 0) | (1 << index)
        return [_segment_color_packet(red, green, blue, mask) for (red, green, blue), mask in masks.items()]
