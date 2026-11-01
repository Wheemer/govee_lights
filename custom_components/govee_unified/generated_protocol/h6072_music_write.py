# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h6076_music_write


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6072MusicWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6072, owner confirmations #486.
    Compatibility hypothesis: the six legacy selectors and six companion-backed
    selectors share the floor-lamp music records. Product admission and companion
    defaults are independently qualified for H6072.
    Complete owner captures, unknown suffixes and physical rendering are unqualified.
    """
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6072MusicWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = self._io.read_bytes(1)
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, self._io, u"/seq/1")
        self.sub = self._io.read_bytes(1)
        if not self.sub == b"\x0F":
            raise kaitaistruct.ValidationNotEqualError(b"\x0F", self.sub, self._io, u"/seq/2")
        self._raw_selector = self._io.read_bytes(16)
        _io__raw_selector = KaitaiStream(BytesIO(self._raw_selector))
        self.selector = h6076_music_write.H6076MusicWrite.MusicSelector(_io__raw_selector)
        self.selector._read()
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.selector._fetch_instances()


    def _write__seq(self, io=None):
        super(H6072MusicWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_bytes(self.opcode)
        self._io.write_bytes(self.sub)
        _io__raw_selector = KaitaiStream(BytesIO(bytearray(16)))
        self._io.add_child_stream(_io__raw_selector)
        _pos2 = self._io.pos()
        self._io.seek(self._io.pos() + (16))
        def handler(parent, _io__raw_selector=_io__raw_selector):
            self._raw_selector = _io__raw_selector.to_byte_array()
            if len(self._raw_selector) != 16:
                raise kaitaistruct.ConsistencyError(u"raw(selector)", 16, len(self._raw_selector))
            parent.write_bytes(self._raw_selector)
        _io__raw_selector.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
        self.selector._write__seq(_io__raw_selector)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        if len(self.opcode) != 1:
            raise kaitaistruct.ConsistencyError(u"opcode", 1, len(self.opcode))
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, None, u"/seq/1")
        if len(self.sub) != 1:
            raise kaitaistruct.ConsistencyError(u"sub", 1, len(self.sub))
        if not self.sub == b"\x0F":
            raise kaitaistruct.ValidationNotEqualError(b"\x0F", self.sub, None, u"/seq/2")
        self._dirty = False


