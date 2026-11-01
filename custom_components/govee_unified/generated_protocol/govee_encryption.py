# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GoveeEncryption(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 encrypted transport, support issue #257.
    Hypothesis: H6099 uses the shared Govee Home 7.6.01 Android BLE encryption
    protocol.  No H6099 official-app capture or owner qualification establishes
    compatibility.  V1 uses a two-phase AES-ECB handshake and full-block AES-ECB
    with an RC4 tail transform; V2 uses AES-GCM with 16-byte tags only.
    Short-MTU fragmented E719/E71A layouts are not implemented.  Unknown
    marker/advertisement tails and V1 padding remain opaque.  Advertisement flags
    follow the shared broadcast Pact format; omission is not negative encryption
    evidence.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(GoveeEncryption, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(GoveeEncryption, self)._write__seq(io)


    def _check(self):
        self._dirty = False

    class Advertisement(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.Advertisement, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.flags = self._io.read_u1()
            self.magic = self._io.read_bytes(2)
            self.pact_type = self._io.read_u2be()
            self.pact_code = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.Advertisement, self)._write__seq(io)
            self._io.write_u1(self.flags)
            self._io.write_bytes(self.magic)
            self._io.write_u2be(self.pact_type)
            self._io.write_u1(self.pact_code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.magic) != 2:
                raise kaitaistruct.ConsistencyError(u"magic", 2, len(self.magic))
            self._dirty = False


    class Marker(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.Marker, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.format = self._io.read_u1()
            self.version = self._io.read_u1()
            if self.format == 2:
                pass
                self.flag = self._io.read_u1()

            if self.format == 2:
                pass
                self.pact_type = self._io.read_u2be()

            if self.format == 2:
                pass
                self.pact_code = self._io.read_u1()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.format == 2:
                pass

            if self.format == 2:
                pass

            if self.format == 2:
                pass



        def _write__seq(self, io=None):
            super(GoveeEncryption.Marker, self)._write__seq(io)
            self._io.write_u1(self.format)
            self._io.write_u1(self.version)
            if self.format == 2:
                pass
                self._io.write_u1(self.flag)

            if self.format == 2:
                pass
                self._io.write_u2be(self.pact_type)

            if self.format == 2:
                pass
                self._io.write_u1(self.pact_code)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.format == 2:
                pass

            if self.format == 2:
                pass

            if self.format == 2:
                pass

            self._dirty = False


    class V1Handshake(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.V1Handshake, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.magic = self._io.read_u1()
            self.opcode = self._io.read_u1()
            self.body = self._io.read_bytes(16)
            self.unknown_padding = self._io.read_bytes(1)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.V1Handshake, self)._write__seq(io)
            self._io.write_u1(self.magic)
            self._io.write_u1(self.opcode)
            self._io.write_bytes(self.body)
            self._io.write_bytes(self.unknown_padding)
            self._io.write_u1(self.checksum)


        def _check(self):
            if len(self.body) != 16:
                raise kaitaistruct.ConsistencyError(u"body", 16, len(self.body))
            if len(self.unknown_padding) != 1:
                raise kaitaistruct.ConsistencyError(u"unknown_padding", 1, len(self.unknown_padding))
            self._dirty = False


    class V2Frame(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.V2Frame, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.counter = self._io.read_u4be()
            self.sealed = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.V2Frame, self)._write__seq(io)
            self._io.write_u4be(self.counter)
            self._io.write_bytes(self.sealed)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"sealed", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class V2Identity(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.V2Identity, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.iv_key = self._io.read_bytes(8)
            self.sku = self._io.read_bytes(5)
            self.mac_wire_order = self._io.read_bytes(6)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.V2Identity, self)._write__seq(io)
            self._io.write_bytes(self.iv_key)
            self._io.write_bytes(self.sku)
            self._io.write_bytes(self.mac_wire_order)


        def _check(self):
            if len(self.iv_key) != 8:
                raise kaitaistruct.ConsistencyError(u"iv_key", 8, len(self.iv_key))
            if len(self.sku) != 5:
                raise kaitaistruct.ConsistencyError(u"sku", 5, len(self.sku))
            if len(self.mac_wire_order) != 6:
                raise kaitaistruct.ConsistencyError(u"mac_wire_order", 6, len(self.mac_wire_order))
            self._dirty = False


    class V2Request(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.V2Request, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.magic = self._io.read_u1()
            self.opcode = self._io.read_u1()
            self.direction = self._io.read_u1()
            self.nonce = self._io.read_bytes(12)
            self.tag_length = self._io.read_u1()
            self.sealed = self._io.read_bytes(24)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.V2Request, self)._write__seq(io)
            self._io.write_u1(self.magic)
            self._io.write_u1(self.opcode)
            self._io.write_u1(self.direction)
            self._io.write_bytes(self.nonce)
            self._io.write_u1(self.tag_length)
            self._io.write_bytes(self.sealed)


        def _check(self):
            if len(self.nonce) != 12:
                raise kaitaistruct.ConsistencyError(u"nonce", 12, len(self.nonce))
            if len(self.sealed) != 24:
                raise kaitaistruct.ConsistencyError(u"sealed", 24, len(self.sealed))
            self._dirty = False


    class V2Response(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GoveeEncryption.V2Response, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.magic = self._io.read_u1()
            self.opcode = self._io.read_u1()
            self.status = self._io.read_u1()
            self.nonce = self._io.read_bytes(12)
            self.sealed = self._io.read_bytes(35)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(GoveeEncryption.V2Response, self)._write__seq(io)
            self._io.write_u1(self.magic)
            self._io.write_u1(self.opcode)
            self._io.write_u1(self.status)
            self._io.write_bytes(self.nonce)
            self._io.write_bytes(self.sealed)


        def _check(self):
            if len(self.nonce) != 12:
                raise kaitaistruct.ConsistencyError(u"nonce", 12, len(self.nonce))
            if len(self.sealed) != 35:
                raise kaitaistruct.ConsistencyError(u"sealed", 35, len(self.sealed))
            self._dirty = False



