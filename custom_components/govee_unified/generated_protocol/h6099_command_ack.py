# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099CommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 command ACK for issue #258.  Android 7.6.01 H6099
    single-frame command handlers read a zero success byte at body offset zero.
    Tail bytes remain unknown; this structure records receipt, never setting
    values or fresh device state.  Exact-device reply tails, firmware differences,
    and encryption need owner qualification.  Only in-scope command opcodes are
    named.
    """

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        installation_direction = 48
        display_setting = 169
        relative_brightness = 174
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099CommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6099CommandAck.CommandOp, self._io.read_u1())
        if not  ((self.opcode == H6099CommandAck.CommandOp.power) or (self.opcode == H6099CommandAck.CommandOp.brightness) or (self.opcode == H6099CommandAck.CommandOp.mode) or (self.opcode == H6099CommandAck.CommandOp.installation_direction) or (self.opcode == H6099CommandAck.CommandOp.display_setting) or (self.opcode == H6099CommandAck.CommandOp.relative_brightness)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.opcode, self._io, u"/seq/1")
        self.status = self._io.read_u1()
        if not self.status == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.status, self._io, u"/seq/2")
        self.unknown_tail = self._io.read_bytes(16)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6099CommandAck, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        if not  ((self.opcode == H6099CommandAck.CommandOp.power) or (self.opcode == H6099CommandAck.CommandOp.brightness) or (self.opcode == H6099CommandAck.CommandOp.mode) or (self.opcode == H6099CommandAck.CommandOp.installation_direction) or (self.opcode == H6099CommandAck.CommandOp.display_setting) or (self.opcode == H6099CommandAck.CommandOp.relative_brightness)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.opcode, None, u"/seq/1")
        if not self.status == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.status, None, u"/seq/2")
        if len(self.unknown_tail) != 16:
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 16, len(self.unknown_tail))
        self._dirty = False


