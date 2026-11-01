# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6125WireWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6125, issue #117.
    Evidence source class: application producers and public legacy observations.
    Compatibility hypothesis: pact 1 uses a scaled brightness register and the
    0x11 music selector. Older controllers use 0x0b RGB with a segment mask;
    the original H612526 music selector is 0x0c with a separate mode codebook.
    The adapter re-encodes shared logical commands through these named fields.
    Revision eligibility belongs to the product profile, not this wire grammar.
    Unresolved assumptions: conflicting minimum-register evidence on some Telink
    paths, firmware-specific acceptance, unused bytes and command echoes.
    The final byte is the XOR of bytes 0 through 18.
    """

    class CommandOp(IntEnum):
        brightness = 4
        mode = 5

    class LegacyMusicMode(IntEnum):
        energetic = 0
        rolling = 2
        spectrum = 3
        rhythm = 4

    class ModeSub(IntEnum):
        legacy_colour = 11
        legacy_music = 12
        music = 17

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
        super(H6125WireWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6125WireWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H6125WireWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125WireWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6125WireWrite.CommandOp.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6125WireWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6125WireWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6125WireWrite.CommandOp.mode:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6125WireWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6125WireWrite.CommandOp.brightness:
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
        elif _on == H6125WireWrite.CommandOp.mode:
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
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        _on = self.opcode
        if _on == H6125WireWrite.CommandOp.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6125WireWrite.CommandOp.mode:
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
            super(H6125WireWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.register = self._io.read_u1()
            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125WireWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.register)
            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColourSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.ColourSettings, self).__init__(_io)
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
            super(H6125WireWrite.ColourSettings, self)._write__seq(io)
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


    class LegacyColour(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.LegacyColour, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.segment_mask = self._io.read_u2le()
            self.padding = self._io.read_bytes(11)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H6125WireWrite.LegacyColour, self)._write__seq(io)
            self.rgb._write__seq(self._io)
            self._io.write_u2le(self.segment_mask)
            self._io.write_bytes(self.padding)


        def _check(self):
            if len(self.padding) != 11:
                raise kaitaistruct.ConsistencyError(u"padding", 11, len(self.padding))
            self._dirty = False


    class LegacyMusicSelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.LegacyMusicSelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H6125WireWrite.LegacyMusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            _on = self.mode_id
            if _on == H6125WireWrite.LegacyMusicMode.energetic:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.OpaqueSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            else:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode_id
            if _on == H6125WireWrite.LegacyMusicMode.energetic:
                pass
                self.settings._fetch_instances()
            else:
                pass
                self.settings._fetch_instances()


        def _write__seq(self, io=None):
            super(H6125WireWrite.LegacyMusicSelector, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            _on = self.mode_id
            if _on == H6125WireWrite.LegacyMusicMode.energetic:
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
            if _on == H6125WireWrite.LegacyMusicMode.energetic:
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


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = KaitaiStream.resolve_enum(H6125WireWrite.ModeSub, self._io.read_u1())
            _on = self.sub
            if _on == H6125WireWrite.ModeSub.legacy_colour:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H6125WireWrite.LegacyColour(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            elif _on == H6125WireWrite.ModeSub.legacy_music:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H6125WireWrite.LegacyMusicSelector(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            elif _on == H6125WireWrite.ModeSub.music:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H6125WireWrite.MusicSelector(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            else:
                pass
                self.sub_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub
            if _on == H6125WireWrite.ModeSub.legacy_colour:
                pass
                self.sub_body._fetch_instances()
            elif _on == H6125WireWrite.ModeSub.legacy_music:
                pass
                self.sub_body._fetch_instances()
            elif _on == H6125WireWrite.ModeSub.music:
                pass
                self.sub_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6125WireWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.sub))
            _on = self.sub
            if _on == H6125WireWrite.ModeSub.legacy_colour:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            elif _on == H6125WireWrite.ModeSub.legacy_music:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            elif _on == H6125WireWrite.ModeSub.music:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            else:
                pass
                self._io.write_bytes(self.sub_body)


        def _check(self):
            _on = self.sub
            if _on == H6125WireWrite.ModeSub.legacy_colour:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            elif _on == H6125WireWrite.ModeSub.legacy_music:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            elif _on == H6125WireWrite.ModeSub.music:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            else:
                pass
                if len(self.sub_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"sub_body", 16, len(self.sub_body))
            self._dirty = False


    class MusicSelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.MusicSelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H6125WireWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            _on = self.mode_id
            if _on == H6125WireWrite.MusicMode.rhythm:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.RhythmSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6125WireWrite.MusicMode.rolling:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            elif _on == H6125WireWrite.MusicMode.spectrum:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.ColourSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            else:
                pass
                self._raw_settings = self._io.read_bytes(14)
                _io__raw_settings = KaitaiStream(BytesIO(self._raw_settings))
                self.settings = H6125WireWrite.OpaqueSettings(_io__raw_settings, self, self._root)
                self.settings._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode_id
            if _on == H6125WireWrite.MusicMode.rhythm:
                pass
                self.settings._fetch_instances()
            elif _on == H6125WireWrite.MusicMode.rolling:
                pass
                self.settings._fetch_instances()
            elif _on == H6125WireWrite.MusicMode.spectrum:
                pass
                self.settings._fetch_instances()
            else:
                pass
                self.settings._fetch_instances()


        def _write__seq(self, io=None):
            super(H6125WireWrite.MusicSelector, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            _on = self.mode_id
            if _on == H6125WireWrite.MusicMode.rhythm:
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
            elif _on == H6125WireWrite.MusicMode.rolling:
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
            elif _on == H6125WireWrite.MusicMode.spectrum:
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
            if _on == H6125WireWrite.MusicMode.rhythm:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6125WireWrite.MusicMode.rolling:
                pass
                if self.settings._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"settings", self._root, self.settings._root)
                if self.settings._parent != self:
                    raise kaitaistruct.ConsistencyError(u"settings", self, self.settings._parent)
            elif _on == H6125WireWrite.MusicMode.spectrum:
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


    class OpaqueSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.OpaqueSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6125WireWrite.OpaqueSettings, self)._write__seq(io)
            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class RhythmSettings(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6125WireWrite.RhythmSettings, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.style = self._io.read_u1()
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
            super(H6125WireWrite.RhythmSettings, self)._write__seq(io)
            self._io.write_u1(self.style)
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



