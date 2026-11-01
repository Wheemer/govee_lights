# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H617aControlPayload(ReadWriteKaitaiStruct):
    """SPECULATIVE H617A support work under capability umbrella issue #286;
    Fountain alternative geometry also relates to issue #129 (whose historical
    segment-count wording must not be interpreted as physical IC metadata).
    Hypothesis: Android 7.6.01 H617A music authoring uses the generalised
    mode-specific tails below.
    Existing H617A captures establish preset bytes and the palette-relative layout,
    not every representable value.  Newly variable Bloom no-rhythm speed, Shiny speed,
    Hopping speed/piece ranges, Piano speed/off-minimum, and Fountain piece length
    remain app-derived; alternate values and geometry need attributable official-app
    captures and owner qualification.  Other fields retain their existing captured
    values with app-derived semantic names.  Grouping tails here does not erase that
    evidence.
    H617E shares music_body's structural parser but keeps its independently declared
    pre-expansion presets, controls, and IC policy.  No new H617E qualification follows.
    H6099 uses its separate speculative/h6099_music_parameters schema and exact-model
    policy; shared app builders are evidence clues, not interchangeable SKU support.
    AA0F=15 was directly observed on H617A HW3.01.01/FW3.02.24, not in an official-app
    capture.  Its signed-positive boundary and ignored tail are app-derived.  Shared
    H617A-status-grammar consumers do not acquire exact-model count qualification.
    Count never establishes physical IC count or changes logical segment geometry.
    No full music-body readback, alternative IC geometry, or new rendering is qualified.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H617aControlPayload, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H617aControlPayload, self)._write__seq(io)


    def _check(self):
        self._dirty = False

    class BloomTail(ReadWriteKaitaiStruct):
        """Bloom music tail; explicit styles set both speeds."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.BloomTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.no_rhythm_speed = self._io.read_u1()
            self.rhythm_speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617aControlPayload.BloomTail, self)._write__seq(io)
            self._io.write_u1(self.no_rhythm_speed)
            self._io.write_u1(self.rhythm_speed)


        def _check(self):
            self._dirty = False


    class DayAndNightTail(ReadWriteKaitaiStruct):
        """Day and Night music tail; piece count is not logical segment count."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.DayAndNightTail, self).__init__(_io)
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
            super(H617aControlPayload.DayAndNightTail, self)._write__seq(io)
            self._io.write_u1(self.piece_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.gradient)


        def _check(self):
            self._dirty = False


    class FountainTail(ReadWriteKaitaiStruct):
        """Fountain music tail: start point, piece length, piece count, and speed."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.FountainTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.start_point = self._io.read_u1()
            self.piece_len = self._io.read_u1()
            self.piece_num = self._io.read_u1()
            self.speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617aControlPayload.FountainTail, self)._write__seq(io)
            self._io.write_u1(self.start_point)
            self._io.write_u1(self.piece_len)
            self._io.write_u1(self.piece_num)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False


    class HoppingTail(ReadWriteKaitaiStruct):
        """Hopping music tail: background RGB, relative brightness, speed, and piece bounds."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.HoppingTail, self).__init__(_io)
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
            super(H617aControlPayload.HoppingTail, self)._write__seq(io)
            self.background._write__seq(self._io)
            self._io.write_u1(self.rel_brightness)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.piece_length_min)
            self._io.write_u1(self.piece_length_max)
            self._io.write_u1(self.piece_count_min)
            self._io.write_u1(self.piece_count_max)


        def _check(self):
            self._dirty = False


    class LightCountBody(ReadWriteKaitaiStruct):
        """AA0F light-count reply body: the first payload byte is interpreted as a
        positive signed byte (1..127), stored separately from physical IC metadata,
        and queried with a zero-filled body.  Unconsumed bytes remain unknown.
        Diagnostic only.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.LightCountBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.light_count = self._io.read_u1()
            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617aControlPayload.LightCountBody, self)._write__seq(io)
            self._io.write_u1(self.light_count)
            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid

            self._m_is_valid =  ((self.light_count > 0) and (self.light_count <= 127)) 
            return getattr(self, '_m_is_valid', None)

        def _invalidate_is_valid(self):
            del self._m_is_valid

    class PianoKeysTail(ReadWriteKaitaiStruct):
        """Piano Keys music tail; off_maximum = max(off_minimum, key_count / 2)."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.PianoKeysTail, self).__init__(_io)
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
            super(H617aControlPayload.PianoKeysTail, self)._write__seq(io)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.key_count)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.off_minimum)
            self._io.write_u1(self.off_maximum)


        def _check(self):
            self._dirty = False


    class SeparationTail(ReadWriteKaitaiStruct):
        """Separation music tail; gradient speed depends on physical IC count."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.SeparationTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.point = self._io.read_u1()
            self.gradient = self._io.read_u1()
            self.speed = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H617aControlPayload.SeparationTail, self)._write__seq(io)
            self._io.write_u1(self.point)
            self._io.write_u1(self.gradient)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False


    class ShinyTail(ReadWriteKaitaiStruct):
        """Shiny music tail: minimum brightness, maximum brightness, and speed."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H617aControlPayload.ShinyTail, self).__init__(_io)
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
            super(H617aControlPayload.ShinyTail, self)._write__seq(io)
            self._io.write_u1(self.minimum_brightness)
            self._io.write_u1(self.maximum_brightness)
            self._io.write_u1(self.speed)


        def _check(self):
            self._dirty = False



