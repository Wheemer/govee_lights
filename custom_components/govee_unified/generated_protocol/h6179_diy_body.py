# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6179DiyBody(ReadWriteKaitaiStruct):
    """SPECULATIVE H6179 compatibility hypothesis: exact-SKU protocol-1.1 DIY
    bodies start with 0xfe and use the candidate single-family or 0xff mixed-family
    palette and pair layouts below.
    Unresolved assumptions: no exact-model capture verifies the family selectors,
    variants, speed, palette length, mixed-pair length or meaning, trailing bytes,
    or transport association.
    """

    class EffectFamily(IntEnum):
        fade = 0
        jumping = 1
        twinkle = 2
        mixed = 255
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6179DiyBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.marker = self._io.read_bytes(1)
        if not self.marker == b"\xFE":
            raise kaitaistruct.ValidationNotEqualError(b"\xFE", self.marker, self._io, u"/seq/0")
        self.family = KaitaiStream.resolve_enum(H6179DiyBody.EffectFamily, self._io.read_u1())
        _on = self.family
        if _on == H6179DiyBody.EffectFamily.fade:
            pass
            self.body = H6179DiyBody.SingleBody(self._io, self, self._root)
            self.body._read()
        elif _on == H6179DiyBody.EffectFamily.jumping:
            pass
            self.body = H6179DiyBody.SingleBody(self._io, self, self._root)
            self.body._read()
        elif _on == H6179DiyBody.EffectFamily.mixed:
            pass
            self.body = H6179DiyBody.MixedBody(self._io, self, self._root)
            self.body._read()
        elif _on == H6179DiyBody.EffectFamily.twinkle:
            pass
            self.body = H6179DiyBody.SingleBody(self._io, self, self._root)
            self.body._read()
        else:
            pass
            self.body = H6179DiyBody.OpaqueBody(self._io, self, self._root)
            self.body._read()
        self.opaque = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.family
        if _on == H6179DiyBody.EffectFamily.fade:
            pass
            self.body._fetch_instances()
        elif _on == H6179DiyBody.EffectFamily.jumping:
            pass
            self.body._fetch_instances()
        elif _on == H6179DiyBody.EffectFamily.mixed:
            pass
            self.body._fetch_instances()
        elif _on == H6179DiyBody.EffectFamily.twinkle:
            pass
            self.body._fetch_instances()
        else:
            pass
            self.body._fetch_instances()


    def _write__seq(self, io=None):
        super(H6179DiyBody, self)._write__seq(io)
        self._io.write_bytes(self.marker)
        self._io.write_u1(int(self.family))
        _on = self.family
        if _on == H6179DiyBody.EffectFamily.fade:
            pass
            self.body._write__seq(self._io)
        elif _on == H6179DiyBody.EffectFamily.jumping:
            pass
            self.body._write__seq(self._io)
        elif _on == H6179DiyBody.EffectFamily.mixed:
            pass
            self.body._write__seq(self._io)
        elif _on == H6179DiyBody.EffectFamily.twinkle:
            pass
            self.body._write__seq(self._io)
        else:
            pass
            self.body._write__seq(self._io)
        self._io.write_bytes(self.opaque)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.marker) != 1:
            raise kaitaistruct.ConsistencyError(u"marker", 1, len(self.marker))
        if not self.marker == b"\xFE":
            raise kaitaistruct.ValidationNotEqualError(b"\xFE", self.marker, None, u"/seq/0")
        _on = self.family
        if _on == H6179DiyBody.EffectFamily.fade:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179DiyBody.EffectFamily.jumping:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179DiyBody.EffectFamily.mixed:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179DiyBody.EffectFamily.twinkle:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        else:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        self._dirty = False

    class EffectPair(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179DiyBody.EffectPair, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.family = KaitaiStream.resolve_enum(H6179DiyBody.EffectFamily, self._io.read_u1())
            self.variant = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179DiyBody.EffectPair, self)._write__seq(io)
            self._io.write_u1(int(self.family))
            self._io.write_u1(self.variant)


        def _check(self):
            self._dirty = False


    class MixedBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179DiyBody.MixedBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.variant = self._io.read_u1()
            self.speed = self._io.read_u1()
            self.len_palette = self._io.read_u1()
            self._raw_palette = self._io.read_bytes(self.len_palette)
            _io__raw_palette = KaitaiStream(BytesIO(self._raw_palette))
            self.palette = H6179DiyBody.Palette(_io__raw_palette, self, self._root)
            self.palette._read()
            self.mix_bytes = self._io.read_u1()
            self.pairs = []
            for i in range(self.mix_bytes // 2):
                _t_pairs = H6179DiyBody.EffectPair(self._io, self, self._root)
                try:
                    _t_pairs._read()
                finally:
                    self.pairs.append(_t_pairs)

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()
            for i in range(len(self.pairs)):
                pass
                self.pairs[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H6179DiyBody.MixedBody, self)._write__seq(io)
            self._io.write_u1(self.variant)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.len_palette)
            _io__raw_palette = KaitaiStream(BytesIO(bytearray(self.len_palette)))
            self._io.add_child_stream(_io__raw_palette)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.len_palette))
            def handler(parent, _io__raw_palette=_io__raw_palette):
                self._raw_palette = _io__raw_palette.to_byte_array()
                if len(self._raw_palette) != self.len_palette:
                    raise kaitaistruct.ConsistencyError(u"raw(palette)", self.len_palette, len(self._raw_palette))
                parent.write_bytes(self._raw_palette)
            _io__raw_palette.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.palette._write__seq(_io__raw_palette)
            self._io.write_u1(self.mix_bytes)
            for i in range(len(self.pairs)):
                pass
                self.pairs[i]._write__seq(self._io)



        def _check(self):
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            if len(self.pairs) != self.mix_bytes // 2:
                raise kaitaistruct.ConsistencyError(u"pairs", self.mix_bytes // 2, len(self.pairs))
            for i in range(len(self.pairs)):
                pass
                if self.pairs[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"pairs", self._root, self.pairs[i]._root)
                if self.pairs[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"pairs", self, self.pairs[i]._parent)

            self._dirty = False


    class OpaqueBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179DiyBody.OpaqueBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179DiyBody.OpaqueBody, self)._write__seq(io)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Palette(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179DiyBody.Palette, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.colours = []
            i = 0
            while not self._io.is_eof():
                _t_colours = govee_shared.GoveeShared.Rgb(self._io)
                try:
                    _t_colours._read()
                finally:
                    self.colours.append(_t_colours)
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.colours)):
                pass
                self.colours[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H6179DiyBody.Palette, self)._write__seq(io)
            for i in range(len(self.colours)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"colours", 0, self._io.size() - self._io.pos())
                self.colours[i]._write__seq(self._io)

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"colours", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.colours)):
                pass

            self._dirty = False


    class SingleBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179DiyBody.SingleBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.variant = self._io.read_u1()
            self.speed = self._io.read_u1()
            self.len_palette = self._io.read_u1()
            self._raw_palette = self._io.read_bytes(self.len_palette)
            _io__raw_palette = KaitaiStream(BytesIO(self._raw_palette))
            self.palette = H6179DiyBody.Palette(_io__raw_palette, self, self._root)
            self.palette._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H6179DiyBody.SingleBody, self)._write__seq(io)
            self._io.write_u1(self.variant)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.len_palette)
            _io__raw_palette = KaitaiStream(BytesIO(bytearray(self.len_palette)))
            self._io.add_child_stream(_io__raw_palette)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.len_palette))
            def handler(parent, _io__raw_palette=_io__raw_palette):
                self._raw_palette = _io__raw_palette.to_byte_array()
                if len(self._raw_palette) != self.len_palette:
                    raise kaitaistruct.ConsistencyError(u"raw(palette)", self.len_palette, len(self._raw_palette))
                parent.write_bytes(self._raw_palette)
            _io__raw_palette.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.palette._write__seq(_io__raw_palette)


        def _check(self):
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False



