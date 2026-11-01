# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_shared
from custom_components.govee_unified.generated_protocol import h617a_control_payload
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MusicBody(ReadWriteKaitaiStruct):
    """Capture-backed H617A music envelope and presets.  Generalised app-derived tails remain in speculative/h617a_control_payload.ksy under issue #286 (Fountain #129); importing them does not promote their evidence class.  Palette-relative tails are read and written by the generated adapter.  A structurally valid alternative palette or tail does not qualify model-specific bounds, defaults, style, companion values, or physical IC geometry.  Issue 286 synthetic tests reuse this structure without claiming new device support.
    """

    class MusicMode(IntEnum):
        bloom = 48
        shiny = 49
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55
    def __init__(self, _io=None, _parent=None, _root=None):
        super(MusicBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = govee_common.GoveeCommon.A3Header(self._io)
        self.header._read()
        self.command = self._io.read_bytes(1)
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, self._io, u"/seq/1")
        self.mode = KaitaiStream.resolve_enum(MusicBody.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == MusicBody.MusicMode.bloom:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.BloomTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.day_and_night:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.DayAndNightTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.fountain:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.FountainTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.hopping:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.HoppingTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.piano_keys:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.PianoKeysTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.separation:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.SeparationTail(_io__raw_tail)
            self.tail._read()
        elif _on == MusicBody.MusicMode.shiny:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.ShinyTail(_io__raw_tail)
            self.tail._read()
        else:
            pass
            self.tail = self._io.read_bytes(self.tail_len)
        self.padding = []
        i = 0
        while not self._io.is_eof():
            self.padding.append(self._io.read_u1())
            if not self.padding[i] == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding[i], self._io, u"/seq/6")
            i += 1

        self._dirty = False


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == MusicBody.MusicMode.bloom:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.day_and_night:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.fountain:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.hopping:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.piano_keys:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        elif _on == MusicBody.MusicMode.shiny:
            pass
            self.tail._fetch_instances()
        else:
            pass
        for i in range(len(self.padding)):
            pass



    def _write__seq(self, io=None):
        super(MusicBody, self)._write__seq(io)
        self.header._write__seq(self._io)
        self._io.write_bytes(self.command)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == MusicBody.MusicMode.bloom:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.day_and_night:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.fountain:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.hopping:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.piano_keys:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.separation:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == MusicBody.MusicMode.shiny:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        else:
            pass
            self._io.write_bytes(self.tail)
        for i in range(len(self.padding)):
            pass
            if self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())
            self._io.write_u1(self.padding[i])

        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.command) != 1:
            raise kaitaistruct.ConsistencyError(u"command", 1, len(self.command))
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, None, u"/seq/1")
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == MusicBody.MusicMode.bloom:
            pass
        elif _on == MusicBody.MusicMode.day_and_night:
            pass
        elif _on == MusicBody.MusicMode.fountain:
            pass
        elif _on == MusicBody.MusicMode.hopping:
            pass
        elif _on == MusicBody.MusicMode.piano_keys:
            pass
        elif _on == MusicBody.MusicMode.separation:
            pass
        elif _on == MusicBody.MusicMode.shiny:
            pass
        else:
            pass
            if len(self.tail) != self.tail_len:
                raise kaitaistruct.ConsistencyError(u"tail", self.tail_len, len(self.tail))
        for i in range(len(self.padding)):
            pass
            if not self.padding[i] == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding[i], None, u"/seq/6")

        self._dirty = False

    class ModeSetFrame(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(MusicBody.ModeSetFrame, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = self._io.read_bytes(1)
            if not self.header == b"\x33":
                raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/types/mode_set_frame/seq/0")
            self.domain = self._io.read_bytes(1)
            if not self.domain == b"\x05":
                raise kaitaistruct.ValidationNotEqualError(b"\x05", self.domain, self._io, u"/types/mode_set_frame/seq/1")
            self.sub = self._io.read_bytes(1)
            if not self.sub == b"\x13":
                raise kaitaistruct.ValidationNotEqualError(b"\x13", self.sub, self._io, u"/types/mode_set_frame/seq/2")
            self._raw_selector = self._io.read_bytes(16)
            _io__raw_selector = KaitaiStream(BytesIO(self._raw_selector))
            self.selector = govee_common.GoveeCommon.MusicSelector(_io__raw_selector)
            self.selector._read()
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.selector._fetch_instances()


        def _write__seq(self, io=None):
            super(MusicBody.ModeSetFrame, self)._write__seq(io)
            self._io.write_bytes(self.header)
            self._io.write_bytes(self.domain)
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
                raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/types/mode_set_frame/seq/0")
            if len(self.domain) != 1:
                raise kaitaistruct.ConsistencyError(u"domain", 1, len(self.domain))
            if not self.domain == b"\x05":
                raise kaitaistruct.ValidationNotEqualError(b"\x05", self.domain, None, u"/types/mode_set_frame/seq/1")
            if len(self.sub) != 1:
                raise kaitaistruct.ConsistencyError(u"sub", 1, len(self.sub))
            if not self.sub == b"\x13":
                raise kaitaistruct.ValidationNotEqualError(b"\x13", self.sub, None, u"/types/mode_set_frame/seq/2")
            self._dirty = False


    @property
    def tail_len(self):
        if hasattr(self, '_m_tail_len'):
            return self._m_tail_len

        self._m_tail_len = (9 if self.mode == MusicBody.MusicMode.hopping else (5 if self.mode == MusicBody.MusicMode.piano_keys else (4 if self.mode == MusicBody.MusicMode.fountain else (3 if self.mode == MusicBody.MusicMode.separation else (3 if self.mode == MusicBody.MusicMode.shiny else (3 if self.mode == MusicBody.MusicMode.day_and_night else 2))))))
        return getattr(self, '_m_tail_len', None)

    def _invalidate_tail_len(self):
        del self._m_tail_len

