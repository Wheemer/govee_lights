# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6LegacyWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 support for issue #402.  Compatibility hypothesis:
    Pact 1/1 uses the whole-device 0D colour operation, without a segment mask.
    Kelvin writes use a white direct-RGB prefix and a companion RGB value.
    This route is independent of native panel/ring enable flags and is not
    used for the owner's segmented revision, which ignores legacy colour
    writes.  Unknown suffix bytes, physical revision behaviour and captures
    for explicit Pact 1/1 remain unresolved.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6LegacyWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(3)
        if not self.header == b"\x33\x05\x0D":
            raise kaitaistruct.ValidationNotEqualError(b"\x33\x05\x0D", self.header, self._io, u"/seq/0")
        self.rgb_direct = govee_shared.GoveeShared.Rgb(self._io)
        self.rgb_direct._read()
        self.kelvin = self._io.read_u2be()
        self.rgb_preview = govee_shared.GoveeShared.Rgb(self._io)
        self.rgb_preview._read()
        self.unknown_tail = self._io.read_bytes(8)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.rgb_direct._fetch_instances()
        self.rgb_preview._fetch_instances()


    def _write__seq(self, io=None):
        super(H60a6LegacyWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self.rgb_direct._write__seq(self._io)
        self._io.write_u2be(self.kelvin)
        self.rgb_preview._write__seq(self._io)
        self._io.write_bytes(self.unknown_tail)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 3:
            raise kaitaistruct.ConsistencyError(u"header", 3, len(self.header))
        if not self.header == b"\x33\x05\x0D":
            raise kaitaistruct.ValidationNotEqualError(b"\x33\x05\x0D", self.header, None, u"/seq/0")
        if len(self.unknown_tail) != 8:
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 8, len(self.unknown_tail))
        self._dirty = False


