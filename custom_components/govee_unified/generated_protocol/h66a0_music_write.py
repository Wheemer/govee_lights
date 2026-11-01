# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H66a0MusicWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H66A0 issue #390.  Android 7.6.01 H66A0 music authoring selects
    the sixteen mode IDs below over 33 05 13.  Classic modes (03..06) carry
    sensitivity, calm flag, fixed-colour flag, and optional RGB triple.  Newer
    modes (30..A9) carry only mode ID and sensitivity after an A3 41 companion
    upload.  AA 05 13 status replies parse the same selector fields.
    """

    class MusicMode(IntEnum):
        rhythm = 3
        spectrum = 4
        energetic = 5
        rolling = 6
        bloom = 48
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55
        flowing_light = 83
        painting = 85
        windmill = 120
        splash = 132
        spring = 133
        beat = 169
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H66a0MusicWrite, self).__init__(_io)
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
        if not self.sub == b"\x13":
            raise kaitaistruct.ValidationNotEqualError(b"\x13", self.sub, self._io, u"/seq/2")
        self._raw_selector = self._io.read_bytes(16)
        _io__raw_selector = KaitaiStream(BytesIO(self._raw_selector))
        self.selector = H66a0MusicWrite.MusicSelector(_io__raw_selector, self, self._root)
        self.selector._read()
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.selector._fetch_instances()


    def _write__seq(self, io=None):
        super(H66a0MusicWrite, self)._write__seq(io)
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
        if not self.sub == b"\x13":
            raise kaitaistruct.ValidationNotEqualError(b"\x13", self.sub, None, u"/seq/2")
        if self.selector._root != self._root:
            raise kaitaistruct.ConsistencyError(u"selector", self._root, self.selector._root)
        if self.selector._parent != self:
            raise kaitaistruct.ConsistencyError(u"selector", self, self.selector._parent)
        self._dirty = False

    class MusicSelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H66a0MusicWrite.MusicSelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H66a0MusicWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            if self.is_legacy:
                pass
                self.style = self._io.read_u1()

            if self.is_legacy:
                pass
                self.has_fixed_colour = self._io.read_u1()

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb = govee_shared.GoveeShared.Rgb(self._io)
                self.rgb._read()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb._fetch_instances()



        def _write__seq(self, io=None):
            super(H66a0MusicWrite.MusicSelector, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            if self.is_legacy:
                pass
                self._io.write_u1(self.style)

            if self.is_legacy:
                pass
                self._io.write_u1(self.has_fixed_colour)

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass
                self.rgb._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if  ((self.is_legacy) and (self.has_fixed_colour != 0)) :
                pass

            self._dirty = False

        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy =  ((self.mode_id == H66a0MusicWrite.MusicMode.rhythm) or (self.mode_id == H66a0MusicWrite.MusicMode.spectrum) or (self.mode_id == H66a0MusicWrite.MusicMode.energetic) or (self.mode_id == H66a0MusicWrite.MusicMode.rolling)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy


