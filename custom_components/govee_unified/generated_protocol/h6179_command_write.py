# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6179CommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6179 compatibility hypothesis: exact-SKU command writes use a
    20-byte 0x33 envelope with the candidate power, brightness, mode, scene, DIY,
    static-colour, music, and boolean current-adaptation layouts below.
    Owner confirmations: #448.  Current adaptation may restart the controller;
    its value must be queried afresh after reconnecting.
    Unresolved assumptions: no exact-model capture verifies the selectors, field
    meanings, brightness scale, optional music colour, opaque tails, or XOR
    checksum byte.
    """

    class CommandOpcode(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        limit = 14

    class ModeSelector(IntEnum):
        legacy_colour = 2
        scene = 4
        diy = 10
        static = 13
        music = 14

    class MusicEffect(IntEnum):
        mode_0 = 0
        mode_1 = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6179CommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6179CommandWrite.CommandOpcode, self._io.read_u1())
        _on = self.opcode
        if _on == H6179CommandWrite.CommandOpcode.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179CommandWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179CommandWrite.CommandOpcode.limit:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179CommandWrite.LimitBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179CommandWrite.CommandOpcode.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179CommandWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179CommandWrite.CommandOpcode.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179CommandWrite.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6179CommandWrite.CommandOpcode.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6179CommandWrite.CommandOpcode.limit:
            pass
            self.body._fetch_instances()
        elif _on == H6179CommandWrite.CommandOpcode.mode:
            pass
            self.body._fetch_instances()
        elif _on == H6179CommandWrite.CommandOpcode.power:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6179CommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6179CommandWrite.CommandOpcode.brightness:
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
        elif _on == H6179CommandWrite.CommandOpcode.limit:
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
        elif _on == H6179CommandWrite.CommandOpcode.mode:
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
        elif _on == H6179CommandWrite.CommandOpcode.power:
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
        if _on == H6179CommandWrite.CommandOpcode.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179CommandWrite.CommandOpcode.limit:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179CommandWrite.CommandOpcode.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179CommandWrite.CommandOpcode.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        else:
            pass
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class BrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.raw = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.raw)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.diy_id = self._io.read_u2le()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.diy_id)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class LegacyColourBody(ReadWriteKaitaiStruct):
        """Unproved whole-device RGB variant retained as structural evidence only."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.LegacyColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.colour = govee_shared.GoveeShared.Rgb(self._io)
            self.colour._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.colour._fetch_instances()


        def _write__seq(self, io=None):
            super(H6179CommandWrite.LegacyColourBody, self)._write__seq(io)
            self.colour._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class LimitBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.LimitBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            if not  ((self.value == 0) or (self.value == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.value, self._io, u"/types/limit_body/seq/0")
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.LimitBody, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not  ((self.value == 0) or (self.value == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.value, None, u"/types/limit_body/seq/0")
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6179CommandWrite.ModeSelector, self._io.read_u1())
            _on = self.mode
            if _on == H6179CommandWrite.ModeSelector.diy:
                pass
                self._raw_payload = self._io.read_bytes(16)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6179CommandWrite.DiyBody(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6179CommandWrite.ModeSelector.legacy_colour:
                pass
                self._raw_payload = self._io.read_bytes(16)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6179CommandWrite.LegacyColourBody(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6179CommandWrite.ModeSelector.music:
                pass
                self._raw_payload = self._io.read_bytes(16)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6179CommandWrite.MusicBody(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6179CommandWrite.ModeSelector.scene:
                pass
                self._raw_payload = self._io.read_bytes(16)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6179CommandWrite.SceneBody(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6179CommandWrite.ModeSelector.static:
                pass
                self._raw_payload = self._io.read_bytes(16)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6179CommandWrite.StaticBody(_io__raw_payload, self, self._root)
                self.payload._read()
            else:
                pass
                self.payload = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H6179CommandWrite.ModeSelector.diy:
                pass
                self.payload._fetch_instances()
            elif _on == H6179CommandWrite.ModeSelector.legacy_colour:
                pass
                self.payload._fetch_instances()
            elif _on == H6179CommandWrite.ModeSelector.music:
                pass
                self.payload._fetch_instances()
            elif _on == H6179CommandWrite.ModeSelector.scene:
                pass
                self.payload._fetch_instances()
            elif _on == H6179CommandWrite.ModeSelector.static:
                pass
                self.payload._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H6179CommandWrite.ModeSelector.diy:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", 16, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6179CommandWrite.ModeSelector.legacy_colour:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", 16, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6179CommandWrite.ModeSelector.music:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", 16, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6179CommandWrite.ModeSelector.scene:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", 16, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6179CommandWrite.ModeSelector.static:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", 16, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            else:
                pass
                self._io.write_bytes(self.payload)


        def _check(self):
            _on = self.mode
            if _on == H6179CommandWrite.ModeSelector.diy:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6179CommandWrite.ModeSelector.legacy_colour:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6179CommandWrite.ModeSelector.music:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6179CommandWrite.ModeSelector.scene:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6179CommandWrite.ModeSelector.static:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            else:
                pass
                if len(self.payload) != 16:
                    raise kaitaistruct.ConsistencyError(u"payload", 16, len(self.payload))
            self._dirty = False


    class MusicBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.MusicBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.effect_id = KaitaiStream.resolve_enum(H6179CommandWrite.MusicEffect, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            self.colour_mode = self._io.read_u1()
            if self.colour_mode != 0:
                pass
                self.fixed_colour = govee_shared.GoveeShared.Rgb(self._io)
                self.fixed_colour._read()

            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.colour_mode != 0:
                pass
                self.fixed_colour._fetch_instances()



        def _write__seq(self, io=None):
            super(H6179CommandWrite.MusicBody, self)._write__seq(io)
            self._io.write_u1(int(self.effect_id))
            self._io.write_u1(self.sensitivity)
            self._io.write_u1(self.colour_mode)
            if self.colour_mode != 0:
                pass
                self.fixed_colour._write__seq(self._io)

            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.colour_mode != 0:
                pass

            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179CommandWrite.SceneBody, self)._write__seq(io)
            self._io.write_u1(self.scene_id)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class StaticBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179CommandWrite.StaticBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb_direct = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_direct._read()
            self.kelvin = self._io.read_u2be()
            self.rgb_preview = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_preview._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb_direct._fetch_instances()
            self.rgb_preview._fetch_instances()


        def _write__seq(self, io=None):
            super(H6179CommandWrite.StaticBody, self)._write__seq(io)
            self.rgb_direct._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.rgb_preview._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



