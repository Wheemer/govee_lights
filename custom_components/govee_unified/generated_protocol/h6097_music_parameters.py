# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from custom_components.govee_unified.generated_protocol import h6097_music_write
from custom_components.govee_unified.generated_protocol import h6099_music_parameters
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6097MusicParameters(ReadWriteKaitaiStruct):
    """SPECULATIVE H6097 support for issue #431.  A3/41 carries mode, palette and
    these mode-specific tails before selector activation.  Shared tail structures
    are compatible with H6099, but Energetic independently carries two opaque
    parameter bytes (default 01 00).  Physical IC count is independent of the
    fourteen logical zones.  Parameter rendering, Energetic byte semantics and
    firmware differences remain unqualified.
    """

    class CompanionMode(IntEnum):
        energetic = 5
        bloom = 48
        shiny = 49
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6097MusicParameters, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.mode = KaitaiStream.resolve_enum(h6097_music_write.H6097MusicWrite.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == h6097_music_write.H6097MusicWrite.MusicMode.bloom:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.BloomTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.day_and_night:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.DaynightTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.energetic:
            pass
            self.tail = H6097MusicParameters.EnergeticTail(self._io, self, self._root)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.fountain:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.FountainTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.hopping:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.HoppingTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.piano_keys:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.PianoTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.separation:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.SeparationTail(self._io)
            self.tail._read()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.shiny:
            pass
            self.tail = h6099_music_parameters.H6099MusicParameters.ShinyTail(self._io)
            self.tail._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == h6097_music_write.H6097MusicWrite.MusicMode.bloom:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.day_and_night:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.energetic:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.fountain:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.hopping:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.piano_keys:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.shiny:
            pass
            self.tail._fetch_instances()


    def _write__seq(self, io=None):
        super(H6097MusicParameters, self)._write__seq(io)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == h6097_music_write.H6097MusicWrite.MusicMode.bloom:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.day_and_night:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.energetic:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.fountain:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.hopping:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.piano_keys:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.separation:
            pass
            self.tail._write__seq(self._io)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.shiny:
            pass
            self.tail._write__seq(self._io)


    def _check(self):
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == h6097_music_write.H6097MusicWrite.MusicMode.bloom:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.day_and_night:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.energetic:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.fountain:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.hopping:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.piano_keys:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.separation:
            pass
        elif _on == h6097_music_write.H6097MusicWrite.MusicMode.shiny:
            pass
        self._dirty = False

    class EnergeticTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6097MusicParameters.EnergeticTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_parameters = self._io.read_bytes(2)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6097MusicParameters.EnergeticTail, self)._write__seq(io)
            self._io.write_bytes(self.unknown_parameters)


        def _check(self):
            if len(self.unknown_parameters) != 2:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 2, len(self.unknown_parameters))
            self._dirty = False



