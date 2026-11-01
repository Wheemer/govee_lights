# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199UploadAckPayload(ReadWriteKaitaiStruct):
    """SPECULATIVE H6199 response hypothesis from issue #115 live qualification.
    On 2026-09-17 HW 3.02.01/FW 1.10.04 returned the same checksum-valid
    A3/04/00 response three times during palette DIY workflows.  These are
    integration notifications, not official-app captures.
    In Android 7.6.01, H6199 DIY uploads use protocol A3 command 0x04 with the
    result byte at absolute offset 2 (zero means success), matching replies on
    protocol and command only.  The sixteen trailing bytes have no established
    meaning and are preserved.  Negative results, nonzero tails, other upload
    commands/revisions, and timing remain physically unqualified.  This result
    does not identify an effect or establish applied device state.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6199UploadAckPayload, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.opcode = self._io.read_u1()
        if not self.opcode == 4:
            raise kaitaistruct.ValidationNotEqualError(4, self.opcode, self._io, u"/seq/0")
        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes(16)
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6199UploadAckPayload, self)._write__seq(io)
        self._io.write_u1(self.opcode)
        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)


    def _check(self):
        if not self.opcode == 4:
            raise kaitaistruct.ValidationNotEqualError(4, self.opcode, None, u"/seq/0")
        if len(self.unknown_tail) != 16:
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 16, len(self.unknown_tail))
        self._dirty = False

    @property
    def is_success(self):
        if hasattr(self, '_m_is_success'):
            return self._m_is_success

        self._m_is_success = self.status == 0
        return getattr(self, '_m_is_success', None)

    def _invalidate_is_success(self):
        del self._m_is_success

