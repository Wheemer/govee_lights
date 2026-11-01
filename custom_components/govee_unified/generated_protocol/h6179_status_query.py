# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6179StatusQuery(ReadWriteKaitaiStruct):
    """SPECULATIVE H6179 compatibility hypothesis: exact-SKU status queries use a
    20-byte 0xaa envelope and the candidate domain and selector bytes represented
    below.
    Unresolved assumptions: no exact-model capture verifies the domain meanings,
    mode, hardware, or timer selectors, opaque body bytes, or XOR checksum byte.
    """

    class HardwareQuerySelector(IntEnum):
        primary = 3

    class ModeQuerySelector(IntEnum):
        current = 1

    class StatusDomain(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        firmware = 6
        hardware = 7
        limit = 14
        sleep = 17
        wake = 18
        timers = 35

    class TimersQuerySelector(IntEnum):
        all = 255
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6179StatusQuery, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6179StatusQuery.StatusDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6179StatusQuery.StatusDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.HardwareQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.limit:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.ModeQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.sleep:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.timers:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.TimersQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusQuery.StatusDomain.wake:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusQuery.OpaqueBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6179StatusQuery.StatusDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.limit:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.mode:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.sleep:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.timers:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusQuery.StatusDomain.wake:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6179StatusQuery, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6179StatusQuery.StatusDomain.brightness:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.firmware:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.hardware:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.limit:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.mode:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.power:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.sleep:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.timers:
            pass
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
        elif _on == H6179StatusQuery.StatusDomain.wake:
            pass
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
        else:
            pass
            self._io.write_bytes(self.body)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, None, u"/seq/0")
        _on = self.domain
        if _on == H6179StatusQuery.StatusDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.firmware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.hardware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.limit:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.sleep:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.timers:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusQuery.StatusDomain.wake:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        else:
            pass
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class HardwareQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusQuery.HardwareQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = KaitaiStream.resolve_enum(H6179StatusQuery.HardwareQuerySelector, self._io.read_u1())
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusQuery.HardwareQueryBody, self)._write__seq(io)
            self._io.write_u1(int(self.selector))
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ModeQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusQuery.ModeQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = KaitaiStream.resolve_enum(H6179StatusQuery.ModeQuerySelector, self._io.read_u1())
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusQuery.ModeQueryBody, self)._write__seq(io)
            self._io.write_u1(int(self.selector))
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class OpaqueBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusQuery.OpaqueBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusQuery.OpaqueBody, self)._write__seq(io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class TimersQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusQuery.TimersQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = KaitaiStream.resolve_enum(H6179StatusQuery.TimersQuerySelector, self._io.read_u1())
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusQuery.TimersQueryBody, self)._write__seq(io)
            self._io.write_u1(int(self.selector))
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



