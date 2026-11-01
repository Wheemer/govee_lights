# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GoveeRgbSegmentPage(ReadWriteKaitaiStruct):
    """SPECULATIVE RGB-only pages, H6125 #117 and H6072 #486.
    Compatibility hypothesis: legacy A2 pages contain a one-based group and
    model-declared RGB-only slots, with no brightness byte. Only the declared
    segment count is meaningful. Unused slots and suffix bytes remain opaque;
    their values and physical mapping are unqualified.
    """
    def __init__(self, segment_count, group_size, _io=None, _parent=None, _root=None):
        super(GoveeRgbSegmentPage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.segment_count = segment_count
        self.group_size = group_size

    def _read(self):
        self.group = self._io.read_u1()
        if not self.group >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.group, self._io, u"/seq/0")
        if not self.group <= ((self.segment_count + self.group_size) - 1) // self.group_size:
            raise kaitaistruct.ValidationGreaterThanError(((self.segment_count + self.group_size) - 1) // self.group_size, self.group, self._io, u"/seq/0")
        self.segments = []
        for i in range(self.num_segments):
            _t_segments = GoveeRgbSegmentPage.SegmentRecord(self._io, self, self._root)
            try:
                _t_segments._read()
            finally:
                self.segments.append(_t_segments)

        self.unknown_tail = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.segments)):
            pass
            self.segments[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(GoveeRgbSegmentPage, self)._write__seq(io)
        self._io.write_u1(self.group)
        for i in range(len(self.segments)):
            pass
            self.segments[i]._write__seq(self._io)

        self._io.write_bytes(self.unknown_tail)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


    def _check(self):
        if not self.group >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.group, None, u"/seq/0")
        if not self.group <= ((self.segment_count + self.group_size) - 1) // self.group_size:
            raise kaitaistruct.ValidationGreaterThanError(((self.segment_count + self.group_size) - 1) // self.group_size, self.group, None, u"/seq/0")
        if len(self.segments) != self.num_segments:
            raise kaitaistruct.ConsistencyError(u"segments", self.num_segments, len(self.segments))
        for i in range(len(self.segments)):
            pass
            if self.segments[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"segments", self._root, self.segments[i]._root)
            if self.segments[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"segments", self, self.segments[i]._parent)

        self._dirty = False

    class SegmentRecord(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeRgbSegmentPage.SegmentRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.colour = govee_shared.GoveeShared.Rgb(self._io)
            self.colour._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.colour._fetch_instances()


        def _write__seq(self, io=None):
            super(GoveeRgbSegmentPage.SegmentRecord, self)._write__seq(io)
            self.colour._write__seq(self._io)


        def _check(self):
            self._dirty = False


    @property
    def num_segments(self):
        if hasattr(self, '_m_num_segments'):
            return self._m_num_segments

        self._m_num_segments = (self.group_size if self.group * self.group_size <= self.segment_count else self.segment_count - (self.group - 1) * self.group_size)
        return getattr(self, '_m_num_segments', None)

    def _invalidate_num_segments(self):
        del self._m_num_segments

