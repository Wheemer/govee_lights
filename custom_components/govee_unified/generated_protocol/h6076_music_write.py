# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6076MusicWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6076, issue #343.
    Evidence source classes: a reporter's decrypted Android HCI snoop of the Govee
    app driving an H6076 (hardware 3.05.00, software 1.04.05, V1 encrypted
    session) and Android Govee 7.5.30 floor-lamp music selector and capability-gate
    behaviour.  The capture is
    reporter-supplied and its raw file has not been reviewed, and no integration or
    owner BLE test of an H6076 exists yet.
    Compatibility hypothesis: the H6076 writes its music selector at submode 0x0f,
    not the H617A submode 0x13.  The twelve-effect screen applies to software
    1.02.00 or newer on pact 1/1 or 2/1; older software uses a legacy screen that
    reuses the same submode with fewer effects.  The six legacy effects carry their
    parameters in the selector.  Rhythm has a leading dynamic byte.  The
    companion-backed effects carry only the sensitivity and take their palette from
    the preceding A3 body described by h6076_music_body.ksy.
    Unresolved assumptions: the value of the unused bytes after the written fields
    (the capture lists frames before padding), whether a fixed-colour flag other
    than one is accepted, whether the device echoes the selector, and the behaviour
    of firmware older than 1.02.00.  The final byte is the XOR of bytes 0 through 18.
    """

    class MusicMode(IntEnum):
        energetic = 0
        hopping = 2
        rhythm = 4
        beat = 6
        spray = 7
        bounce = 8
        separation = 50
        skittles = 77
        candy_crush = 78
        fusion = 79
        torch = 80
        shiny = 81
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6076MusicWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = self._io.read_bytes(1)
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, self._io, u"/seq/1")
        self.sub = self._io.read_bytes(1)
        if not self.sub == b"\x0F":
            raise kaitaistruct.ValidationNotEqualError(b"\x0F", self.sub, self._io, u"/seq/2")
        self._raw_selector = self._io.read_bytes(16)
        _io__raw_selector = KaitaiStream(BytesIO(self._raw_selector))
        self.selector = H6076MusicWrite.MusicSelector(_io__raw_selector, self, self._root)
        self.selector._read()
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.selector._fetch_instances()


    def _write__seq(self, io=None):
        super(H6076MusicWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_bytes(self.opcode)
        self._io.write_bytes(self.sub)
        _io__raw_selector = KaitaiStream(BytesIO(bytearray(16)))
        self._io.add_child_stream(_io__raw_selector)
        _pos2 = self._io.pos()
        self._io.seek(self._io.pos() + (16))
        def handler(parent, _io__raw_selector=_io__raw_selector):
            self._raw_selector = _io__raw_selector.to_byte_array()
            if len(self._raw_selector) != 16:
                raise kaitaistruct.ConsistencyError(u"raw(selector)", 16, len(self._raw_selector))
            parent.write_bytes(self._raw_selector)
        _io__raw_selector.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
        self.selector._write__seq(_io__raw_selector)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        if len(self.opcode) != 1:
            raise kaitaistruct.ConsistencyError(u"opcode", 1, len(self.opcode))
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, None, u"/seq/1")
        if len(self.sub) != 1:
            raise kaitaistruct.ConsistencyError(u"sub", 1, len(self.sub))
        if not self.sub == b"\x0F":
            raise kaitaistruct.ValidationNotEqualError(b"\x0F", self.sub, None, u"/seq/2")
        if self.selector._root != self._root:
            raise kaitaistruct.ConsistencyError(u"selector", self._root, self.selector._root)
        if self.selector._parent != self:
            raise kaitaistruct.ConsistencyError(u"selector", self, self.selector._parent)
        self._dirty = False

    class ColourSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6076MusicWrite.ColourSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.has_fixed_colour = self._io.read_u1()
            if self.has_fixed_colour != 0:
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.has_fixed_colour != 0:
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H6076MusicWrite.ColourSettings, self)._write__seq(io)
            self._io.write_u1(self.has_fixed_colour)
            if self.has_fixed_colour != 0:
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.has_fixed_colour != 0:
                pass

            self._dirty = False


    class MusicSelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6076MusicWrite.MusicSelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H6076MusicWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            _on = self.mode_id
            if _on == H6076MusicWrite.MusicMode.beat:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6076MusicWrite.MusicMode.bounce:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6076MusicWrite.MusicMode.energetic:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6076MusicWrite.MusicMode.hopping:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6076MusicWrite.MusicMode.rhythm:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.RhythmSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6076MusicWrite.MusicMode.spray:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            else:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6076MusicWrite.OpaqueSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode_id
            if _on == H6076MusicWrite.MusicMode.beat:
                pass
                self.settings._fetch_instances()
            elif _on == H6076MusicWrite.MusicMode.bounce:
                pass
                self.settings._fetch_instances()
            elif _on == H6076MusicWrite.MusicMode.energetic:
                pass
                self.settings._fetch_instances()
            elif _on == H6076MusicWrite.MusicMode.hopping:
                pass
                self.settings._fetch_instances()
            elif _on == H6076MusicWrite.MusicMode.rhythm:
                pass
                self.settings._fetch_instances()
            elif _on == H6076MusicWrite.MusicMode.spray:
                pass
                self.settings._fetch_instances()
            else:
                pass
                self.settings._fetch_instances()


        def _write__seq(self, io=None):
            super(H6076MusicWrite.MusicSelector, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            _on = self.mode_id
            if _on == H6076MusicWrite.MusicMode.beat:
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
            elif _on == H6076MusicWrite.MusicMode.bounce:
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
            elif _on == H6076MusicWrite.MusicMode.energetic:
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
            elif _on == H6076MusicWrite.MusicMode.hopping:
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
            elif _on == H6076MusicWrite.MusicMode.rhythm:
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
            elif _on == H6076MusicWrite.MusicMode.spray:
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
            if _on == H6076MusicWrite.MusicMode.beat:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6076MusicWrite.MusicMode.bounce:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6076MusicWrite.MusicMode.energetic:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6076MusicWrite.MusicMode.hopping:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6076MusicWrite.MusicMode.rhythm:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6076MusicWrite.MusicMode.spray:
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

            self._m_has_fixed_colour = (self.settings.has_fixed_colour if self.mode_id == H6076MusicWrite.MusicMode.rhythm else (self.settings.has_fixed_colour if self.is_legacy else 0))
            return getattr(self, '_m_has_fixed_colour', None)

        def _invalidate_has_fixed_colour(self):
            del self._m_has_fixed_colour
        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy =  ((self.mode_id == H6076MusicWrite.MusicMode.rhythm) or (self.mode_id == H6076MusicWrite.MusicMode.energetic) or (self.mode_id == H6076MusicWrite.MusicMode.hopping) or (self.mode_id == H6076MusicWrite.MusicMode.beat) or (self.mode_id == H6076MusicWrite.MusicMode.spray) or (self.mode_id == H6076MusicWrite.MusicMode.bounce)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy
        @property
        def rgb(self):
            if hasattr(self, '_m_rgb'):
                return self._m_rgb

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self._m_rgb = (self.settings.rgb if self.mode_id == H6076MusicWrite.MusicMode.rhythm else self.settings.rgb)

            return getattr(self, '_m_rgb', None)

        def _invalidate_rgb(self):
            del self._m_rgb
        @property
        def style(self):
            if hasattr(self, '_m_style'):
                return self._m_style

            self._m_style = ((1 if self.settings.dynamic == 0 else 0) if self.mode_id == H6076MusicWrite.MusicMode.rhythm else 0)
            return getattr(self, '_m_style', None)

        def _invalidate_style(self):
            del self._m_style

    class OpaqueSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6076MusicWrite.OpaqueSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6076MusicWrite.OpaqueSettings, self)._write__seq(io)
            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class RhythmSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6076MusicWrite.RhythmSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.dynamic = self._io.read_u1()
            self.has_fixed_colour = self._io.read_u1()
            if self.has_fixed_colour != 0:
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.has_fixed_colour != 0:
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H6076MusicWrite.RhythmSettings, self)._write__seq(io)
            self._io.write_u1(self.dynamic)
            self._io.write_u1(self.has_fixed_colour)
            if self.has_fixed_colour != 0:
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.has_fixed_colour != 0:
                pass

            self._dirty = False



