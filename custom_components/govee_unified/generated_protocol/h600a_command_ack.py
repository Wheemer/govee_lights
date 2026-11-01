# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H600aCommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H600A support request #492, owner confirmations #494.
    Compatibility hypothesis: ordinary 33 replies and A3/01 scene or A3/04 DIY
    upload results carry a zero-success status at byte 2. Positive upload
    results precede activation; they do not establish state or rendering.
    Unknown suffix bytes remain opaque. Physical reply availability, latency,
    revision differences and correlation beyond protocol/opcode are unqualified.
    No transaction token or safe replay guarantee is inferred.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H600aCommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = self._io.read_u1()
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes(16)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H600aCommandAck, self)._write__seq(io)
        self._io.write_u1(self.protocol)
        self._io.write_u1(self.opcode)
        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, None, u"/seq/0")
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
    @property
    def is_upload(self):
        if hasattr(self, '_m_is_upload'):
            return self._m_is_upload

        self._m_is_upload = self.protocol == 163
        return getattr(self, '_m_is_upload', None)

    def _invalidate_is_upload(self):
        del self._m_is_upload
    @property
    def protocol_id(self):
        if hasattr(self, '_m_protocol_id'):
            return self._m_protocol_id

        self._m_protocol_id = self.protocol
        return getattr(self, '_m_protocol_id', None)

    def _invalidate_protocol_id(self):
        del self._m_protocol_id

