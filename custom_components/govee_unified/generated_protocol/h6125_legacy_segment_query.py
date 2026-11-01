# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6125LegacySegmentQuery(ReadWriteKaitaiStruct):
    """SPECULATIVE H6125, issue #117.
    Compatibility hypothesis: legacy segment readback queries four A2 groups
    for fifteen logical segments.  The command carries a one-based group and
    zero-filled request bytes.  Reply padding and hardware acceptance remain
    unqualified and are not constrained by this writer.
    """

    class QueryDomain(IntEnum):
        segments = 162
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6125LegacySegmentQuery, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6125LegacySegmentQuery.QueryDomain, self._io.read_u1())
        if not self.domain == H6125LegacySegmentQuery.QueryDomain.segments:
            raise kaitaistruct.ValidationNotEqualError(H6125LegacySegmentQuery.QueryDomain.segments, self.domain, self._io, u"/seq/1")
        self.group = self._io.read_u1()
        if not self.group >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.group, self._io, u"/seq/2")
        if not self.group <= 4:
            raise kaitaistruct.ValidationGreaterThanError(4, self.group, self._io, u"/seq/2")
        self.padding = self._io.read_bytes(16)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6125LegacySegmentQuery, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        self._io.write_u1(self.group)
        self._io.write_bytes(self.padding)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, None, u"/seq/0")
        if not self.domain == H6125LegacySegmentQuery.QueryDomain.segments:
            raise kaitaistruct.ValidationNotEqualError(H6125LegacySegmentQuery.QueryDomain.segments, self.domain, None, u"/seq/1")
        if not self.group >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.group, None, u"/seq/2")
        if not self.group <= 4:
            raise kaitaistruct.ValidationGreaterThanError(4, self.group, None, u"/seq/2")
        if len(self.padding) != 16:
            raise kaitaistruct.ConsistencyError(u"padding", 16, len(self.padding))
        self._dirty = False


