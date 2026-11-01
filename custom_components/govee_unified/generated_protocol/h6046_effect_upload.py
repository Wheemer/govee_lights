# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6046EffectUpload(ReadWriteKaitaiStruct):
    """SPECULATIVE (audited prospective) H6046, support issue #479.
    Evidence class: exact-model behavioural audit and exact-SKU catalogue
    structures, not captures or hardware qualification. Known Pact 1/1 and 2/1
    admit shared type-1 parameters, type-2 layers and H6046 type-4 flat/mixed DIY.
    This reassembled content starts with marker 1, line count and body kind.
    Physical A3 fragments use the shared 20-byte XOR envelope; this root does not
    duplicate transport fragmentation. Upload acceptance precedes the separate
    16-bit scene/DIY selector. Selector status is not content readback.
    Flat DIY has family, variant, speed and byte-length-prefixed RGB palette.
    Mixed family 255 appends a byte length and up to four family/variant pairs.
    Palette size is 1..8, speed 1..100 with default 50. Family and variant are
    wire selectors, not editor identities. Product eligibility, scene carrier
    selection and storage-slot approval remain profile/catalogue policy.
    Unsupported and AI families are not admitted. No whole-SKU alias is used.
    Unresolved assumptions: nondefault variants, suffix meanings, other revisions
    and visible rendering. Uncertain tails remain opaque without zero validation.
    """

    class BodyKind(IntEnum):
        builtin_parameters = 1
        scene = 2
        diy = 4

    class EffectFamily(IntEnum):
        fade = 0
        jumping = 1
        twinkle = 2
        breathing = 5
        stream = 8
        flow = 9
        chase = 10
        snow = 11
        aurora = 13
        mixed = 255
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6046EffectUpload, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x01", self.header, self._io, u"/seq/0")
        self.chunk_count = self._io.read_u1()
        self.kind = KaitaiStream.resolve_enum(H6046EffectUpload.BodyKind, self._io.read_u1())
        if not  ((self.kind == H6046EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6046EffectUpload.BodyKind.scene) or (self.kind == H6046EffectUpload.BodyKind.diy)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.kind, self._io, u"/seq/2")
        _on = self.kind
        if _on == H6046EffectUpload.BodyKind.builtin_parameters:
            pass
            self.content = govee_shared.GoveeShared.SceneType1Content(self._io)
            self.content._read()
        elif _on == H6046EffectUpload.BodyKind.diy:
            pass
            self.content = H6046EffectUpload.DiyContent(self._io, self, self._root)
            self.content._read()
        elif _on == H6046EffectUpload.BodyKind.scene:
            pass
            self.content = H6046EffectUpload.SceneContent(self._io, self, self._root)
            self.content._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.kind
        if _on == H6046EffectUpload.BodyKind.builtin_parameters:
            pass
            self.content._fetch_instances()
        elif _on == H6046EffectUpload.BodyKind.diy:
            pass
            self.content._fetch_instances()
        elif _on == H6046EffectUpload.BodyKind.scene:
            pass
            self.content._fetch_instances()


    def _write__seq(self, io=None):
        super(H6046EffectUpload, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(self.chunk_count)
        self._io.write_u1(int(self.kind))
        _on = self.kind
        if _on == H6046EffectUpload.BodyKind.builtin_parameters:
            pass
            self.content._write__seq(self._io)
        elif _on == H6046EffectUpload.BodyKind.diy:
            pass
            self.content._write__seq(self._io)
        elif _on == H6046EffectUpload.BodyKind.scene:
            pass
            self.content._write__seq(self._io)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x01", self.header, None, u"/seq/0")
        if not  ((self.kind == H6046EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6046EffectUpload.BodyKind.scene) or (self.kind == H6046EffectUpload.BodyKind.diy)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.kind, None, u"/seq/2")
        _on = self.kind
        if _on == H6046EffectUpload.BodyKind.builtin_parameters:
            pass
        elif _on == H6046EffectUpload.BodyKind.diy:
            pass
            if self.content._root != self._root:
                raise kaitaistruct.ConsistencyError(u"content", self._root, self.content._root)
            if self.content._parent != self:
                raise kaitaistruct.ConsistencyError(u"content", self, self.content._parent)
        elif _on == H6046EffectUpload.BodyKind.scene:
            pass
            if self.content._root != self._root:
                raise kaitaistruct.ConsistencyError(u"content", self._root, self.content._root)
            if self.content._parent != self:
                raise kaitaistruct.ConsistencyError(u"content", self, self.content._parent)
        self._dirty = False

    class Block(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046EffectUpload.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.len_body = self._io.read_u1()
            self._raw_body = self._io.read_bytes(self.len_body)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = govee_shared.GoveeShared.EffectLayer(_io__raw_body)
            self.body._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(H6046EffectUpload.Block, self)._write__seq(io)
            self._io.write_u1(self.len_body)
            _io__raw_body = KaitaiStream(BytesIO(bytearray(self.len_body)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.len_body))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != self.len_body:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", self.len_body, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)


        def _check(self):
            self._dirty = False


    class DiyContent(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046EffectUpload.DiyContent, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.family = KaitaiStream.resolve_enum(H6046EffectUpload.EffectFamily, self._io.read_u1())
            if not  ((self.family == H6046EffectUpload.EffectFamily.fade) or (self.family == H6046EffectUpload.EffectFamily.jumping) or (self.family == H6046EffectUpload.EffectFamily.twinkle) or (self.family == H6046EffectUpload.EffectFamily.breathing) or (self.family == H6046EffectUpload.EffectFamily.stream) or (self.family == H6046EffectUpload.EffectFamily.flow) or (self.family == H6046EffectUpload.EffectFamily.chase) or (self.family == H6046EffectUpload.EffectFamily.snow) or (self.family == H6046EffectUpload.EffectFamily.aurora) or (self.family == H6046EffectUpload.EffectFamily.mixed)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.family, self._io, u"/types/diy_content/seq/0")
            self.variant = self._io.read_u1()
            self.speed = self._io.read_u1()
            if not self.speed >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.speed, self._io, u"/types/diy_content/seq/2")
            if not self.speed <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.speed, self._io, u"/types/diy_content/seq/2")
            self.palette_len = self._io.read_u1()
            _ = self.palette_len
            if not  ((_ >= 3) and (_ <= 24) and (_ % 3 == 0)) :
                raise kaitaistruct.ValidationExprError(self.palette_len, self._io, u"/types/diy_content/seq/3")
            self.palette = []
            for i in range(self.palette_len // 3):
                _t_palette = govee_shared.GoveeShared.Rgb(self._io)
                try:
                    _t_palette._read()
                finally:
                    self.palette.append(_t_palette)

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                self.mix_bytes = self._io.read_u1()
                _ = self.mix_bytes
                if not  ((_ <= 8) and (_ % 2 == 0)) :
                    raise kaitaistruct.ValidationExprError(self.mix_bytes, self._io, u"/types/diy_content/seq/5")

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                self.pairs = []
                for i in range(self.mix_bytes // 2):
                    _t_pairs = H6046EffectUpload.EffectPair(self._io, self, self._root)
                    try:
                        _t_pairs._read()
                    finally:
                        self.pairs.append(_t_pairs)


            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.palette)):
                pass
                self.palette[i]._fetch_instances()

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                for i in range(len(self.pairs)):
                    pass
                    self.pairs[i]._fetch_instances()




        def _write__seq(self, io=None):
            super(H6046EffectUpload.DiyContent, self)._write__seq(io)
            self._io.write_u1(int(self.family))
            self._io.write_u1(self.variant)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.palette_len)
            for i in range(len(self.palette)):
                pass
                self.palette[i]._write__seq(self._io)

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                self._io.write_u1(self.mix_bytes)

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                for i in range(len(self.pairs)):
                    pass
                    self.pairs[i]._write__seq(self._io)


            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not  ((self.family == H6046EffectUpload.EffectFamily.fade) or (self.family == H6046EffectUpload.EffectFamily.jumping) or (self.family == H6046EffectUpload.EffectFamily.twinkle) or (self.family == H6046EffectUpload.EffectFamily.breathing) or (self.family == H6046EffectUpload.EffectFamily.stream) or (self.family == H6046EffectUpload.EffectFamily.flow) or (self.family == H6046EffectUpload.EffectFamily.chase) or (self.family == H6046EffectUpload.EffectFamily.snow) or (self.family == H6046EffectUpload.EffectFamily.aurora) or (self.family == H6046EffectUpload.EffectFamily.mixed)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.family, None, u"/types/diy_content/seq/0")
            if not self.speed >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.speed, None, u"/types/diy_content/seq/2")
            if not self.speed <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.speed, None, u"/types/diy_content/seq/2")
            _ = self.palette_len
            if not  ((_ >= 3) and (_ <= 24) and (_ % 3 == 0)) :
                raise kaitaistruct.ValidationExprError(self.palette_len, None, u"/types/diy_content/seq/3")
            if len(self.palette) != self.palette_len // 3:
                raise kaitaistruct.ConsistencyError(u"palette", self.palette_len // 3, len(self.palette))
            for i in range(len(self.palette)):
                pass

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                _ = self.mix_bytes
                if not  ((_ <= 8) and (_ % 2 == 0)) :
                    raise kaitaistruct.ValidationExprError(self.mix_bytes, None, u"/types/diy_content/seq/5")

            if self.family == H6046EffectUpload.EffectFamily.mixed:
                pass
                if len(self.pairs) != self.mix_bytes // 2:
                    raise kaitaistruct.ConsistencyError(u"pairs", self.mix_bytes // 2, len(self.pairs))
                for i in range(len(self.pairs)):
                    pass
                    if self.pairs[i]._root != self._root:
                        raise kaitaistruct.ConsistencyError(u"pairs", self._root, self.pairs[i]._root)
                    if self.pairs[i]._parent != self:
                        raise kaitaistruct.ConsistencyError(u"pairs", self, self.pairs[i]._parent)


            self._dirty = False

        @property
        def default_speed(self):
            if hasattr(self, '_m_default_speed'):
                return self._m_default_speed

            self._m_default_speed = 50
            return getattr(self, '_m_default_speed', None)

        def _invalidate_default_speed(self):
            del self._m_default_speed

    class EffectPair(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046EffectUpload.EffectPair, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.family = KaitaiStream.resolve_enum(H6046EffectUpload.EffectFamily, self._io.read_u1())
            if not  ((self.family == H6046EffectUpload.EffectFamily.fade) or (self.family == H6046EffectUpload.EffectFamily.jumping) or (self.family == H6046EffectUpload.EffectFamily.twinkle) or (self.family == H6046EffectUpload.EffectFamily.breathing) or (self.family == H6046EffectUpload.EffectFamily.stream) or (self.family == H6046EffectUpload.EffectFamily.flow) or (self.family == H6046EffectUpload.EffectFamily.chase) or (self.family == H6046EffectUpload.EffectFamily.snow) or (self.family == H6046EffectUpload.EffectFamily.aurora)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.family, self._io, u"/types/effect_pair/seq/0")
            self.variant = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046EffectUpload.EffectPair, self)._write__seq(io)
            self._io.write_u1(int(self.family))
            self._io.write_u1(self.variant)


        def _check(self):
            if not  ((self.family == H6046EffectUpload.EffectFamily.fade) or (self.family == H6046EffectUpload.EffectFamily.jumping) or (self.family == H6046EffectUpload.EffectFamily.twinkle) or (self.family == H6046EffectUpload.EffectFamily.breathing) or (self.family == H6046EffectUpload.EffectFamily.stream) or (self.family == H6046EffectUpload.EffectFamily.flow) or (self.family == H6046EffectUpload.EffectFamily.chase) or (self.family == H6046EffectUpload.EffectFamily.snow) or (self.family == H6046EffectUpload.EffectFamily.aurora)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.family, None, u"/types/effect_pair/seq/0")
            self._dirty = False


    class SceneContent(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046EffectUpload.SceneContent, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_blocks = self._io.read_u1()
            self.blocks = []
            for i in range(self.num_blocks):
                _t_blocks = H6046EffectUpload.Block(self._io, self, self._root)
                try:
                    _t_blocks._read()
                finally:
                    self.blocks.append(_t_blocks)

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.blocks)):
                pass
                self.blocks[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H6046EffectUpload.SceneContent, self)._write__seq(io)
            self._io.write_u1(self.num_blocks)
            for i in range(len(self.blocks)):
                pass
                self.blocks[i]._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.blocks) != self.num_blocks:
                raise kaitaistruct.ConsistencyError(u"blocks", self.num_blocks, len(self.blocks))
            for i in range(len(self.blocks)):
                pass
                if self.blocks[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"blocks", self._root, self.blocks[i]._root)
                if self.blocks[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"blocks", self, self.blocks[i]._parent)

            self._dirty = False



