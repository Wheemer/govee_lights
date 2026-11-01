# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import command_write
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6072CommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6072, owner confirmations #486.
    Compatibility hypothesis: basic controls, scenes, DIY selection and newer
    static bodies share the common envelope. Legacy static selector 14 places
    its eight-zone mask after an unknown byte; newer selector 15 uses the
    shared static operations. Product revision admission is independent.
    Exact-model captures, unused bytes, rendering and ACK timing are unqualified.
    """

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        multi = 5
        multi_effect = 163

    class MultiSub(IntEnum):
        scene = 4
        diy = 10
        legacy_static = 20
        static = 21
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6072CommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6072CommandWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H6072CommandWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = command_write.CommandWrite.BrightnessCmd(_io__raw_body)
            self.body._read()
        elif _on == H6072CommandWrite.CommandOp.multi:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6072CommandWrite.MultiCmd(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6072CommandWrite.CommandOp.multi_effect:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = command_write.CommandWrite.MultiEffectCmd(_io__raw_body)
            self.body._read()
        elif _on == H6072CommandWrite.CommandOp.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = command_write.CommandWrite.PowerCmd(_io__raw_body)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6072CommandWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6072CommandWrite.CommandOp.multi:
            pass
            self.body._fetch_instances()
        elif _on == H6072CommandWrite.CommandOp.multi_effect:
            pass
            self.body._fetch_instances()
        elif _on == H6072CommandWrite.CommandOp.power:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6072CommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6072CommandWrite.CommandOp.brightness:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(17)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (17))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 17:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 17, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        elif _on == H6072CommandWrite.CommandOp.multi:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(17)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (17))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 17:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 17, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        elif _on == H6072CommandWrite.CommandOp.multi_effect:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(17)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (17))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 17:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 17, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        elif _on == H6072CommandWrite.CommandOp.power:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(17)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (17))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 17:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 17, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        else:
            pass
            self._io.write_bytes(self.body)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        _on = self.opcode
        if _on == H6072CommandWrite.CommandOp.brightness:
            pass
        elif _on == H6072CommandWrite.CommandOp.multi:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6072CommandWrite.CommandOp.multi_effect:
            pass
        elif _on == H6072CommandWrite.CommandOp.power:
            pass
        else:
            pass
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class LegacyColour(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072CommandWrite.LegacyColour, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb_direct = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_direct._read()
            self.kelvin = self._io.read_u2be()
            self.rgb_preview = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_preview._read()
            self.unknown = self._io.read_u1()
            self.mask = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb_direct._fetch_instances()
            self.rgb_preview._fetch_instances()


        def _write__seq(self, io=None):
            super(H6072CommandWrite.LegacyColour, self)._write__seq(io)
            self.rgb_direct._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.rgb_preview._write__seq(self._io)
            self._io.write_u1(self.unknown)
            self._io.write_u1(self.mask)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class MultiCmd(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6072CommandWrite.MultiCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = KaitaiStream.resolve_enum(H6072CommandWrite.MultiSub, self._io.read_u1())
            _on = self.sub
            if _on == H6072CommandWrite.MultiSub.diy:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = govee_common.GoveeCommon.DiySelector(_io__raw_sub_body)
                self.sub_body._read()
            elif _on == H6072CommandWrite.MultiSub.legacy_static:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H6072CommandWrite.LegacyColour(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            elif _on == H6072CommandWrite.MultiSub.scene:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = command_write.CommandWrite.SceneActivate(_io__raw_sub_body)
                self.sub_body._read()
            elif _on == H6072CommandWrite.MultiSub.static:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = command_write.CommandWrite.StaticCmd(_io__raw_sub_body)
                self.sub_body._read()
            else:
                pass
                self.sub_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub
            if _on == H6072CommandWrite.MultiSub.diy:
                pass
                self.sub_body._fetch_instances()
            elif _on == H6072CommandWrite.MultiSub.legacy_static:
                pass
                self.sub_body._fetch_instances()
            elif _on == H6072CommandWrite.MultiSub.scene:
                pass
                self.sub_body._fetch_instances()
            elif _on == H6072CommandWrite.MultiSub.static:
                pass
                self.sub_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6072CommandWrite.MultiCmd, self)._write__seq(io)
            self._io.write_u1(int(self.sub))
            _on = self.sub
            if _on == H6072CommandWrite.MultiSub.diy:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            elif _on == H6072CommandWrite.MultiSub.legacy_static:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            elif _on == H6072CommandWrite.MultiSub.scene:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            elif _on == H6072CommandWrite.MultiSub.static:
                pass
                _io__raw_sub_body = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_sub_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_sub_body=_io__raw_sub_body):
                    self._raw_sub_body = _io__raw_sub_body.to_byte_array()
                    if len(self._raw_sub_body) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(sub_body)", 16, len(self._raw_sub_body))
                    parent.write_bytes(self._raw_sub_body)
                _io__raw_sub_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.sub_body._write__seq(_io__raw_sub_body)
            else:
                pass
                self._io.write_bytes(self.sub_body)


        def _check(self):
            _on = self.sub
            if _on == H6072CommandWrite.MultiSub.diy:
                pass
            elif _on == H6072CommandWrite.MultiSub.legacy_static:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            elif _on == H6072CommandWrite.MultiSub.scene:
                pass
            elif _on == H6072CommandWrite.MultiSub.static:
                pass
            else:
                pass
                if len(self.sub_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"sub_body", 16, len(self.sub_body))
            self._dirty = False


    @property
    def is_static(self):
        if hasattr(self, '_m_is_static'):
            return self._m_is_static

        self._m_is_static =  ((self.opcode == H6072CommandWrite.CommandOp.multi) and ( ((self.body.sub == H6072CommandWrite.MultiSub.static) or (self.body.sub == H6072CommandWrite.MultiSub.legacy_static)) )) 
        return getattr(self, '_m_is_static', None)

    def _invalidate_is_static(self):
        del self._m_is_static

