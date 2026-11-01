# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h6199_upload_ack_payload
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199CommandAck(ReadWriteKaitaiStruct):
    """H6199 display-setting and relative-brightness writes acknowledge with the command opcode,
    a zero success byte, and zero padding. The acknowledgement does not echo the setting or
    value, so callers verify changes with the corresponding status query.
    Issue #294 direction30, position31 and Gradient A3 ACKs were observed in
    direct-register tests, not official-app BLE captures. Their use remains
    speculative; a zero ACK never establishes changed state.
    A3/04 DIY upload responses observed during issue #115 live qualification use
    the separate speculative payload; they are acknowledgements, not status.
    """

    class CommandOp(IntEnum):
        power = 1
        mode = 5
        strip_direction = 48
        camera_position = 49
        gradient = 163
        display_setting = 169
        relative_brightness = 174
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6199CommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_u1()
        if not  ((self.header == 51) or (self.header == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.header, self._io, u"/seq/0")
        if self.header == 51:
            pass
            self.opcode = KaitaiStream.resolve_enum(H6199CommandAck.CommandOp, self._io.read_u1())
            if not  ((self.opcode == H6199CommandAck.CommandOp.power) or (self.opcode == H6199CommandAck.CommandOp.mode) or (self.opcode == H6199CommandAck.CommandOp.display_setting) or (self.opcode == H6199CommandAck.CommandOp.relative_brightness) or (self.opcode == H6199CommandAck.CommandOp.strip_direction) or (self.opcode == H6199CommandAck.CommandOp.camera_position) or (self.opcode == H6199CommandAck.CommandOp.gradient)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.opcode, self._io, u"/seq/1")

        if self.header == 51:
            pass
            self.status = self._io.read_u1()
            if not self.status == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.status, self._io, u"/seq/2")

        if self.header == 51:
            pass
            self.padding = self._io.read_bytes(16)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/seq/3")

        if self.header == 163:
            pass
            self.upload = h6199_upload_ack_payload.H6199UploadAckPayload(self._io)
            self.upload._read()

        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        if self.header == 51:
            pass

        if self.header == 51:
            pass

        if self.header == 51:
            pass

        if self.header == 163:
            pass
            self.upload._fetch_instances()



    def _write__seq(self, io=None):
        super(H6199CommandAck, self)._write__seq(io)
        self._io.write_u1(self.header)
        if self.header == 51:
            pass
            self._io.write_u1(int(self.opcode))

        if self.header == 51:
            pass
            self._io.write_u1(self.status)

        if self.header == 51:
            pass
            self._io.write_bytes(self.padding)

        if self.header == 163:
            pass
            self.upload._write__seq(self._io)

        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.header == 51) or (self.header == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.header, None, u"/seq/0")
        if self.header == 51:
            pass
            if not  ((self.opcode == H6199CommandAck.CommandOp.power) or (self.opcode == H6199CommandAck.CommandOp.mode) or (self.opcode == H6199CommandAck.CommandOp.display_setting) or (self.opcode == H6199CommandAck.CommandOp.relative_brightness) or (self.opcode == H6199CommandAck.CommandOp.strip_direction) or (self.opcode == H6199CommandAck.CommandOp.camera_position) or (self.opcode == H6199CommandAck.CommandOp.gradient)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.opcode, None, u"/seq/1")

        if self.header == 51:
            pass
            if not self.status == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.status, None, u"/seq/2")

        if self.header == 51:
            pass
            if len(self.padding) != 16:
                raise kaitaistruct.ConsistencyError(u"padding", 16, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/seq/3")

        if self.header == 163:
            pass

        self._dirty = False


