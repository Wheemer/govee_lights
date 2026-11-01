# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_segment_page
from custom_components.govee_unified.generated_protocol import govee_shared
from custom_components.govee_unified.generated_protocol import h6102_status_reply
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6125StatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H6125, issue #117.
    Evidence source class: reachable Android 7.6.01 status-parsing behaviour; no
    official-app BLE capture of an identified H6125 is available.
    Compatibility hypothesis: the extended pact-1 route replies with the
    shared power, identity, static, scene, DIY and fifteen-segment layouts, plus a
    brightness register, the submode 0x11 music layout and the gradual register.
    In Android 7.6.01, mode replies carry a gradual flag and big-endian Kelvin for
    static colour (0x15), little-endian codes for scenes (0x04) and DIY (0x0a),
    and effect, sensitivity, and per-effect settings for music (0x11); segment
    pages carry three brightness/RGB records per group, and brightness replies
    return the raw register byte unchanged.
    Unresolved assumptions: register range for each hardware revision, whether the
    device ever answers with the legacy 0x0b static or 0x0c music modes, unused
    bytes of every reply, and whether segment pages contain meaningful records
    beyond fifteen.  Unknown mode selectors and every unused byte stay opaque.
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
        music = 17
        static = 21

    class MusicMode(IntEnum):
        energetic = 16
        rhythm = 17
        spectrum = 18
        rolling = 19
        bloom = 48
        shiny = 49
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6125StatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6125StatusReply.AaDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6125StatusReply.AaDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125StatusReply.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.colormode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125StatusReply.ColormodeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.fw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125StatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.hw_version:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125StatusReply.HwVersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.multi_effect:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = h6102_status_reply.H6102StatusReply.MultiEffectBody(_io__raw_body)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125StatusReply.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125StatusReply.AaDomain.segments:
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
        if _on == H6125StatusReply.AaDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.colormode:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.fw_version:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.hw_version:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.multi_effect:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6125StatusReply.AaDomain.segments:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6125StatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6125StatusReply.AaDomain.brightness:
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
        elif _on == H6125StatusReply.AaDomain.colormode:
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
        elif _on == H6125StatusReply.AaDomain.fw_version:
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
        elif _on == H6125StatusReply.AaDomain.hw_version:
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
        elif _on == H6125StatusReply.AaDomain.multi_effect:
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
        elif _on == H6125StatusReply.AaDomain.power:
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
        elif _on == H6125StatusReply.AaDomain.segments:
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
        if _on == H6125StatusReply.AaDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125StatusReply.AaDomain.colormode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125StatusReply.AaDomain.fw_version:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125StatusReply.AaDomain.hw_version:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125StatusReply.AaDomain.multi_effect:
            pass
        elif _on == H6125StatusReply.AaDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125StatusReply.AaDomain.segments:
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
            super(H6125StatusReply.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.register = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.register)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmDiy(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.CmDiy, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.CmDiy, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmMusic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.CmMusic, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H6125StatusReply.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            _on = self.mode_id
            if _on == H6125StatusReply.MusicMode.rhythm:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125StatusReply.RhythmSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6125StatusReply.MusicMode.rolling:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125StatusReply.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6125StatusReply.MusicMode.spectrum:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125StatusReply.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            else:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125StatusReply.OpaqueSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode_id
            if _on == H6125StatusReply.MusicMode.rhythm:
                pass
                self.settings._fetch_instances()
            elif _on == H6125StatusReply.MusicMode.rolling:
                pass
                self.settings._fetch_instances()
            elif _on == H6125StatusReply.MusicMode.spectrum:
                pass
                self.settings._fetch_instances()
            else:
                pass
                self.settings._fetch_instances()


        def _write__seq(self, io=None):
            super(H6125StatusReply.CmMusic, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            _on = self.mode_id
            if _on == H6125StatusReply.MusicMode.rhythm:
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
            elif _on == H6125StatusReply.MusicMode.rolling:
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
            elif _on == H6125StatusReply.MusicMode.spectrum:
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
            if _on == H6125StatusReply.MusicMode.rhythm:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6125StatusReply.MusicMode.rolling:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6125StatusReply.MusicMode.spectrum:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            else:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            self._dirty = False

        @property
        def has_fixed_colour(self):
            if hasattr(self, '_m_has_fixed_colour'):
                return self._m_has_fixed_colour

            self._m_has_fixed_colour = (self.settings.has_fixed_colour if self.mode_id == H6125StatusReply.MusicMode.rhythm else (self.settings.has_fixed_colour if  ((self.mode_id == H6125StatusReply.MusicMode.spectrum) or (self.mode_id == H6125StatusReply.MusicMode.rolling))  else 0))
            return getattr(self, '_m_has_fixed_colour', None)

        def _invalidate_has_fixed_colour(self):
            del self._m_has_fixed_colour
        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy =  ((self.mode_id == H6125StatusReply.MusicMode.energetic) or (self.mode_id == H6125StatusReply.MusicMode.rhythm) or (self.mode_id == H6125StatusReply.MusicMode.spectrum) or (self.mode_id == H6125StatusReply.MusicMode.rolling)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy
        @property
        def rgb(self):
            if hasattr(self, '_m_rgb'):
                return self._m_rgb

            self._m_rgb = (self.settings.rgb if self.mode_id == H6125StatusReply.MusicMode.rhythm else self.settings.rgb)
            return getattr(self, '_m_rgb', None)

        def _invalidate_rgb(self):
            del self._m_rgb
        @property
        def style(self):
            if hasattr(self, '_m_style'):
                return self._m_style

            self._m_style = (self.settings.style if self.mode_id == H6125StatusReply.MusicMode.rhythm else 0)
            return getattr(self, '_m_style', None)

        def _invalidate_style(self):
            del self._m_style

    class CmScene(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.CmScene, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.CmScene, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class CmStatic(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.CmStatic, self).__init__(_io)
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
            super(H6125StatusReply.CmStatic, self)._write__seq(io)
            self._io.write_u1(self.sub)
            self._io.write_u2be(self.kelvin)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColormodeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.ColormodeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6125StatusReply.ColorMode, self._io.read_u1())
            _on = self.mode
            if _on == H6125StatusReply.ColorMode.diy:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125StatusReply.CmDiy(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H6125StatusReply.ColorMode.music:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125StatusReply.CmMusic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H6125StatusReply.ColorMode.scene:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125StatusReply.CmScene(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            elif _on == H6125StatusReply.ColorMode.static:
                pass
                self._raw_mode_body = self._io.read_bytes(16)
                _io__raw_mode_body = KaitaiStream(BytesIO(self._raw_mode_body))
                self.mode_body = H6125StatusReply.CmStatic(_io__raw_mode_body, self, self._root)
                self.mode_body._read()
            else:
                pass
                self.mode_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H6125StatusReply.ColorMode.diy:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125StatusReply.ColorMode.music:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125StatusReply.ColorMode.scene:
                pass
                self.mode_body._fetch_instances()
            elif _on == H6125StatusReply.ColorMode.static:
                pass
                self.mode_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.ColormodeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H6125StatusReply.ColorMode.diy:
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
            elif _on == H6125StatusReply.ColorMode.music:
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
            elif _on == H6125StatusReply.ColorMode.scene:
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
            elif _on == H6125StatusReply.ColorMode.static:
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
            if _on == H6125StatusReply.ColorMode.diy:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H6125StatusReply.ColorMode.music:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H6125StatusReply.ColorMode.scene:
                pass
                if self.mode_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self._root, self.mode_body._root)
                if self.mode_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"mode_body", self, self.mode_body._parent)
            elif _on == H6125StatusReply.ColorMode.static:
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


    class ColourSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.ColourSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.has_fixed_colour = self._io.read_u1()
            if self.has_fixed_colour != 0:
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.has_fixed_colour != 0:
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H6125StatusReply.ColourSettings, self)._write__seq(io)
            self._io.write_u1(self.has_fixed_colour)
            if self.has_fixed_colour != 0:
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.has_fixed_colour != 0:
                pass

            self._dirty = False


    class HwVersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.HwVersionBody, self).__init__(_io)
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
            super(H6125StatusReply.HwVersionBody, self)._write__seq(io)
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


    class OpaqueSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.OpaqueSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.OpaqueSettings, self)._write__seq(io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class RhythmSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.RhythmSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.style = self._io.read_u1()
            self.has_fixed_colour = self._io.read_u1()
            if self.has_fixed_colour != 0:
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.has_fixed_colour != 0:
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H6125StatusReply.RhythmSettings, self)._write__seq(io)
            self._io.write_u1(self.style)
            self._io.write_u1(self.has_fixed_colour)
            if self.has_fixed_colour != 0:
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.has_fixed_colour != 0:
                pass

            self._dirty = False


    class VersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125StatusReply.VersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125StatusReply.VersionBody, self)._write__seq(io)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False



