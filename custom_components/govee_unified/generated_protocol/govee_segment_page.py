# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GoveeSegmentPage(ReadWriteKaitaiStruct):
    """Brightness/RGB records with model-declared cardinality. Wire slots need not
    all represent segments. Unused octets are retained, never inferred from black
    or off records. Only models with evidenced zero padding enforce zeroes.
    """
    def __init__(self, segment_count, group_size, unused_must_be_zero, _io=None, _parent=None, _root=None):
        super(GoveeSegmentPage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.segment_count = segment_count
        self.group_size = group_size
        self.unused_must_be_zero = unused_must_be_zero

    def _read(self):
        self.group = self._io.read_u1()
        if not self.group >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.group, self._io, u"/seq/0")
        if not self.group <= ((self.segment_count + self.group_size) - 1) // self.group_size:
            raise kaitaistruct.ValidationGreaterThanError(((self.segment_count + self.group_size) - 1) // self.group_size, self.group, self._io, u"/seq/0")
        self.segments = []
        for i in range(self.num_segments):
            _t_segments = GoveeSegmentPage.SegmentRecord(self._io, self, self._root)
            try:
                _t_segments._read()
            finally:
                self.segments.append(_t_segments)

        self.unused = []
        for i in range((4 - self.num_segments) * 4):
            self.unused.append(self._io.read_u1())
            _ = self.unused[i]
            if not  (((not (self.unused_must_be_zero))) or (_ == 0)) :
                raise kaitaistruct.ValidationExprError(self.unused[i], self._io, u"/seq/2")

        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.segments)):
            pass
            self.segments[i]._fetch_instances()

        for i in range(len(self.unused)):
            pass



    def _write__seq(self, io=None):
        super(GoveeSegmentPage, self)._write__seq(io)
        self._io.write_u1(self.group)
        for i in range(len(self.segments)):
            pass
            self.segments[i]._write__seq(self._io)

        for i in range(len(self.unused)):
            pass
            self._io.write_u1(self.unused[i])



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

        if len(self.unused) != (4 - self.num_segments) * 4:
            raise kaitaistruct.ConsistencyError(u"unused", (4 - self.num_segments) * 4, len(self.unused))
        for i in range(len(self.unused)):
            pass
            _ = self.unused[i]
            if not  (((not (self.unused_must_be_zero))) or (_ == 0)) :
                raise kaitaistruct.ValidationExprError(self.unused[i], None, u"/seq/2")

        self._dirty = False

    class SegmentRecord(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeSegmentPage.SegmentRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.brightness = self._io.read_u1()
            self.colour = govee_shared.GoveeShared.Rgb(self._io)
            self.colour._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.colour._fetch_instances()


        def _write__seq(self, io=None):
            super(GoveeSegmentPage.SegmentRecord, self)._write__seq(io)
            self._io.write_u1(self.brightness)
            self.colour._write__seq(self._io)


        def _check(self):
            self._dirty = False


    @property
    def num_segments(self):
        """Meaningful record count, independent of unused wire slots and record values."""
        if hasattr(self, '_m_num_segments'):
            return self._m_num_segments

        self._m_num_segments = (self.group_size if self.group * self.group_size <= self.segment_count else self.segment_count - (self.group - 1) * self.group_size)
        return getattr(self, '_m_num_segments', None)

    def _invalidate_num_segments(self):
        del self._m_num_segments

