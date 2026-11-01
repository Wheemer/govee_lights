# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6CommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 support for issue #402.  Compatibility hypothesis:
    ordinary 33 and A4/58 replies put the result after the opcode, whereas
    A3/58 has one opaque byte before the result.  Zero denotes success.
    Acknowledgements have
    no transaction identifier or content/readback guarantee.  Their timing,
    late duplicates and revision coverage require capture qualification.
    Unknown suffix bytes remain opaque.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6CommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = self._io.read_u1()
        if not  ((self.protocol == 51) or (self.protocol == 163) or (self.protocol == 164)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        if  ((self.protocol == 163) and (self.opcode == 88)) :
            pass
            self.unknown_a3_prefix = self._io.read_u1()

        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes((15 if  ((self.protocol == 163) and (self.opcode == 88))  else 16))
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        if  ((self.protocol == 163) and (self.opcode == 88)) :
            pass



    def _write__seq(self, io=None):
        super(H60a6CommandAck, self)._write__seq(io)
        self._io.write_u1(self.protocol)
        self._io.write_u1(self.opcode)
        if  ((self.protocol == 163) and (self.opcode == 88)) :
            pass
            self._io.write_u1(self.unknown_a3_prefix)

        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.protocol == 51) or (self.protocol == 163) or (self.protocol == 164)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, None, u"/seq/0")
        if  ((self.protocol == 163) and (self.opcode == 88)) :
            pass

        if len(self.unknown_tail) != (15 if  ((self.protocol == 163) and (self.opcode == 88))  else 16):
            raise kaitaistruct.ConsistencyError(u"unknown_tail", (15 if  ((self.protocol == 163) and (self.opcode == 88))  else 16), len(self.unknown_tail))
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

        self._m_is_upload =  ((self.protocol == 163) or (self.protocol == 164)) 
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

