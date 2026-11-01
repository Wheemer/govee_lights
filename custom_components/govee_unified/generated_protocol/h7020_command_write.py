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

class H7020CommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H7020, support PR #363. Candidate commands use the shared
    20-byte envelope, with four-byte masks for up to two fifteen-bulb strings.
    Colour temperature uses white direct RGB and a table-derived companion.
    The configured string count is not physical attachment detection.
    Unresolved assumptions: exact-model captures have not qualified mask width,
    colour appearance, count changes, music parameters, upload activation or ACK
    timing. Unknown suffixes are retained without inferred padding constraints.
    A3/02 layered and A3/04 basic/mixed bodies reuse the shared effect schemas;
    both DIY families activate with a separate DIY slot, not the body effect ID.
    """

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        multi = 5
        configured_strings = 15
        power_off_memory = 65

    class MultiSub(IntEnum):
        scene = 4
        diy = 10
        music = 19
        static = 21

    class MusicMode(IntEnum):
        rhythm = 3
        spectrum = 4
        energetic = 5
        rolling = 6
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H7020CommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H7020CommandWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H7020CommandWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = command_write.CommandWrite.BrightnessCmd(_io__raw_body)
            self.body._read()
        elif _on == H7020CommandWrite.CommandOp.configured_strings:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H7020CommandWrite.ConfiguredStringsCmd(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H7020CommandWrite.CommandOp.multi:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H7020CommandWrite.MultiCmd(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H7020CommandWrite.CommandOp.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = command_write.CommandWrite.PowerCmd(_io__raw_body)
            self.body._read()
        elif _on == H7020CommandWrite.CommandOp.power_off_memory:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H7020CommandWrite.BooleanCmd(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H7020CommandWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H7020CommandWrite.CommandOp.configured_strings:
            pass
            self.body._fetch_instances()
        elif _on == H7020CommandWrite.CommandOp.multi:
            pass
            self.body._fetch_instances()
        elif _on == H7020CommandWrite.CommandOp.power:
            pass
            self.body._fetch_instances()
        elif _on == H7020CommandWrite.CommandOp.power_off_memory:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H7020CommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H7020CommandWrite.CommandOp.brightness:
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
        elif _on == H7020CommandWrite.CommandOp.configured_strings:
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
        elif _on == H7020CommandWrite.CommandOp.multi:
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
        elif _on == H7020CommandWrite.CommandOp.power:
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
        elif _on == H7020CommandWrite.CommandOp.power_off_memory:
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
        if _on == H7020CommandWrite.CommandOp.brightness:
            pass
        elif _on == H7020CommandWrite.CommandOp.configured_strings:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H7020CommandWrite.CommandOp.multi:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H7020CommandWrite.CommandOp.power:
            pass
        elif _on == H7020CommandWrite.CommandOp.power_off_memory:
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

    class BooleanCmd(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.BooleanCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.flag = self._io.read_u1()
            if not  ((self.flag == 0) or (self.flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.flag, self._io, u"/types/boolean_cmd/seq/0")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7020CommandWrite.BooleanCmd, self)._write__seq(io)
            self._io.write_u1(self.flag)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not  ((self.flag == 0) or (self.flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.flag, None, u"/types/boolean_cmd/seq/0")
            self._dirty = False


    class ConfiguredStringsCmd(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.ConfiguredStringsCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.count = self._io.read_u1()
            if not  ((self.count == 1) or (self.count == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.count, self._io, u"/types/configured_strings_cmd/seq/0")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7020CommandWrite.ConfiguredStringsCmd, self)._write__seq(io)
            self._io.write_u1(self.count)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not  ((self.count == 1) or (self.count == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.count, None, u"/types/configured_strings_cmd/seq/0")
            self._dirty = False


    class MultiCmd(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.MultiCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = KaitaiStream.resolve_enum(H7020CommandWrite.MultiSub, self._io.read_u1())
            _on = self.sub
            if _on == H7020CommandWrite.MultiSub.diy:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = govee_common.GoveeCommon.DiySelector(_io__raw_sub_body)
                self.sub_body._read()
            elif _on == H7020CommandWrite.MultiSub.music:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H7020CommandWrite.MusicSelector(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            elif _on == H7020CommandWrite.MultiSub.scene:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = command_write.CommandWrite.SceneActivate(_io__raw_sub_body)
                self.sub_body._read()
            elif _on == H7020CommandWrite.MultiSub.static:
                pass
                self._raw_sub_body = self._io.read_bytes(16)
                _io__raw_sub_body = KaitaiStream(BytesIO(self._raw_sub_body))
                self.sub_body = H7020CommandWrite.StaticCmd(_io__raw_sub_body, self, self._root)
                self.sub_body._read()
            else:
                pass
                self.sub_body = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub
            if _on == H7020CommandWrite.MultiSub.diy:
                pass
                self.sub_body._fetch_instances()
            elif _on == H7020CommandWrite.MultiSub.music:
                pass
                self.sub_body._fetch_instances()
            elif _on == H7020CommandWrite.MultiSub.scene:
                pass
                self.sub_body._fetch_instances()
            elif _on == H7020CommandWrite.MultiSub.static:
                pass
                self.sub_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H7020CommandWrite.MultiCmd, self)._write__seq(io)
            self._io.write_u1(int(self.sub))
            _on = self.sub
            if _on == H7020CommandWrite.MultiSub.diy:
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
            elif _on == H7020CommandWrite.MultiSub.music:
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
            elif _on == H7020CommandWrite.MultiSub.scene:
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
            elif _on == H7020CommandWrite.MultiSub.static:
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
            if _on == H7020CommandWrite.MultiSub.diy:
                pass
            elif _on == H7020CommandWrite.MultiSub.music:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            elif _on == H7020CommandWrite.MultiSub.scene:
                pass
            elif _on == H7020CommandWrite.MultiSub.static:
                pass
                if self.sub_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self._root, self.sub_body._root)
                if self.sub_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"sub_body", self, self.sub_body._parent)
            else:
                pass
                if len(self.sub_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"sub_body", 16, len(self.sub_body))
            self._dirty = False


    class MusicSelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.MusicSelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode_id = KaitaiStream.resolve_enum(H7020CommandWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            self.rhythm_response = self._io.read_u1()
            self.has_fixed_colour = self._io.read_u1()
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H7020CommandWrite.MusicSelector, self)._write__seq(io)
            self._io.write_u1(int(self.mode_id))
            self._io.write_u1(self.sensitivity)
            self._io.write_u1(self.rhythm_response)
            self._io.write_u1(self.has_fixed_colour)
            self.rgb._write__seq(self._io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SegmentMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.SegmentMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bits = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7020CommandWrite.SegmentMask, self)._write__seq(io)
            self._io.write_u4le(self.bits)


        def _check(self):
            self._dirty = False


    class StaticBrightness(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.StaticBrightness, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, self._io, u"/types/static_brightness/seq/0")
            self.mask = H7020CommandWrite.SegmentMask(self._io, self, self._root)
            self.mask._read()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.mask._fetch_instances()


        def _write__seq(self, io=None):
            super(H7020CommandWrite.StaticBrightness, self)._write__seq(io)
            self._io.write_u1(self.percent)
            self.mask._write__seq(self._io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, None, u"/types/static_brightness/seq/0")
            if self.mask._root != self._root:
                raise kaitaistruct.ConsistencyError(u"mask", self._root, self.mask._root)
            if self.mask._parent != self:
                raise kaitaistruct.ConsistencyError(u"mask", self, self.mask._parent)
            self._dirty = False


    class StaticCmd(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.StaticCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.static_sub = self._io.read_u1()
            _on = self.static_sub
            if _on == 1:
                pass
                self._raw_static_body = self._io.read_bytes(15)
                _io__raw_static_body = KaitaiStream(BytesIO(self._raw_static_body))
                self.static_body = H7020CommandWrite.StaticColor(_io__raw_static_body, self, self._root)
                self.static_body._read()
            elif _on == 2:
                pass
                self._raw_static_body = self._io.read_bytes(15)
                _io__raw_static_body = KaitaiStream(BytesIO(self._raw_static_body))
                self.static_body = H7020CommandWrite.StaticBrightness(_io__raw_static_body, self, self._root)
                self.static_body._read()
            else:
                pass
                self.static_body = self._io.read_bytes(15)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.static_sub
            if _on == 1:
                pass
                self.static_body._fetch_instances()
            elif _on == 2:
                pass
                self.static_body._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H7020CommandWrite.StaticCmd, self)._write__seq(io)
            self._io.write_u1(self.static_sub)
            _on = self.static_sub
            if _on == 1:
                pass
                _io__raw_static_body = KaitaiStream(BytesIO(bytearray(15)))
                self._io.add_child_stream(_io__raw_static_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (15))
                def handler(parent, _io__raw_static_body=_io__raw_static_body):
                    self._raw_static_body = _io__raw_static_body.to_byte_array()
                    if len(self._raw_static_body) != 15:
                        raise kaitaistruct.ConsistencyError(u"raw(static_body)", 15, len(self._raw_static_body))
                    parent.write_bytes(self._raw_static_body)
                _io__raw_static_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.static_body._write__seq(_io__raw_static_body)
            elif _on == 2:
                pass
                _io__raw_static_body = KaitaiStream(BytesIO(bytearray(15)))
                self._io.add_child_stream(_io__raw_static_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (15))
                def handler(parent, _io__raw_static_body=_io__raw_static_body):
                    self._raw_static_body = _io__raw_static_body.to_byte_array()
                    if len(self._raw_static_body) != 15:
                        raise kaitaistruct.ConsistencyError(u"raw(static_body)", 15, len(self._raw_static_body))
                    parent.write_bytes(self._raw_static_body)
                _io__raw_static_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.static_body._write__seq(_io__raw_static_body)
            else:
                pass
                self._io.write_bytes(self.static_body)


        def _check(self):
            _on = self.static_sub
            if _on == 1:
                pass
                if self.static_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"static_body", self._root, self.static_body._root)
                if self.static_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"static_body", self, self.static_body._parent)
            elif _on == 2:
                pass
                if self.static_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"static_body", self._root, self.static_body._root)
                if self.static_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"static_body", self, self.static_body._parent)
            else:
                pass
                if len(self.static_body) != 15:
                    raise kaitaistruct.ConsistencyError(u"static_body", 15, len(self.static_body))
            self._dirty = False


    class StaticColor(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7020CommandWrite.StaticColor, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb_direct = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_direct._read()
            self.kelvin = self._io.read_u2be()
            self.rgb_preview = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb_preview._read()
            self.mask = H7020CommandWrite.SegmentMask(self._io, self, self._root)
            self.mask._read()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb_direct._fetch_instances()
            self.rgb_preview._fetch_instances()
            self.mask._fetch_instances()


        def _write__seq(self, io=None):
            super(H7020CommandWrite.StaticColor, self)._write__seq(io)
            self.rgb_direct._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.rgb_preview._write__seq(self._io)
            self.mask._write__seq(self._io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.mask._root != self._root:
                raise kaitaistruct.ConsistencyError(u"mask", self._root, self.mask._root)
            if self.mask._parent != self:
                raise kaitaistruct.ConsistencyError(u"mask", self, self.mask._parent)
            self._dirty = False


    @property
    def is_static(self):
        if hasattr(self, '_m_is_static'):
            return self._m_is_static

        self._m_is_static =  ((self.opcode == H7020CommandWrite.CommandOp.multi) and (self.body.sub == H7020CommandWrite.MultiSub.static) and ( ((self.body.sub_body.static_sub == 1) or (self.body.sub_body.static_sub == 2)) )) 
        return getattr(self, '_m_is_static', None)

    def _invalidate_is_static(self):
        del self._m_is_static

