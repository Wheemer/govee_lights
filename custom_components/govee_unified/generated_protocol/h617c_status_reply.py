# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_segment_page
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H617cStatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H617C, issue #413.
    Compatibility hypothesis: the H617C modern DreamColor route (product type 70,
    Pact 10/1) replies with 20-byte XOR-checksummed AA frames carrying power,
    percentage brightness, active colour mode, firmware and hardware version
    strings, the gradual-change boolean register (AA A3), and fifteen logical
    segments across five three-record AA A5 pages.  Static colour replies (0x15)
    carry the gradual flag and big-endian Kelvin; scene (0x04) and DIY (0x0a)
    replies carry little-endian selectors; music replies (0x13) carry the mode ID,
    sensitivity, and selector settings for legacy modes.
    Unresolved assumptions: exact firmware-specific reply presence, unrecognised
    mode selectors, and all trailing bytes in status and segment replies.
    Trailing bytes remain opaque rather than validated as zeroes.
    """

    class AaDomain(IntEnum):
        power = 1
        brightness = 4
        colormode = 5
        fw_version = 6
        hw_version = 7
        multi_effect = 163
        segments = 165

    class ColorMode(IntEnum):
        scene = 4
        diy = 10
        music = 19
        static = 21
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H617cStatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H617cStatusReply.AaDomain, self._io.read_u1())
        _on = self.domain
        if _on == H617cStatusReply.AaDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.colormode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.ColormodeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.fw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.hw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.HwVersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.multi_effect:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.MultiEffectBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H617cStatusReply.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H617cStatusReply.AaDomain.segments:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = govee_segment_page.GoveeSegmentPage(15, 3, False, _io__raw_body)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H617cStatusReply.AaDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.colormode:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.fw_version:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.hw_version:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.multi_effect:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H617cStatusReply.AaDomain.segments:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H617cStatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H617cStatusReply.AaDomain.brightness:
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
        elif _on == H617cStatusReply.AaDomain.colormode:
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
        elif _on == H617cStatusReply.AaDomain.fw_version:
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
        elif _on == H617cStatusReply.AaDomain.hw_version:
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
        elif _on == H617cStatusReply.AaDomain.multi_effect:
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
        elif _on == H617cStatusReply.AaDomain.power:
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
        elif _on == H617cStatusReply.AaDomain.segments:
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
        if _on == H617cStatusReply.AaDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.colormode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.fw_version:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.hw_version:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.multi_effect:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H617cStatusReply.AaDomain.segments:
            pass
            if self.body.segment_count != 15:
                raise kaitaistruct.ConsistencyError(u"body", 15, self.body.segment_count)
            if self.body.group_size != 3:
                raise kaitaistruct.ConsistencyError(u"body", 3, self.body.group_size)
            if self.body.unused_must_be_zero != False:
                raise kaitaistruct.ConsistencyError(u"body", False, self.body.unused_must_be_zero)
        else:
            pass
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class BrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.brightness_pct = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.brightness_pct)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmDiy(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.CmDiy, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.CmDiy, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmMusic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.CmMusic, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(govee_common.GoveeCommon.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            if self.is_legacy:
                pass
                self.style = self._io.read_u1()

            if self.is_legacy:
                pass
                self.has_fixed_colour = self._io.read_u1()

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H617cStatusReply.CmMusic, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            if self.is_legacy:
                pass
                self._io.write_u1(self.style)

            if self.is_legacy:
                pass
                self._io.write_u1(self.has_fixed_colour)

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass

            self._dirty = False

        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy =  ((self.mode_id == govee_common.GoveeCommon.MusicMode.rhythm) or (self.mode_id == govee_common.GoveeCommon.MusicMode.spectrum) or (self.mode_id == govee_common.GoveeCommon.MusicMode.energetic) or (self.mode_id == govee_common.GoveeCommon.MusicMode.rolling)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy

    class CmScene(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.CmScene, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.CmScene, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmStatic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.CmStatic, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = self._io.read_u1()
            self.kelvin = self._io.read_u2be()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.CmStatic, self)._write__seq(io)
            self._io.write_u1(self.sub)
            self._io.write_u2be(self.kelvin)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColormodeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.ColormodeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H617cStatusReply.ColorMode, self._io.read_u1())
            _on = self.mode
            if _on == H617cStatusReply.ColorMode.diy:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H617cStatusReply.CmDiy(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H617cStatusReply.ColorMode.music:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H617cStatusReply.CmMusic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H617cStatusReply.ColorMode.scene:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H617cStatusReply.CmScene(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H617cStatusReply.ColorMode.static:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H617cStatusReply.CmStatic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            else:
                pass
                self.mode_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H617cStatusReply.ColorMode.diy:
                pass
                self.mode_body._fetch_instances()
            elif _on == H617cStatusReply.ColorMode.music:
                pass
                self.mode_body._fetch_instances()
            elif _on == H617cStatusReply.ColorMode.scene:
                pass
                self.mode_body._fetch_instances()
            elif _on == H617cStatusReply.ColorMode.static:
                pass
                self.mode_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.ColormodeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H617cStatusReply.ColorMode.diy:
                pass
                _io__raw_mode_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_mode_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_mode_body=_io__raw_mode_body):
                    self._raw_mode_body = _io__raw_mode_body.to_byte_array()
                    if len(self._raw_mode_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(mode_body)", 16, len(self._raw_mode_body))
                    parent.write_bytes(self._raw_mode_body)
                _io__raw_mode_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.mode_body._write__seq(_io__raw_mode_body)
            elif _on == H617cStatusReply.ColorMode.music:
                pass
                _io__raw_mode_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_mode_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_mode_body=_io__raw_mode_body):
                    self._raw_mode_body = _io__raw_mode_body.to_byte_array()
                    if len(self._raw_mode_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(mode_body)", 16, len(self._raw_mode_body))
                    parent.write_bytes(self._raw_mode_body)
                _io__raw_mode_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.mode_body._write__seq(_io__raw_mode_body)
            elif _on == H617cStatusReply.ColorMode.scene:
                pass
                _io__raw_mode_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_mode_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_mode_body=_io__raw_mode_body):
                    self._raw_mode_body = _io__raw_mode_body.to_byte_array()
                    if len(self._raw_mode_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(mode_body)", 16, len(self._raw_mode_body))
                    parent.write_bytes(self._raw_mode_body)
                _io__raw_mode_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.mode_body._write__seq(_io__raw_mode_body)
            elif _on == H617cStatusReply.ColorMode.static:
                pass
                _io__raw_mode_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_mode_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_mode_body=_io__raw_mode_body):
                    self._raw_mode_body = _io__raw_mode_body.to_byte_array()
                    if len(self._raw_mode_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(mode_body)", 16, len(self._raw_mode_body))
                    parent.write_bytes(self._raw_mode_body)
                _io__raw_mode_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.mode_body._write__seq(_io__raw_mode_body)
            else:
                pass
                self._io.write_bytes(self.mode_body)


        def _check(self):
            _on = self.mode
            if _on == H617cStatusReply.ColorMode.diy:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H617cStatusReply.ColorMode.music:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H617cStatusReply.ColorMode.scene:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H617cStatusReply.ColorMode.static:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            else:
                pass
                if len(self.mode_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"mode_body", 16, len(self.mode_body))
            self._dirty = False


    class HwVersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.HwVersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.prefix = self._io.read_bytes(1)
            if not self.prefix == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.prefix, self._io, u"/types/hw_version_body/seq/0")
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.HwVersionBody, self)._write__seq(io)
            self._io.write_bytes(self.prefix)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.prefix) != 1:
                raise kaitaistruct.ConsistencyError(u"prefix", 1, len(self.prefix))
            if not self.prefix == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.prefix, None, u"/types/hw_version_body/seq/0")
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class MultiEffectBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.MultiEffectBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.flag = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.MultiEffectBody, self)._write__seq(io)
            self._io.write_u1(self.flag)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class VersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617cStatusReply.VersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617cStatusReply.VersionBody, self)._write__seq(io)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False



