# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H61f5MusicParameters(ReadWriteKaitaiStruct):
    """SPECULATIVE H61F5 issue #392.  Android 7.6.01 MusicModeNewH61F6 (goodsType 261)
    uploads A3 command 41 (mode followed by this palette and tail) before sending
    the mode selector.  Physical IC count (50 on uncut H61F5, read via AA 40)
    controls dependent geometry.
    """

    class MusicMode(IntEnum):
        bloom = 48
        shiny = 49
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55
        splash = 132
        spring = 133
        meteor = 139
        ripple = 146
        orbit = 163
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H61f5MusicParameters, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.mode = KaitaiStream.resolve_enum(H61f5MusicParameters.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == H61f5MusicParameters.MusicMode.bloom:
            pass
            self.tail = H61f5MusicParameters.BloomTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.day_and_night:
            pass
            self.tail = H61f5MusicParameters.DaynightTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.fountain:
            pass
            self.tail = H61f5MusicParameters.FountainTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.hopping:
            pass
            self.tail = H61f5MusicParameters.HoppingTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.meteor:
            pass
            self.tail = H61f5MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.orbit:
            pass
            self.tail = H61f5MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.piano_keys:
            pass
            self.tail = H61f5MusicParameters.PianoTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.ripple:
            pass
            self.tail = H61f5MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.separation:
            pass
            self.tail = H61f5MusicParameters.SeparationTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.shiny:
            pass
            self.tail = H61f5MusicParameters.ShinyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.splash:
            pass
            self.tail = H61f5MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H61f5MusicParameters.MusicMode.spring:
            pass
            self.tail = H61f5MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == H61f5MusicParameters.MusicMode.bloom:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.day_and_night:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.fountain:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.hopping:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.meteor:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.orbit:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.piano_keys:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.ripple:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.shiny:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.splash:
            pass
            self.tail._fetch_instances()
        elif _on == H61f5MusicParameters.MusicMode.spring:
            pass
            self.tail._fetch_instances()


    def _write__seq(self, io=None):
        super(H61f5MusicParameters, self)._write__seq(io)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == H61f5MusicParameters.MusicMode.bloom:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.day_and_night:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.fountain:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.hopping:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.meteor:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.orbit:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.piano_keys:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.ripple:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.separation:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.shiny:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.splash:
            pass
            self.tail._write__seq(self._io)
        elif _on == H61f5MusicParameters.MusicMode.spring:
            pass
            self.tail._write__seq(self._io)


    def _check(self):
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == H61f5MusicParameters.MusicMode.bloom:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.day_and_night:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.fountain:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.hopping:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.meteor:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.orbit:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.piano_keys:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.ripple:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.separation:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.shiny:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.splash:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H61f5MusicParameters.MusicMode.spring:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        self._dirty = False

    class BloomTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.BloomTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.no_rhythm_speed = self._io.read_u1()
            self.rhythm_speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H61f5MusicParameters.BloomTail, self)._write__seq(io)
            self._io.write_u1(self.no_rhythm_speed)
            self._io.write_u1(self.rhythm_speed)


        def _check(self):
            self._dirty = False


    class DaynightTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.DaynightTail, self).__init__(_io)
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
            super(H61f5MusicParameters.DaynightTail, self)._write__seq(io)
            self._io.write_u1(self.piece_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.gradient)


        def _check(self):
            self._dirty = False


    class EmptyTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.EmptyTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H61f5MusicParameters.EmptyTail, self)._write__seq(io)


        def _check(self):
            self._dirty = False


    class FountainTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.FountainTail, self).__init__(_io)
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
            super(H61f5MusicParameters.FountainTail, self)._write__seq(io)
            self._io.write_u1(self.start_point)
            self._io.write_u1(self.piece_length)
            self._io.write_u1(self.piece_count)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False


    class HoppingTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.HoppingTail, self).__init__(_io)
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
            super(H61f5MusicParameters.HoppingTail, self)._write__seq(io)
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
            super(H61f5MusicParameters.PianoTail, self).__init__(_io)
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
            super(H61f5MusicParameters.PianoTail, self)._write__seq(io)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.key_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.off_minimum)
            self._io.write_u1(self.off_maximum)


        def _check(self):
            self._dirty = False


    class SeparationTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.SeparationTail, self).__init__(_io)
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
            super(H61f5MusicParameters.SeparationTail, self)._write__seq(io)
            self._io.write_u1(self.point)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.companion)


        def _check(self):
            self._dirty = False


    class ShinyTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H61f5MusicParameters.ShinyTail, self).__init__(_io)
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
            super(H61f5MusicParameters.ShinyTail, self)._write__seq(io)
            self._io.write_u1(self.minimum_brightness)
            self._io.write_u1(self.maximum_brightness)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False



