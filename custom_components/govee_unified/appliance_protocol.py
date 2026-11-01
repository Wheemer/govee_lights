"""Local BLE frames for non-light Govee appliance families.

The H7172 ice-maker family was reconstructed from Govee Home 7.5.30's
``com.govee.h7172`` APK module.  It uses the familiar 20-byte XOR envelope,
but its command payloads are appliance commands rather than light commands.
Keeping this separate makes it impossible for a light profile to accidentally
send RGB/status queries to an appliance.
"""

from __future__ import annotations

from .transport import xor_checksum

_FRAME_SIZE = 20
_H7172_POWER_COMMAND = 0x01

# APK WorkStatus values from com.govee.h7172.adjust.WorkStatus.
H7172_WORK_STATUS = {
    0: "idle",
    1: "ice_making",
    2: "ice_full",
    3: "washing",
    4: "wash_finished",
    5: "scheduled",
}


def build_legacy_frame(prefix: int, command: int, payload: bytes = b"") -> bytes:
    """Build the APK's 20-byte, XOR-signed single-controller frame."""
    if not 0 <= prefix <= 0xFF or not 0 <= command <= 0xFF or len(payload) > 17:
        raise ValueError("invalid legacy appliance frame")
    frame = bytearray((prefix, command))
    frame.extend(payload)
    frame.extend(bytes(_FRAME_SIZE - 1 - len(frame)))
    frame.append(xor_checksum(frame))
    return bytes(frame)


def build_h7172_power_query() -> bytes:
    """Query H7172/H7178/H717D power state (APK AbsSingleController read)."""
    return build_legacy_frame(0xAA, _H7172_POWER_COMMAND)


def build_h7172_power_write(enabled: bool) -> bytes:
    """Build the APK SwitchController power frame.

    The app sends ``33 01 01 01`` to start ice-making: the first byte is
    power and the second selects the normal-start route.  Off is ``33 01 00``.
    """
    return build_legacy_frame(
        0x33,
        _H7172_POWER_COMMAND,
        bytes((1, 1)) if enabled else bytes((0,)),
    )


def build_standard_power_write(enabled: bool) -> bytes:
    """Build Govee's shared APK ``SwitchController`` write.

    The H7111 fan and H7121 air-purifier modules both instantiate the shared
    controller, whose ``getValue`` serializes ``33 01 <0|1>``.
    """
    return build_legacy_frame(0x33, _H7172_POWER_COMMAND, bytes((int(enabled),)))


def parse_h7172_power_reply(frame: bytes) -> bool | None:
    """Return power from an H7172 read/write reply, or ``None`` if unrelated."""
    if len(frame) != _FRAME_SIZE or xor_checksum(frame[:19]) != frame[19]:
        return None
    if frame[0] != 0xAA or frame[1] != _H7172_POWER_COMMAND:
        return None
    return bool(frame[2])


def parse_h7172_work_status(frame: bytes) -> str | None:
    """Decode the APK's spontaneous ``AA 19`` appliance work-status report."""
    if len(frame) != _FRAME_SIZE or xor_checksum(frame[:19]) != frame[19]:
        return None
    if frame[:2] != b"\xaa\x19":
        return None
    return H7172_WORK_STATUS.get(frame[2], "unknown")
