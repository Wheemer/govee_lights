# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_rgb_segment_page
from custom_components.govee_unified.generated_protocol import h6102_status_reply
from custom_components.govee_unified.generated_protocol import h6125_status_reply
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6125LegacyStatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H6125, issue #117.
    Compatibility hypothesis: legacy controllers use submode 0x0b colour and
    A2 RGB-only pages. The original H612526 route uses submode 0x0c music.
    Application consumers establish these layouts, not firmware acceptance.
    Unresolved assumptions: per-revision reply presence, unused bytes and
    legacy scene catalogue availability. Colour mode does not report RGB.
    """

    class AaDomain(IntEnum):
        power = 1
        brightness = 4
        colormode = 5
        fw_version = 6
        hw_version = 7
        segments = 162
        multi_effect = 163

    class ColorMode(IntEnum):
        scene = 4
        diy = 10
        static = 11
        music = 12

    class MusicMode(IntEnum):
        energetic = 0
        rolling = 2
        spectrum = 3
        rhythm = 4

    class SceneMode(IntEnum):
        film = 4
        date = 5
        romantic = 7
        blinking = 8
        candle = 9
        breathe = 10
        snow = 15
        energetic = 16
        chase = 21
        stream = 22
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6125LegacyStatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6125LegacyStatusReply.AaDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6125LegacyStatusReply.AaDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6125_status_reply.H6125StatusReply.BrightnessBody(_io__raw_body)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.colormode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125LegacyStatusReply.ColormodeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.fw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6125_status_reply.H6125StatusReply.VersionBody(_io__raw_body)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.hw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6125_status_reply.H6125StatusReply.HwVersionBody(_io__raw_body)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.multi_effect:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6102_status_reply.H6102StatusReply.MultiEffectBody(_io__raw_body)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6125_status_reply.H6125StatusReply.PowerBody(_io__raw_body)
            self.body._read()
        elif _on == H6125LegacyStatusReply.AaDomain.segments:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = govee_rgb_segment_page.GoveeRgbSegmentPage(15, 4, _io__raw_body)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6125LegacyStatusReply.AaDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.colormode:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.fw_version:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.hw_version:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.multi_effect:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6125LegacyStatusReply.AaDomain.segments:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6125LegacyStatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6125LegacyStatusReply.AaDomain.brightness:
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
        elif _on == H6125LegacyStatusReply.AaDomain.colormode:
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
        elif _on == H6125LegacyStatusReply.AaDomain.fw_version:
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
        elif _on == H6125LegacyStatusReply.AaDomain.hw_version:
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
        elif _on == H6125LegacyStatusReply.AaDomain.multi_effect:
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
        elif _on == H6125LegacyStatusReply.AaDomain.power:
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
        elif _on == H6125LegacyStatusReply.AaDomain.segments:
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
        if _on == H6125LegacyStatusReply.AaDomain.brightness:
            pass
        elif _on == H6125LegacyStatusReply.AaDomain.colormode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125LegacyStatusReply.AaDomain.fw_version:
            pass
        elif _on == H6125LegacyStatusReply.AaDomain.hw_version:
            pass
        elif _on == H6125LegacyStatusReply.AaDomain.multi_effect:
            pass
        elif _on == H6125LegacyStatusReply.AaDomain.power:
            pass
        elif _on == H6125LegacyStatusReply.AaDomain.segments:
            pass
            if self.body.segment_count != 15:
                raise kaitaistruct.ConsistencyError(u"body", 15, self.body.segment_count)
            if self.body.group_size != 4:
                raise kaitaistruct.ConsistencyError(u"body", 4, self.body.group_size)
        else:
            pass
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class CmMusic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125LegacyStatusReply.CmMusic, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H6125LegacyStatusReply.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            _on = self.mode_id
            if _on == H6125LegacyStatusReply.MusicMode.energetic:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = h6125_status_reply.H6125StatusReply.OpaqueSettings(_io__raw_settings)
                self.settings._read()
            else:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = h6125_status_reply.H6125StatusReply.ColourSettings(_io__raw_settings)
                self.settings._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode_id
            if _on == H6125LegacyStatusReply.MusicMode.energetic:
                pass
                self.settings._fetch_instances()
            else:
                pass
                self.settings._fetch_instances()


        def _write__seq(self, io=None):
            super(H6125LegacyStatusReply.CmMusic, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            _on = self.mode_id
            if _on == H6125LegacyStatusReply.MusicMode.energetic:
                pass
                _io__raw_settings = KaitaiStream(BytesIO(bytearray(14)))
                self._io.add_child_stream(_io__raw_settings)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (14))
                def handler(parent, _io__raw_settings=_io__raw_settings):
                    self._raw_settings = _io__raw_settings.to_byte_array()
                    if len(self._raw_settings) != 14:
                        raise kaitaistruct.ConsistencyError(u"raw(settings)", 14, len(self._raw_settings))
                    parent.write_bytes(self._raw_settings)
                _io__raw_settings.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.settings._write__seq(_io__raw_settings)
            else:
                pass
                _io__raw_settings = KaitaiStream(BytesIO(bytearray(14)))
                self._io.add_child_stream(_io__raw_settings)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (14))
                def handler(parent, _io__raw_settings=_io__raw_settings):
                    self._raw_settings = _io__raw_settings.to_byte_array()
                    if len(self._raw_settings) != 14:
                        raise kaitaistruct.ConsistencyError(u"raw(settings)", 14, len(self._raw_settings))
                    parent.write_bytes(self._raw_settings)
                _io__raw_settings.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.settings._write__seq(_io__raw_settings)


        def _check(self):
            _on = self.mode_id
            if _on == H6125LegacyStatusReply.MusicMode.energetic:
                pass
            else:
                pass
            self._dirty = False

        @property
        def has_fixed_colour(self):
            if hasattr(self, '_m_has_fixed_colour'):
                return self._m_has_fixed_colour

            self._m_has_fixed_colour = (0 if self.mode_id == H6125LegacyStatusReply.MusicMode.energetic else self.settings.has_fixed_colour)
            return getattr(self, '_m_has_fixed_colour', None)

        def _invalidate_has_fixed_colour(self):
            del self._m_has_fixed_colour
        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy = True
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy
        @property
        def rgb(self):
            if hasattr(self, '_m_rgb'):
                return self._m_rgb

            self._m_rgb = self.settings.rgb
            return getattr(self, '_m_rgb', None)

        def _invalidate_rgb(self):
            del self._m_rgb
        @property
        def style(self):
            if hasattr(self, '_m_style'):
                return self._m_style

            self._m_style = 0
            return getattr(self, '_m_style', None)

        def _invalidate_style(self):
            del self._m_style

    class CmScene(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125LegacyStatusReply.CmScene, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = KaitaiStream.resolve_enum(H6125LegacyStatusReply.SceneMode, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125LegacyStatusReply.CmScene, self)._write__seq(io)
            self._io.write_u1(int(self.scene_id))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmStatic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125LegacyStatusReply.CmStatic, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125LegacyStatusReply.CmStatic, self)._write__seq(io)
            self._io.write_u1(self.sub)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColormodeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125LegacyStatusReply.ColormodeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6125LegacyStatusReply.ColorMode, self._io.read_u1())
            _on = self.mode
            if _on == H6125LegacyStatusReply.ColorMode.diy:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = h6125_status_reply.H6125StatusReply.CmDiy(_io__raw_mode_body)
                self.mode_body._read()
            elif _on == H6125LegacyStatusReply.ColorMode.music:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125LegacyStatusReply.CmMusic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H6125LegacyStatusReply.ColorMode.scene:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125LegacyStatusReply.CmScene(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H6125LegacyStatusReply.ColorMode.static:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125LegacyStatusReply.CmStatic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            else:
                pass
                self.mode_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H6125LegacyStatusReply.ColorMode.diy:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125LegacyStatusReply.ColorMode.music:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125LegacyStatusReply.ColorMode.scene:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125LegacyStatusReply.ColorMode.static:
                pass
                self.mode_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6125LegacyStatusReply.ColormodeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H6125LegacyStatusReply.ColorMode.diy:
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
            elif _on == H6125LegacyStatusReply.ColorMode.music:
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
            elif _on == H6125LegacyStatusReply.ColorMode.scene:
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
            elif _on == H6125LegacyStatusReply.ColorMode.static:
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
            if _on == H6125LegacyStatusReply.ColorMode.diy:
                pass
            elif _on == H6125LegacyStatusReply.ColorMode.music:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H6125LegacyStatusReply.ColorMode.scene:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H6125LegacyStatusReply.ColorMode.static:
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



