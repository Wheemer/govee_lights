# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h60a_bulk
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6097Control(ReadWriteKaitaiStruct):
    """SPECULATIVE H6097 support for issue #431.  The ordinary 41 register uses
    selector 02 and the shared previous/on/off state codebook, not a boolean or
    bulk query.  Reply availability/status is independent of the state byte.
    Unknown state values and suffixes remain opaque to runtime semantics.
    Exact-device option mapping, reply timing and other revisions need
    qualification.
    """

    class Command(IntEnum):
        power_on_behaviour = 65
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6097Control, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6097Control.Command, self._io.read_u1())
        if not self.opcode == H6097Control.Command.power_on_behaviour:
            raise kaitaistruct.ValidationNotEqualError(H6097Control.Command.power_on_behaviour, self.opcode, self._io, u"/seq/1")
        self._raw_body = self._io.read_bytes(17)
        _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
        self.body = H6097Control.PowerOnCommand(_io__raw_body, self, self._root)
        self.body._read()
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.body._fetch_instances()


    def _write__seq(self, io=None):
        super(H6097Control, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _io__raw_body = KaitaiStream(BytesIO(bytearray(17)))
        self._io.add_child_stream(_io__raw_body)
        _pos2 = self._io.pos()
        self._io.seek(self._io.pos() + (17))
        def handler(parent, _io__raw_body=_io__raw_body):
            self._raw_body = _io__raw_body.to_byte_array()
            if len(self._raw_body) != 17:
                raise kaitaistruct.ConsistencyError(u"raw(body)", 17, len(self._raw_body))
            parent.write_bytes(self._raw_body)
        _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
        self.body._write__seq(_io__raw_body)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        if not self.opcode == H6097Control.Command.power_on_behaviour:
            raise kaitaistruct.ValidationNotEqualError(H6097Control.Command.power_on_behaviour, self.opcode, None, u"/seq/1")
        if self.body._root != self._root:
            raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
        if self.body._parent != self:
            raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        self._dirty = False

    class PowerOnCommand(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6097Control.PowerOnCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.selector, self._io, u"/types/power_on_command/seq/0")
            self.state = KaitaiStream.resolve_enum(h60a_bulk.H60aBulk.PowerOnState, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6097Control.PowerOnCommand, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            self._io.write_u1(int(self.state))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.selector, None, u"/types/power_on_command/seq/0")
            self._dirty = False


    class PowerOnState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6097Control.PowerOnState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.availability = self._io.read_u1()
            self.state = KaitaiStream.resolve_enum(h60a_bulk.H60aBulk.PowerOnState, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6097Control.PowerOnState, self)._write__seq(io)
            self._io.write_u1(self.availability)
            self._io.write_u1(int(self.state))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Query(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6097Control.Query, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = self._io.read_bytes(3)
            if not self.header == b"\xAA\x41\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\xAA\x41\x02", self.header, self._io, u"/types/query/seq/0")
            self.unknown_tail = self._io.read_bytes(16)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6097Control.Query, self)._write__seq(io)
            self._io.write_bytes(self.header)
            self._io.write_bytes(self.unknown_tail)
            self._io.write_u1(self.checksum)


        def _check(self):
            if len(self.header) != 3:
                raise kaitaistruct.ConsistencyError(u"header", 3, len(self.header))
            if not self.header == b"\xAA\x41\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\xAA\x41\x02", self.header, None, u"/types/query/seq/0")
            if len(self.unknown_tail) != 16:
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 16, len(self.unknown_tail))
            self._dirty = False



