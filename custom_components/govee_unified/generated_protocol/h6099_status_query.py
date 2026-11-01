# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099StatusQuery(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 query frame for issue #258.  In Android 7.6.01, H6099 mode
    queries use selector 01 and segment queries request four groups for fourteen
    logical zones.  Scalar white balance uses A9 06, black-border removal uses
    A9 0B, and relative brightness uses AE 01.  AA40 queries the signed
    big-endian physical IC count (distinct from the 14 logical zones).  AA20 and
    AA21 query Wi-Fi hardware and software identity.  AA30 queries installation
    direction and AA32 queries camera health with zero-filled bodies; camera
    position (31) is separate and not queried here.  Encryption is outside this
    logical frame; owner acceptance, firmware differences, and unused bytes
    remain unresolved.
    H6097 issue #431 independently shares these query selectors and fourteen-zone
    paging.  Its ordinary three-state power-on query has a separate exact root.
    """

    class DisplaySetting(IntEnum):
        scalar_white_balance = 6
        blank_screen = 10
        black_border = 11

    class QueryDomain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
        firmware = 6
        hardware = 7
        subordinate_20 = 32
        subordinate_21 = 33
        installation_direction = 48
        camera_health = 50
        physical_ic_count = 64
        segments = 165
        display_setting = 169
        relative_brightness = 174
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099StatusQuery, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6099StatusQuery.QueryDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6099StatusQuery.QueryDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.camera_health:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.colour_mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ColourModeQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.display_setting:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.DisplaySettingQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.HardwareQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.installation_direction:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.physical_ic_count:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.relative_brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.RelativeBrightnessQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.segments:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.SegmentQueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.subordinate_20:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusQuery.QueryDomain.subordinate_21:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusQuery.ZeroBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6099StatusQuery.QueryDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.camera_health:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.colour_mode:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.display_setting:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.installation_direction:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.physical_ic_count:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.relative_brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.segments:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.subordinate_20:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusQuery.QueryDomain.subordinate_21:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6099StatusQuery, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6099StatusQuery.QueryDomain.brightness:
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
        elif _on == H6099StatusQuery.QueryDomain.camera_health:
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
        elif _on == H6099StatusQuery.QueryDomain.colour_mode:
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
        elif _on == H6099StatusQuery.QueryDomain.display_setting:
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
        elif _on == H6099StatusQuery.QueryDomain.firmware:
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
        elif _on == H6099StatusQuery.QueryDomain.hardware:
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
        elif _on == H6099StatusQuery.QueryDomain.installation_direction:
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
        elif _on == H6099StatusQuery.QueryDomain.physical_ic_count:
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
        elif _on == H6099StatusQuery.QueryDomain.power:
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
        elif _on == H6099StatusQuery.QueryDomain.relative_brightness:
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
        elif _on == H6099StatusQuery.QueryDomain.segments:
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
        elif _on == H6099StatusQuery.QueryDomain.subordinate_20:
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
        elif _on == H6099StatusQuery.QueryDomain.subordinate_21:
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
        if _on == H6099StatusQuery.QueryDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.camera_health:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.colour_mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.display_setting:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.firmware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.hardware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.installation_direction:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.physical_ic_count:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.relative_brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.segments:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.subordinate_20:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusQuery.QueryDomain.subordinate_21:
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

    class ColourModeQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.ColourModeQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, self._io, u"/types/colour_mode_query_body/seq/0")
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/colour_mode_query_body/seq/1")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6099StatusQuery.ColourModeQueryBody, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, None, u"/types/colour_mode_query_body/seq/0")
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/colour_mode_query_body/seq/1")

            self._dirty = False


    class DisplaySettingQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.DisplaySettingQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.setting = KaitaiStream.resolve_enum(H6099StatusQuery.DisplaySetting, self._io.read_u1())
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/display_setting_query_body/seq/1")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6099StatusQuery.DisplaySettingQueryBody, self)._write__seq(io)
            self._io.write_u1(int(self.setting))
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/display_setting_query_body/seq/1")

            self._dirty = False


    class HardwareQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.HardwareQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.selector, self._io, u"/types/hardware_query_body/seq/0")
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/hardware_query_body/seq/1")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6099StatusQuery.HardwareQueryBody, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.selector, None, u"/types/hardware_query_body/seq/0")
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/hardware_query_body/seq/1")

            self._dirty = False


    class RelativeBrightnessQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.RelativeBrightnessQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, self._io, u"/types/relative_brightness_query_body/seq/0")
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/relative_brightness_query_body/seq/1")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6099StatusQuery.RelativeBrightnessQueryBody, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, None, u"/types/relative_brightness_query_body/seq/0")
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/relative_brightness_query_body/seq/1")

            self._dirty = False


    class SegmentQueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.SegmentQueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.group = self._io.read_u1()
            if not self.group >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.group, self._io, u"/types/segment_query_body/seq/0")
            if not self.group <= 4:
                raise kaitaistruct.ValidationGreaterThanError(4, self.group, self._io, u"/types/segment_query_body/seq/0")
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
            super(H6099StatusQuery.SegmentQueryBody, self)._write__seq(io)
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
            if not self.group <= 4:
                raise kaitaistruct.ValidationGreaterThanError(4, self.group, None, u"/types/segment_query_body/seq/0")
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/segment_query_body/seq/1")

            self._dirty = False


    class ZeroBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusQuery.ZeroBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.zeros = []
            i = 0
            while not self._io.is_eof():
                self.zeros.append(self._io.read_u1())
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], self._io, u"/types/zero_body/seq/0")
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.zeros)):
                pass



        def _write__seq(self, io=None):
            super(H6099StatusQuery.ZeroBody, self)._write__seq(io)
            for i in range(len(self.zeros)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.zeros[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"zeros", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.zeros)):
                pass
                if not self.zeros[i] == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.zeros[i], None, u"/types/zero_body/seq/0")

            self._dirty = False



