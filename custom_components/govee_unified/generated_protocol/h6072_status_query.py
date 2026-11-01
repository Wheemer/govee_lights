# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import status_query
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6072StatusQuery(ReadWriteKaitaiStruct):
    """SPECULATIVE H6072, owner confirmations #486.
    Compatibility hypothesis: common basic queries and three newer A5 segment
    groups. Exact-model captures and revision-specific response timing are unqualified.
    """

    class QueryDomain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
        firmware = 6
        hardware = 7
        multi_effect = 163
        segments = 165
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6072StatusQuery, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6072StatusQuery.QueryDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6072StatusQuery.QueryDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.ZeroBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.colour_mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.ColourModeQueryBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.ZeroBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.HardwareQueryBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.multi_effect:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.ZeroBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = status_query.StatusQuery.ZeroBody(_io__raw_body)
            self.body._read()
        elif _on == H6072StatusQuery.QueryDomain.segments:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6072StatusQuery.SegmentQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6072StatusQuery.QueryDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.colour_mode:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.multi_effect:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6072StatusQuery.QueryDomain.segments:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6072StatusQuery, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6072StatusQuery.QueryDomain.brightness:
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
        elif _on == H6072StatusQuery.QueryDomain.colour_mode:
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
        elif _on == H6072StatusQuery.QueryDomain.firmware:
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
        elif _on == H6072StatusQuery.QueryDomain.hardware:
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
        elif _on == H6072StatusQuery.QueryDomain.multi_effect:
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
        elif _on == H6072StatusQuery.QueryDomain.power:
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
        elif _on == H6072StatusQuery.QueryDomain.segments:
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
        if _on == H6072StatusQuery.QueryDomain.brightness:
            pass
        elif _on == H6072StatusQuery.QueryDomain.colour_mode:
            pass
        elif _on == H6072StatusQuery.QueryDomain.firmware:
            pass
        elif _on == H6072StatusQuery.QueryDomain.hardware:
            pass
        elif _on == H6072StatusQuery.QueryDomain.multi_effect:
            pass
        elif _on == H6072StatusQuery.QueryDomain.power:
            pass
        elif _on == H6072StatusQuery.QueryDomain.segments:
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

    class SegmentQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072StatusQuery.SegmentQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.group = self._io.read_u1()
            if not self.group >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.group, self._io, u"/types/segment_query_body/seq/0")
            if not self.group <= 3:
                raise kaitaistruct.ValidationGreaterThanError(3, self.group, self._io, u"/types/segment_query_body/seq/0")
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/segment_query_body/seq/1")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6072StatusQuery.SegmentQueryBody, self)._write__seq(io)
            self._io.write_u1(self.group)
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not self.group >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.group, None, u"/types/segment_query_body/seq/0")
            if not self.group <= 3:
                raise kaitaistruct.ValidationGreaterThanError(3, self.group, None, u"/types/segment_query_body/seq/0")
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/segment_query_body/seq/1")

            self._dirty = False



