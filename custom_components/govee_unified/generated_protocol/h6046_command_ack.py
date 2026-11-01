# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h6046_command_write


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6046CommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE (audited prospective) H6046, support issue #479.
    Evidence class: exact-model behavioural audit, not captures or hardware
    qualification. Known Pact 1/1 and 2/1 use ordinary 0x33 command results and
    A3 upload results. Each 20-byte frame ends with XOR of bytes 0..18.
    Ordinary commands echo the opcode and carry a result at offset 2.
    A3 scene 0x02 and DIY 0x04 results also occupy offset 2; music 0x41 instead
    echoes its mode there and places the result at offset 3.
    Zero means upload acceptance, not selector activation or visible rendering.
    Correlate protocol, subtype and music mode, never the mode byte as a result.
    Unresolved assumptions: nonzero result meanings, opaque suffixes, reply
    timing and unreported revisions. No zero-only result or suffix validation.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6046CommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = self._io.read_u1()
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        if  ((self.protocol == 163) and (self.opcode == 65)) :
            pass
            self.mode = KaitaiStream.resolve_enum(h6046_command_write.H6046CommandWrite.MusicMode, self._io.read_u1())

        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes((15 if  ((self.protocol == 163) and (self.opcode == 65))  else 16))
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        if  ((self.protocol == 163) and (self.opcode == 65)) :
            pass



    def _write__seq(self, io=None):
        super(H6046CommandAck, self)._write__seq(io)
        self._io.write_u1(self.protocol)
        self._io.write_u1(self.opcode)
        if  ((self.protocol == 163) and (self.opcode == 65)) :
            pass
            self._io.write_u1(int(self.mode))

        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, None, u"/seq/0")
        if  ((self.protocol == 163) and (self.opcode == 65)) :
            pass

        if len(self.unknown_tail) != (15 if  ((self.protocol == 163) and (self.opcode == 65))  else 16):
            raise kaitaistruct.ConsistencyError(u"unknown_tail", (15 if  ((self.protocol == 163) and (self.opcode == 65))  else 16), len(self.unknown_tail))
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

        self._m_is_upload =  ((self.protocol == 163) and ( ((self.opcode == 2) or (self.opcode == 4) or (self.opcode == 65)) )) 
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

