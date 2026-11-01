# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6072LowBlueLight(ReadWriteKaitaiStruct):
    """SPECULATIVE H6072 setting for owner confirmation #486.
    Method 1 carries enable, two opaque sibling fields, and a level.
    Sibling fields have no independently established control semantics.
    Unknown methods and values remain uninterpreted.
    """

    class Method(IntEnum):
        scale = 1

    class Operation(IntEnum):
        low_blue_light = 186

    class Prefix(IntEnum):
        write = 51
        status = 170
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6072LowBlueLight, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = KaitaiStream.resolve_enum(H6072LowBlueLight.Prefix, self._io.read_u1())
        if not self.header == H6072LowBlueLight.Prefix.status:
            raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.status, self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6072LowBlueLight.Operation, self._io.read_u1())
        if not self.domain == H6072LowBlueLight.Operation.low_blue_light:
            raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.domain, self._io, u"/seq/1")
        self.body = H6072LowBlueLight.State(self._io, self, self._root)
        self.body._read()
        self.padding = self._io.read_bytes(12)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.body._fetch_instances()


    def _write__seq(self, io=None):
        super(H6072LowBlueLight, self)._write__seq(io)
        self._io.write_u1(int(self.header))
        self._io.write_u1(int(self.domain))
        self.body._write__seq(self._io)
        self._io.write_bytes(self.padding)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not self.header == H6072LowBlueLight.Prefix.status:
            raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.status, self.header, None, u"/seq/0")
        if not self.domain == H6072LowBlueLight.Operation.low_blue_light:
            raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.domain, None, u"/seq/1")
        if self.body._root != self._root:
            raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
        if self.body._parent != self:
            raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        if len(self.padding) != 12:
            raise kaitaistruct.ConsistencyError(u"padding", 12, len(self.padding))
        self._dirty = False

    class Envelope(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072LowBlueLight.Envelope, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = KaitaiStream.resolve_enum(H6072LowBlueLight.Prefix, self._io.read_u1())
            if not  ((self.header == H6072LowBlueLight.Prefix.status) or (self.header == H6072LowBlueLight.Prefix.write)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.header, self._io, u"/types/envelope/seq/0")
            self.opcode = KaitaiStream.resolve_enum(H6072LowBlueLight.Operation, self._io.read_u1())
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, self._io, u"/types/envelope/seq/1")
            self.payload = self._io.read_bytes(17)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6072LowBlueLight.Envelope, self)._write__seq(io)
            self._io.write_u1(int(self.header))
            self._io.write_u1(int(self.opcode))
            self._io.write_bytes(self.payload)
            self._io.write_u1(self.checksum)


        def _check(self):
            if not  ((self.header == H6072LowBlueLight.Prefix.status) or (self.header == H6072LowBlueLight.Prefix.write)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.header, None, u"/types/envelope/seq/0")
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, None, u"/types/envelope/seq/1")
            if len(self.payload) != 17:
                raise kaitaistruct.ConsistencyError(u"payload", 17, len(self.payload))
            self._dirty = False


    class Query(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072LowBlueLight.Query, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = KaitaiStream.resolve_enum(H6072LowBlueLight.Prefix, self._io.read_u1())
            if not self.header == H6072LowBlueLight.Prefix.status:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.status, self.header, self._io, u"/types/query/seq/0")
            self.opcode = KaitaiStream.resolve_enum(H6072LowBlueLight.Operation, self._io.read_u1())
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, self._io, u"/types/query/seq/1")
            self.method = KaitaiStream.resolve_enum(H6072LowBlueLight.Method, self._io.read_u1())
            if not self.method == H6072LowBlueLight.Method.scale:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Method.scale, self.method, self._io, u"/types/query/seq/2")
            self.padding = self._io.read_bytes(16)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/query/seq/3")
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6072LowBlueLight.Query, self)._write__seq(io)
            self._io.write_u1(int(self.header))
            self._io.write_u1(int(self.opcode))
            self._io.write_u1(int(self.method))
            self._io.write_bytes(self.padding)
            self._io.write_u1(self.checksum)


        def _check(self):
            if not self.header == H6072LowBlueLight.Prefix.status:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.status, self.header, None, u"/types/query/seq/0")
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, None, u"/types/query/seq/1")
            if not self.method == H6072LowBlueLight.Method.scale:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Method.scale, self.method, None, u"/types/query/seq/2")
            if len(self.padding) != 16:
                raise kaitaistruct.ConsistencyError(u"padding", 16, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/query/seq/3")
            self._dirty = False


    class State(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072LowBlueLight.State, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.method = KaitaiStream.resolve_enum(H6072LowBlueLight.Method, self._io.read_u1())
            self.enabled = self._io.read_u1()
            self.sibling_1 = self._io.read_u1()
            self.sibling_2 = self._io.read_u1()
            self.level = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6072LowBlueLight.State, self)._write__seq(io)
            self._io.write_u1(int(self.method))
            self._io.write_u1(self.enabled)
            self._io.write_u1(self.sibling_1)
            self._io.write_u1(self.sibling_2)
            self._io.write_u1(self.level)


        def _check(self):
            self._dirty = False

        @property
        def is_supported(self):
            if hasattr(self, '_m_is_supported'):
                return self._m_is_supported

            self._m_is_supported =  ((self.method == H6072LowBlueLight.Method.scale) and (self.enabled <= 1) and (self.level >= self.minimum_level) and (self.level <= self.maximum_level)) 
            return getattr(self, '_m_is_supported', None)

        def _invalidate_is_supported(self):
            del self._m_is_supported
        @property
        def maximum_level(self):
            if hasattr(self, '_m_maximum_level'):
                return self._m_maximum_level

            self._m_maximum_level = 100
            return getattr(self, '_m_maximum_level', None)

        def _invalidate_maximum_level(self):
            del self._m_maximum_level
        @property
        def minimum_level(self):
            if hasattr(self, '_m_minimum_level'):
                return self._m_minimum_level

            self._m_minimum_level = 20
            return getattr(self, '_m_minimum_level', None)

        def _invalidate_minimum_level(self):
            del self._m_minimum_level

    class Write(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072LowBlueLight.Write, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = KaitaiStream.resolve_enum(H6072LowBlueLight.Prefix, self._io.read_u1())
            if not self.header == H6072LowBlueLight.Prefix.write:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.write, self.header, self._io, u"/types/write/seq/0")
            self.opcode = KaitaiStream.resolve_enum(H6072LowBlueLight.Operation, self._io.read_u1())
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, self._io, u"/types/write/seq/1")
            self.body = H6072LowBlueLight.State(self._io, self, self._root)
            self.body._read()
            _ = self.body
            if not _.is_supported:
                raise kaitaistruct.ValidationExprError(self.body, self._io, u"/types/write/seq/2")
            self.padding = self._io.read_bytes(12)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(H6072LowBlueLight.Write, self)._write__seq(io)
            self._io.write_u1(int(self.header))
            self._io.write_u1(int(self.opcode))
            self.body._write__seq(self._io)
            self._io.write_bytes(self.padding)
            self._io.write_u1(self.checksum)


        def _check(self):
            if not self.header == H6072LowBlueLight.Prefix.write:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Prefix.write, self.header, None, u"/types/write/seq/0")
            if not self.opcode == H6072LowBlueLight.Operation.low_blue_light:
                raise kaitaistruct.ValidationNotEqualError(H6072LowBlueLight.Operation.low_blue_light, self.opcode, None, u"/types/write/seq/1")
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            _ = self.body
            if not _.is_supported:
                raise kaitaistruct.ValidationExprError(self.body, None, u"/types/write/seq/2")
            if len(self.padding) != 12:
                raise kaitaistruct.ConsistencyError(u"padding", 12, len(self.padding))
            self._dirty = False



