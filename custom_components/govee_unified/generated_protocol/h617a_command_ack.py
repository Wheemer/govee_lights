# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H617aCommandAck(ReadWriteKaitaiStruct):
    """SPECULATIVE H617A support work under capability umbrella issue #286.
    In Android 7.6.01, ordinary 0x33 command replies and A3/02 or A3/04 DIY/scene
    uploads report status at absolute byte 2, whereas A3/41 music uploads report
    status at absolute byte 3, with zero meaning success.  The H617A workflow
    activates native DIY and music only after a positive upload result.
    Hypothesis: these acknowledgement layouts describe H617A replies on the tested
    revision.  Ordinary positive replies have direct-device evidence; A3/negative
    replies, suffixes, timing, and other revisions lack official-app capture or
    owner qualification.  Replies match protocol and command only.  Music byte 2
    is not a transaction ID.  An H6076 capture (issue #343) shows it repeating the
    music mode; the H617A value remains unconfirmed, so the field keeps its name.
    A delayed same-subtype ACK during a later final attempt is indistinguishable.
    ACK never establishes applied device state.
    H617E and other command_grammar=H617A consumers structurally share this parser;
    this adds no exact-SKU ACK qualification or upload-ACK policy for them.  H6099
    retains its independent speculative command-ACK parser and upload policy.
    H6102 #115 (goods type 18, Pact 10) and H7025 #148 independently use the same
    A3/02 and A3/04 byte-2 and A3/41 byte-3 acknowledgement layouts and require a
    positive upload result before activation; schema reuse is not donor
    qualification, and no H7025 mode echo, transaction token, or LAN receipt
    guarantee is inferred from the H607C observation in #148.
    H6097 #431 independently shares A3/02 and A3/04 result-byte-2 and A3/41
    result-byte-3 handling.  No mode echo or transaction token is established.
    An attempted upload is not automatically replayed after an uncertain result.
    H7020 #363 reuses ordinary zero-success ACKs, including configured strings,
    and the A3/02 and A3/04 result-byte-2 forms.  This is candidate structural
    compatibility, not exact-model capture qualification or state confirmation.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H617aCommandAck, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.protocol = self._io.read_u1()
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, self._io, u"/seq/0")
        self.opcode = self._io.read_u1()
        if  ((self.is_upload) and (self.opcode == 65)) :
            pass
            self.unknown_music_prefix = self._io.read_u1()

        self.status = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes((15 if  ((self.is_upload) and (self.opcode == 65))  else 16))
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        if  ((self.is_upload) and (self.opcode == 65)) :
            pass



    def _write__seq(self, io=None):
        super(H617aCommandAck, self)._write__seq(io)
        self._io.write_u1(self.protocol)
        self._io.write_u1(self.opcode)
        if  ((self.is_upload) and (self.opcode == 65)) :
            pass
            self._io.write_u1(self.unknown_music_prefix)

        self._io.write_u1(self.status)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if not  ((self.protocol == 51) or (self.protocol == 163)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.protocol, None, u"/seq/0")
        if  ((self.is_upload) and (self.opcode == 65)) :
            pass

        if len(self.unknown_tail) != (15 if  ((self.is_upload) and (self.opcode == 65))  else 16):
            raise kaitaistruct.ConsistencyError(u"unknown_tail", (15 if  ((self.is_upload) and (self.opcode == 65))  else 16), len(self.unknown_tail))
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

