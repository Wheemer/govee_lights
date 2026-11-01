# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6125CommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H6125, issue #117.
    Compatibility hypothesis: ordinary replies and A1 uploads use result byte 2;
    A3 music uploads use result byte 3, while A3 DIY uses byte 2.
    The shared single-frame, A1, and A3 acknowledgement handlers
    treat zero as success.  Unknown suffixes and music prefixes remain opaque.
    No transaction identifier is inferred.  A same-protocol, same-command delayed
    acknowledgement remains indistinguishable from a later attempt.
    ACK establishes transport acceptance only, not activation or rendering.
    """

    class ProtocolKind(IntEnum):
        command = 51
        legacy_upload = 161
        upload = 163
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6125CommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = KaitaiStream.resolve_enum(H6125CommandAck.ProtocolKind, self._io.read_u1())
        if not  ((self.protocol == H6125CommandAck.ProtocolKind.command) or (self.protocol == H6125CommandAck.ProtocolKind.legacy_upload) or (self.protocol == H6125CommandAck.ProtocolKind.upload)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65)) :
            pass
            self.unknown_music_prefix = self._io.read_u1()

        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes((15 if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65))  else 16))
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65)) :
            pass



    def _write__seq(self, io=None):
        super(H6125CommandAck, self)._write__seq(io)
        self._io.write_u1(int(self.protocol))
        self._io.write_u1(self.opcode)
        if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65)) :
            pass
            self._io.write_u1(self.unknown_music_prefix)

        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.protocol == H6125CommandAck.ProtocolKind.command) or (self.protocol == H6125CommandAck.ProtocolKind.legacy_upload) or (self.protocol == H6125CommandAck.ProtocolKind.upload)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, None, u"/seq/0")
        if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65)) :
            pass

        if len(self.unknown_tail) != (15 if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65))  else 16):
            raise kaitaistruct.ConsistencyError(u"unknown_tail", (15 if  ((self.protocol == H6125CommandAck.ProtocolKind.upload) and (self.opcode == 65))  else 16), len(self.unknown_tail))
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

        self._m_is_upload =  ((self.protocol == H6125CommandAck.ProtocolKind.legacy_upload) or (self.protocol == H6125CommandAck.ProtocolKind.upload)) 
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

