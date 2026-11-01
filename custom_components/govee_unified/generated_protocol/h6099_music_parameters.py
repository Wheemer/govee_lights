# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099MusicParameters(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 issue #258.  Android 7.6.01 H6099 music control uploads A3
    command 41 (mode followed by this palette and tail) before sending the mode
    selector.  Default companions carry seven RGB colours, and the mode
    configuration admits 1-8 colours.  Shared music parameter builders define the
    mode-specific tail fields below.  Physical IC count, not fourteen logical
    zones, controls dependent geometry.  Day/Night's app UI parameter indices
    disagree with its payload builder (no segment count is applied, index 0 sets
    speed, and index 1 sets fade), so those UI parameters remain unqualified.
    Energetic's companion upload path differs from the legacy selector path and
    remains unresolved.  No official-app capture or owner qualification yet.
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
        super(H6099MusicParameters, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.mode = KaitaiStream.resolve_enum(H6099MusicParameters.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == H6099MusicParameters.MusicMode.bloom:
            pass
            self.tail = H6099MusicParameters.BloomTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.day_and_night:
            pass
            self.tail = H6099MusicParameters.DaynightTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.fountain:
            pass
            self.tail = H6099MusicParameters.FountainTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.hopping:
            pass
            self.tail = H6099MusicParameters.HoppingTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.piano_keys:
            pass
            self.tail = H6099MusicParameters.PianoTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.separation:
            pass
            self.tail = H6099MusicParameters.SeparationTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H6099MusicParameters.MusicMode.shiny:
            pass
            self.tail = H6099MusicParameters.ShinyTail(self._io, self, self._root)
            self.tail._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == H6099MusicParameters.MusicMode.bloom:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.day_and_night:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.fountain:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.hopping:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.piano_keys:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        elif _on == H6099MusicParameters.MusicMode.shiny:
            pass
            self.tail._fetch_instances()


    def _write__seq(self, io=None):
        super(H6099MusicParameters, self)._write__seq(io)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == H6099MusicParameters.MusicMode.bloom:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.day_and_night:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.fountain:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.hopping:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.piano_keys:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.separation:
            pass
            self.tail._write__seq(self._io)
        elif _on == H6099MusicParameters.MusicMode.shiny:
            pass
            self.tail._write__seq(self._io)


    def _check(self):
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == H6099MusicParameters.MusicMode.bloom:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.day_and_night:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.fountain:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.hopping:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.piano_keys:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.separation:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H6099MusicParameters.MusicMode.shiny:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        self._dirty = False

    class BloomTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.BloomTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.no_rhythm_speed = self._io.read_u1()
            self.rhythm_speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.BloomTail, self)._write__seq(io)
            self._io.write_u1(self.no_rhythm_speed)
            self._io.write_u1(self.rhythm_speed)


        def _check(self):
            self._dirty = False


    class DaynightTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.DaynightTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.piece_count = self._io.read_u1()
            self.speed = self._io.read_u1()
            self.gradient = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.DaynightTail, self)._write__seq(io)
            self._io.write_u1(self.piece_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.gradient)


        def _check(self):
            self._dirty = False


    class FountainTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.FountainTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.start_point = self._io.read_u1()
            self.piece_length = self._io.read_u1()
            self.piece_count = self._io.read_u1()
            self.speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.FountainTail, self)._write__seq(io)
            self._io.write_u1(self.start_point)
            self._io.write_u1(self.piece_length)
            self._io.write_u1(self.piece_count)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False


    class HoppingTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.HoppingTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.background = govee_shared.GoveeShared.Rgb(self._io)
            self.background._read()
            self.rel_brightness = self._io.read_u1()
            self.speed = self._io.read_u1()
            self.piece_length_min = self._io.read_u1()
            self.piece_length_max = self._io.read_u1()
            self.piece_count_min = self._io.read_u1()
            self.piece_count_max = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.background._fetch_instances()


        def _write__seq(self, io=None):
            super(H6099MusicParameters.HoppingTail, self)._write__seq(io)
            self.background._write__seq(self._io)
            self._io.write_u1(self.rel_brightness)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.piece_length_min)
            self._io.write_u1(self.piece_length_max)
            self._io.write_u1(self.piece_count_min)
            self._io.write_u1(self.piece_count_max)


        def _check(self):
            self._dirty = False


    class PianoTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.PianoTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.gradient = self._io.read_u1()
            self.key_count = self._io.read_u1()
            self.speed = self._io.read_u1()
            self.off_minimum = self._io.read_u1()
            self.off_maximum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.PianoTail, self)._write__seq(io)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.key_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.off_minimum)
            self._io.write_u1(self.off_maximum)


        def _check(self):
            self._dirty = False


    class SeparationTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.SeparationTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.point = self._io.read_u1()
            self.gradient = self._io.read_u1()
            self.companion = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.SeparationTail, self)._write__seq(io)
            self._io.write_u1(self.point)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.companion)


        def _check(self):
            self._dirty = False


    class ShinyTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099MusicParameters.ShinyTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.minimum_brightness = self._io.read_u1()
            self.maximum_brightness = self._io.read_u1()
            self.speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099MusicParameters.ShinyTail, self)._write__seq(io)
            self._io.write_u1(self.minimum_brightness)
            self._io.write_u1(self.maximum_brightness)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False



