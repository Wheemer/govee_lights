# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h6076_music_body


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6072MusicAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H6072, owner confirmations #486.
    Compatibility hypothesis: A3 subtype 41 has a mode and result, with zero
    indicating upload success. This is separate from active-selection readback.
    Exact-model mode echo, other result values and timing are unqualified.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6072MusicAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = self._io.read_bytes(1)
        if not self.protocol == b"\xA3":
            raise kaitaistruct.ValidationNotEqualError(b"\xA3", self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        if not self.opcode == 65:
            raise kaitaistruct.ValidationNotEqualError(65, self.opcode, self._io, u"/seq/1")
        self.mode = KaitaiStream.resolve_enum(h6076_music_body.H6076MusicBody.MusicMode, self._io.read_u1())
        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes(15)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6072MusicAck, self)._write__seq(io)
        self._io.write_bytes(self.protocol)
        self._io.write_u1(self.opcode)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.protocol) != 1:
            raise kaitaistruct.ConsistencyError(u"protocol", 1, len(self.protocol))
        if not self.protocol == b"\xA3":
            raise kaitaistruct.ValidationNotEqualError(b"\xA3", self.protocol, None, u"/seq/0")
        if not self.opcode == 65:
            raise kaitaistruct.ValidationNotEqualError(65, self.opcode, None, u"/seq/1")
        if len(self.unknown_tail) != 15:
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 15, len(self.unknown_tail))
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
    def protocol_id(self):
        if hasattr(self, '_m_protocol_id'):
            return self._m_protocol_id

        self._m_protocol_id = KaitaiStream.byte_array_index(self.protocol, 0)
        return getattr(self, '_m_protocol_id', None)

    def _invalidate_protocol_id(self):
        del self._m_protocol_id

