# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import diy_type03
from custom_components.govee_unified.generated_protocol import diy_type04
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099EffectUpload(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 catalogue upload hypothesis for issue #258.  Android 7.6.01
    H6099 scene handling uploads type-1 and type-2 A3 bodies before activating a
    little-endian scene selector.  Exact-SKU catalogue parameters fit the shared
    type-1 and layered structures.  Physical upload, activation, and restoration
    remain unqualified.  Goods type 191 also uploads shared type-04 Basic/Mixed
    bodies (without an FE prefix) and type-03 Graffiti bodies, then activates
    ordinary 0x0a DIY with default code 254.  Graffiti indices address physical
    ICs, not the 14 logical segments.  This does not authorise arbitrary Advanced
    or Workshop carriers.  Exact physical topology and visible behaviour still
    require owner qualification.
    H6097 issue #431 independently shares type-1/type-2 scenes and type-03/type-04
    DIY bodies with default selector 254, its own family bounds and 24 physical
    ICs.  Its selector-only native scenes do not upload a type-0 body.
    """

    class BodyKind(IntEnum):
        builtin_parameters = 1
        scene = 2
        painted = 3
        basic = 4
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099EffectUpload, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._should_write_diy = False
        self.diy__enabled = True

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x01", self.header, self._io, u"/seq/0")
        self.chunk_count = self._io.read_u1()
        self.kind = KaitaiStream.resolve_enum(H6099EffectUpload.BodyKind, self._io.read_u1())
        if not  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene) or (self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.kind, self._io, u"/seq/2")
        if  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene)) :
            pass
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.builtin_parameters:
                pass
                self.content = govee_shared.GoveeShared.SceneType1Content(self._io)
                self.content._read()
            elif _on == H6099EffectUpload.BodyKind.scene:
                pass
                self.content = H6099EffectUpload.SceneContent(self._io, self, self._root)
                self.content._read()

        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass
            self.diy_bytes = self._io.read_bytes_full()

        self._dirty = False


    def _fetch_instances(self):
        pass
        if  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene)) :
            pass
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.builtin_parameters:
                pass
                self.content._fetch_instances()
            elif _on == H6099EffectUpload.BodyKind.scene:
                pass
                self.content._fetch_instances()

        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass

        _ = self.diy
        if hasattr(self, '_m_diy'):
            pass
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.basic:
                pass
                self._m_diy._fetch_instances()
            elif _on == H6099EffectUpload.BodyKind.painted:
                pass
                self._m_diy._fetch_instances()



    def _write__seq(self, io=None):
        super(H6099EffectUpload, self)._write__seq(io)
        self._should_write_diy = self.diy__enabled
        self._io.write_bytes(self.header)
        self._io.write_u1(self.chunk_count)
        self._io.write_u1(int(self.kind))
        if  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene)) :
            pass
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.builtin_parameters:
                pass
                self.content._write__seq(self._io)
            elif _on == H6099EffectUpload.BodyKind.scene:
                pass
                self.content._write__seq(self._io)

        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass
            self._io.write_bytes(self.diy_bytes)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"diy_bytes", 0, self._io.size() - self._io.pos())



    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x01", self.header, None, u"/seq/0")
        if not  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene) or (self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.kind, None, u"/seq/2")
        if  ((self.kind == H6099EffectUpload.BodyKind.builtin_parameters) or (self.kind == H6099EffectUpload.BodyKind.scene)) :
            pass
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.builtin_parameters:
                pass
            elif _on == H6099EffectUpload.BodyKind.scene:
                pass
                if self.content._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"content", self._root, self.content._root)
                if self.content._parent != self:
                    raise kaitaistruct.ConsistencyError(u"content", self, self.content._parent)

        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass

        if self.diy__enabled:
            pass
            if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
                pass
                _on = self.kind
                if _on == H6099EffectUpload.BodyKind.basic:
                    pass
                elif _on == H6099EffectUpload.BodyKind.painted:
                    pass


        self._dirty = False

    class Block(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099EffectUpload.Block, self).__init__(_io)
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
            super(H6099EffectUpload.Block, self)._write__seq(io)
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


    class SceneContent(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099EffectUpload.SceneContent, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_blocks = self._io.read_u1()
            self.blocks = []
            for i in range(self.num_blocks):
                _t_blocks = H6099EffectUpload.Block(self._io, self, self._root)
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
            super(H6099EffectUpload.SceneContent, self)._write__seq(io)
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


    @property
    def diy(self):
        if self._should_write_diy:
            self._write_diy()
        if hasattr(self, '_m_diy'):
            return self._m_diy

        if not self.diy__enabled:
            return None

        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass
            _pos = self._io.pos()
            self._io.seek(0)
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.basic:
                pass
                self._m_diy = diy_type04.DiyType04(self._io)
                self._m_diy._read()
            elif _on == H6099EffectUpload.BodyKind.painted:
                pass
                self._m_diy = diy_type03.DiyType03(self._io)
                self._m_diy._read()
            self._io.seek(_pos)

        return getattr(self, '_m_diy', None)

    @diy.setter
    def diy(self, v):
        self._dirty = True
        self._m_diy = v

    def _write_diy(self):
        self._should_write_diy = False
        if  ((self.kind == H6099EffectUpload.BodyKind.painted) or (self.kind == H6099EffectUpload.BodyKind.basic)) :
            pass
            _pos = self._io.pos()
            self._io.seek(0)
            _on = self.kind
            if _on == H6099EffectUpload.BodyKind.basic:
                pass
                self._m_diy._write__seq(self._io)
            elif _on == H6099EffectUpload.BodyKind.painted:
                pass
                self._m_diy._write__seq(self._io)
            self._io.seek(_pos)



