# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60aBulk(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A1 and H60A6 support for issue #402.  Compatibility
    hypothesis: AC03 reads return ordered, fixed-size response frames carrying
    a complete sequence of domain/length/value records.  The first response
    declares the frame count and final-frame payload length.  Single-frame
    responses carry at most twelve bytes; continuation frames carry seventeen.
    Mode, native H60A6 zone flags and power-on behaviour are independent
    observations, not proof of uploaded content or emitted light.  The AC30
    record has no master flag.  Unknown records, flag bits and suffixes remain
    opaque.  Capture qualification, other revisions and unsolicited response
    timing remain unresolved.  No timer or network records are interpreted.
    """

    class Domain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
        zone_enable = 48
        power_on_behaviour = 65

    class Mode(IntEnum):
        scene = 4
        diy = 10
        static_colour = 13
        music = 19
        static = 21

    class PowerOnState(IntEnum):
        previous = 0
        on = 1
        off = 2
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60aBulk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAC":
            raise kaitaistruct.ValidationNotEqualError(b"\xAC", self.header, self._io, u"/seq/0")
        self.index = self._io.read_u1()
        _on = self.index
        if _on == 0:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H60aBulk.FirstFrame(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.index
        if _on == 0:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H60aBulk, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(self.index)
        _on = self.index
        if _on == 0:
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
        if not self.header == b"\xAC":
            raise kaitaistruct.ValidationNotEqualError(b"\xAC", self.header, None, u"/seq/0")
        _on = self.index
        if _on == 0:
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

    class BrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColourBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.ColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.kelvin = self._io.read_u2be()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H60aBulk.ColourBody, self)._write__seq(io)
            self.rgb._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class FirstFrame(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.FirstFrame, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.frame_count = self._io.read_u2le()
            self.final_size = self._io.read_u1()
            self.command = self._io.read_bytes(1)
            if not self.command == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.command, self._io, u"/types/first_frame/seq/2")
            self.discriminator = self._io.read_bytes(1)
            if not self.discriminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.discriminator, self._io, u"/types/first_frame/seq/3")
            self.payload = self._io.read_bytes(12)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.FirstFrame, self)._write__seq(io)
            self._io.write_u2le(self.frame_count)
            self._io.write_u1(self.final_size)
            self._io.write_bytes(self.command)
            self._io.write_bytes(self.discriminator)
            self._io.write_bytes(self.payload)


        def _check(self):
            if len(self.command) != 1:
                raise kaitaistruct.ConsistencyError(u"command", 1, len(self.command))
            if not self.command == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.command, None, u"/types/first_frame/seq/2")
            if len(self.discriminator) != 1:
                raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
            if not self.discriminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.discriminator, None, u"/types/first_frame/seq/3")
            if len(self.payload) != 12:
                raise kaitaistruct.ConsistencyError(u"payload", 12, len(self.payload))
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H60aBulk.Mode, self._io.read_u1())
            _on = self.mode
            if _on == H60aBulk.Mode.diy:
                pass
                self._raw_detail = self._io.read_bytes_full()
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H60aBulk.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H60aBulk.Mode.scene:
                pass
                self._raw_detail = self._io.read_bytes_full()
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H60aBulk.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H60aBulk.Mode.static:
                pass
                self._raw_detail = self._io.read_bytes_full()
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H60aBulk.StaticBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H60aBulk.Mode.static_colour:
                pass
                self._raw_detail = self._io.read_bytes_full()
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H60aBulk.ColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H60aBulk.Mode.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H60aBulk.Mode.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H60aBulk.Mode.static:
                pass
                self.detail._fetch_instances()
            elif _on == H60aBulk.Mode.static_colour:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H60aBulk.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H60aBulk.Mode.diy:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(self._io.size() - self._io.pos())))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    parent.write_bytes(self._raw_detail)
                    if not parent.is_eof():
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 0, parent.size() - parent.pos())
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H60aBulk.Mode.scene:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(self._io.size() - self._io.pos())))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    parent.write_bytes(self._raw_detail)
                    if not parent.is_eof():
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 0, parent.size() - parent.pos())
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H60aBulk.Mode.static:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(self._io.size() - self._io.pos())))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    parent.write_bytes(self._raw_detail)
                    if not parent.is_eof():
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 0, parent.size() - parent.pos())
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H60aBulk.Mode.static_colour:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(self._io.size() - self._io.pos())))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    parent.write_bytes(self._raw_detail)
                    if not parent.is_eof():
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 0, parent.size() - parent.pos())
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            else:
                pass
                self._io.write_bytes(self.detail)
                if not self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"detail", 0, self._io.size() - self._io.pos())


        def _check(self):
            _on = self.mode
            if _on == H60aBulk.Mode.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H60aBulk.Mode.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H60aBulk.Mode.static:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H60aBulk.Mode.static_colour:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            else:
                pass
            self._dirty = False


    class Payload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.Payload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.records = []
            i = 0
            while not self._io.is_eof():
                _t_records = H60aBulk.Record(self._io, self, self._root)
                try:
                    _t_records._read()
                finally:
                    self.records.append(_t_records)
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.records)):
                pass
                self.records[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H60aBulk.Payload, self)._write__seq(io)
            for i in range(len(self.records)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"records", 0, self._io.size() - self._io.pos())
                self.records[i]._write__seq(self._io)

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"records", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.records)):
                pass
                if self.records[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"records", self._root, self.records[i]._root)
                if self.records[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"records", self, self.records[i]._parent)

            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class PowerOnBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.PowerOnBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_prefix = self._io.read_u1()
            self.state = KaitaiStream.resolve_enum(H60aBulk.PowerOnState, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.PowerOnBody, self)._write__seq(io)
            self._io.write_u1(self.unknown_prefix)
            self._io.write_u1(int(self.state))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Query(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.Query, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = self._io.read_bytes(2)
            if not self.header == b"\xAC\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\xAC\x03", self.header, self._io, u"/types/query/seq/0")
            self.domain_count = self._io.read_u1()
            if not self.domain_count <= 16:
                raise kaitaistruct.ValidationGreaterThanError(16, self.domain_count, self._io, u"/types/query/seq/1")
            self.domains = []
            for i in range(self.domain_count):
                self.domains.append(KaitaiStream.resolve_enum(H60aBulk.Domain, self._io.read_u1()))

            self.padding = self._io.read_bytes(16 - self.domain_count)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.domains)):
                pass



        def _write__seq(self, io=None):
            super(H60aBulk.Query, self)._write__seq(io)
            self._io.write_bytes(self.header)
            self._io.write_u1(self.domain_count)
            for i in range(len(self.domains)):
                pass
                self._io.write_u1(int(self.domains[i]))

            self._io.write_bytes(self.padding)
            self._io.write_u1(self.checksum)


        def _check(self):
            if len(self.header) != 2:
                raise kaitaistruct.ConsistencyError(u"header", 2, len(self.header))
            if not self.header == b"\xAC\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\xAC\x03", self.header, None, u"/types/query/seq/0")
            if not self.domain_count <= 16:
                raise kaitaistruct.ValidationGreaterThanError(16, self.domain_count, None, u"/types/query/seq/1")
            if len(self.domains) != self.domain_count:
                raise kaitaistruct.ConsistencyError(u"domains", self.domain_count, len(self.domains))
            for i in range(len(self.domains)):
                pass

            if len(self.padding) != 16 - self.domain_count:
                raise kaitaistruct.ConsistencyError(u"padding", 16 - self.domain_count, len(self.padding))
            self._dirty = False


    class Record(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.Record, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.domain = KaitaiStream.resolve_enum(H60aBulk.Domain, self._io.read_u1())
            self.length = self._io.read_u1()
            _on = self.domain
            if _on == H60aBulk.Domain.brightness:
                pass
                self._raw_body = self._io.read_bytes(self.length)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60aBulk.BrightnessBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60aBulk.Domain.colour_mode:
                pass
                self._raw_body = self._io.read_bytes(self.length)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60aBulk.ModeBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60aBulk.Domain.power:
                pass
                self._raw_body = self._io.read_bytes(self.length)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60aBulk.PowerBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60aBulk.Domain.power_on_behaviour:
                pass
                self._raw_body = self._io.read_bytes(self.length)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60aBulk.PowerOnBody(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60aBulk.Domain.zone_enable:
                pass
                self._raw_body = self._io.read_bytes(self.length)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60aBulk.ZoneBody(_io__raw_body, self, self._root)
                self.body._read()
            else:
                pass
                self.body = self._io.read_bytes(self.length)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.domain
            if _on == H60aBulk.Domain.brightness:
                pass
                self.body._fetch_instances()
            elif _on == H60aBulk.Domain.colour_mode:
                pass
                self.body._fetch_instances()
            elif _on == H60aBulk.Domain.power:
                pass
                self.body._fetch_instances()
            elif _on == H60aBulk.Domain.power_on_behaviour:
                pass
                self.body._fetch_instances()
            elif _on == H60aBulk.Domain.zone_enable:
                pass
                self.body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H60aBulk.Record, self)._write__seq(io)
            self._io.write_u1(int(self.domain))
            self._io.write_u1(self.length)
            _on = self.domain
            if _on == H60aBulk.Domain.brightness:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60aBulk.Domain.colour_mode:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60aBulk.Domain.power:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60aBulk.Domain.power_on_behaviour:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60aBulk.Domain.zone_enable:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            else:
                pass
                self._io.write_bytes(self.body)


        def _check(self):
            _on = self.domain
            if _on == H60aBulk.Domain.brightness:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60aBulk.Domain.colour_mode:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60aBulk.Domain.power:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60aBulk.Domain.power_on_behaviour:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60aBulk.Domain.zone_enable:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            else:
                pass
                if len(self.body) != self.length:
                    raise kaitaistruct.ConsistencyError(u"body", self.length, len(self.body))
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class StaticBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.StaticBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_flag = self._io.read_u1()
            self.kelvin = self._io.read_u2be()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.StaticBody, self)._write__seq(io)
            self._io.write_u1(self.unknown_flag)
            self._io.write_u2be(self.kelvin)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ZoneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60aBulk.ZoneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.panel_flags = self._io.read_u1()
            self.ring_flags = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60aBulk.ZoneBody, self)._write__seq(io)
            self._io.write_u1(self.panel_flags)
            self._io.write_u1(self.ring_flags)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def panel_enabled(self):
            if hasattr(self, '_m_panel_enabled'):
                return self._m_panel_enabled

            self._m_panel_enabled = self.panel_flags & 1 != 0
            return getattr(self, '_m_panel_enabled', None)

        def _invalidate_panel_enabled(self):
            del self._m_panel_enabled
        @property
        def ring_enabled(self):
            if hasattr(self, '_m_ring_enabled'):
                return self._m_ring_enabled

            self._m_ring_enabled = self.ring_flags & 1 != 0
            return getattr(self, '_m_ring_enabled', None)

        def _invalidate_ring_enabled(self):
            del self._m_ring_enabled


