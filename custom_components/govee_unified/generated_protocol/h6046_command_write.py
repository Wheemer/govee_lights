# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6046CommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE (audited prospective) H6046, support issue #479.
    Evidence class: exact-model behavioural audit and source-reconstructed bytes,
    not official-app captures or owner qualification. Known Pact 1/1 and 2/1 use
    this modern layout; no H6053 legacy range or firmware gate is assumed.
    Each frame is 20 bytes, with XOR of bytes 0..18 in the final byte; the
    transport validates that checksum. Ten segments comprise five per bar.
    Unresolved assumptions: other Pact/revision combinations, opaque suffixes,
    timing and physical rendering, including differences between RGBIC/RGBWIC
    revisions. Unknown bytes have no zero-only validation.
    """

    class BarFlag(IntEnum):
        left = 1
        right = 16

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        bar_enable = 51
        swap_bars = 52

    class ModeSel(IntEnum):
        scene = 4
        diy = 10
        music = 19
        static_colour = 21

    class MusicMode(IntEnum):
        rhythm = 3
        energetic = 5
        impact = 8
        spray = 9
        beat = 73
        torch = 80
        rainbow_ring = 81
        glitter = 82

    class StaticOperation(IntEnum):
        colour = 1
        brightness = 2
        brightness_vector = 3
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6046CommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6046CommandWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H6046CommandWrite.CommandOp.bar_enable:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6046CommandWrite.BarEnableBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6046CommandWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6046CommandWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6046CommandWrite.CommandOp.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6046CommandWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6046CommandWrite.CommandOp.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6046CommandWrite.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6046CommandWrite.CommandOp.swap_bars:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6046CommandWrite.SwapBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6046CommandWrite.CommandOp.bar_enable:
            pass
            self.body._fetch_instances()
        elif _on == H6046CommandWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6046CommandWrite.CommandOp.mode:
            pass
            self.body._fetch_instances()
        elif _on == H6046CommandWrite.CommandOp.power:
            pass
            self.body._fetch_instances()
        elif _on == H6046CommandWrite.CommandOp.swap_bars:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6046CommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6046CommandWrite.CommandOp.bar_enable:
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
        elif _on == H6046CommandWrite.CommandOp.brightness:
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
        elif _on == H6046CommandWrite.CommandOp.mode:
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
        elif _on == H6046CommandWrite.CommandOp.power:
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
        elif _on == H6046CommandWrite.CommandOp.swap_bars:
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
        if _on == H6046CommandWrite.CommandOp.bar_enable:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6046CommandWrite.CommandOp.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6046CommandWrite.CommandOp.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6046CommandWrite.CommandOp.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6046CommandWrite.CommandOp.swap_bars:
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

    class BarEnableBody(ReadWriteKaitaiStruct):
        """Both flags are written together, independently of master power.
        Left is bit 0x01 and right is bit 0x10. Other bits remain uninterpreted.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.BarEnableBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mask = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.BarEnableBody, self)._write__seq(io)
            self._io.write_u1(self.mask)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def left_enabled(self):
            if hasattr(self, '_m_left_enabled'):
                return self._m_left_enabled

            self._m_left_enabled = self.mask & 1 != 0
            return getattr(self, '_m_left_enabled', None)

        def _invalidate_left_enabled(self):
            del self._m_left_enabled
        @property
        def right_enabled(self):
            if hasattr(self, '_m_right_enabled'):
                return self._m_right_enabled

            self._m_right_enabled = self.mask & 16 != 0
            return getattr(self, '_m_right_enabled', None)

        def _invalidate_right_enabled(self):
            del self._m_right_enabled

    class BrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, self._io, u"/types/brightness_body/seq/0")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, None, u"/types/brightness_body/seq/0")
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        """Slot selector after an acknowledged DIY upload, not a content read."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub_mode = KaitaiStream.resolve_enum(H6046CommandWrite.ModeSel, self._io.read_u1())
            _on = self.sub_mode
            if _on == H6046CommandWrite.ModeSel.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6046CommandWrite.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6046CommandWrite.ModeSel.music:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6046CommandWrite.MusicBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6046CommandWrite.ModeSel.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6046CommandWrite.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6046CommandWrite.ModeSel.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6046CommandWrite.StaticColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub_mode
            if _on == H6046CommandWrite.ModeSel.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H6046CommandWrite.ModeSel.music:
                pass
                self.detail._fetch_instances()
            elif _on == H6046CommandWrite.ModeSel.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H6046CommandWrite.ModeSel.static_colour:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.sub_mode))
            _on = self.sub_mode
            if _on == H6046CommandWrite.ModeSel.diy:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    if len(self._raw_detail) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 16, len(self._raw_detail))
                    parent.write_bytes(self._raw_detail)
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H6046CommandWrite.ModeSel.music:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    if len(self._raw_detail) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 16, len(self._raw_detail))
                    parent.write_bytes(self._raw_detail)
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H6046CommandWrite.ModeSel.scene:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    if len(self._raw_detail) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 16, len(self._raw_detail))
                    parent.write_bytes(self._raw_detail)
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            elif _on == H6046CommandWrite.ModeSel.static_colour:
                pass
                _io__raw_detail = KaitaiStream(BytesIO(bytearray(16)))
                self._io.add_child_stream(_io__raw_detail)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (16))
                def handler(parent, _io__raw_detail=_io__raw_detail):
                    self._raw_detail = _io__raw_detail.to_byte_array()
                    if len(self._raw_detail) != 16:
                        raise kaitaistruct.ConsistencyError(u"raw(detail)", 16, len(self._raw_detail))
                    parent.write_bytes(self._raw_detail)
                _io__raw_detail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.detail._write__seq(_io__raw_detail)
            else:
                pass
                self._io.write_bytes(self.detail)


        def _check(self):
            _on = self.sub_mode
            if _on == H6046CommandWrite.ModeSel.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6046CommandWrite.ModeSel.music:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6046CommandWrite.ModeSel.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6046CommandWrite.ModeSel.static_colour:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            else:
                pass
                if len(self.detail) != 16:
                    raise kaitaistruct.ConsistencyError(u"detail", 16, len(self.detail))
            self._dirty = False


    class MusicBody(ReadWriteKaitaiStruct):
        """Sensitivity is 0..99. Rhythm alone carries a calm/style byte before the
        fixed-colour flag. For the four base modes a nonzero fixed flag adds
        target mask 0x01/0x10/0x11 and one RGB triple; a zero flag omits them.
        Unequal bar colours require two ordered selector writes.
        Companion-backed modes carry only mode and sensitivity here, after the
        A3/41 upload has succeeded. RX instead carries two RGB triples.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.MusicBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6046CommandWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            if not self.sensitivity <= 99:
                raise kaitaistruct.ValidationGreaterThanError(99, self.sensitivity, self._io, u"/types/music_body/seq/1")
            if self.mode == H6046CommandWrite.MusicMode.rhythm:
                pass
                self.is_calm = self._io.read_u1()

            if self.is_base:
                pass
                self.has_fixed_colour = self._io.read_u1()

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass
                self.bar_mask = self._io.read_u1()

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass
                self.fixed_colour = govee_shared.GoveeShared.Rgb(self._io)
                self.fixed_colour._read()

            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.mode == H6046CommandWrite.MusicMode.rhythm:
                pass

            if self.is_base:
                pass

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass
                self.fixed_colour._fetch_instances()



        def _write__seq(self, io=None):
            super(H6046CommandWrite.MusicBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            self._io.write_u1(self.sensitivity)
            if self.mode == H6046CommandWrite.MusicMode.rhythm:
                pass
                self._io.write_u1(self.is_calm)

            if self.is_base:
                pass
                self._io.write_u1(self.has_fixed_colour)

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass
                self._io.write_u1(self.bar_mask)

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass
                self.fixed_colour._write__seq(self._io)

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not self.sensitivity <= 99:
                raise kaitaistruct.ValidationGreaterThanError(99, self.sensitivity, None, u"/types/music_body/seq/1")
            if self.mode == H6046CommandWrite.MusicMode.rhythm:
                pass

            if self.is_base:
                pass

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass

            if  ((self.is_base) and (self.has_fixed_colour != 0)) :
                pass

            self._dirty = False

        @property
        def is_base(self):
            if hasattr(self, '_m_is_base'):
                return self._m_is_base

            self._m_is_base =  ((self.mode == H6046CommandWrite.MusicMode.rhythm) or (self.mode == H6046CommandWrite.MusicMode.energetic) or (self.mode == H6046CommandWrite.MusicMode.impact) or (self.mode == H6046CommandWrite.MusicMode.spray)) 
            return getattr(self, '_m_is_base', None)

        def _invalidate_is_base(self):
            del self._m_is_base

    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            if not  ((self.is_on == 0) or (self.is_on == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_on, self._io, u"/types/power_body/seq/0")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not  ((self.is_on == 0) or (self.is_on == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_on, None, u"/types/power_body/seq/0")
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        """Little-endian selector, including codes above 255. Uploaded parameters
        must be acknowledged before activation. Readback proves selection only.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class StaticColourBody(ReadWriteKaitaiStruct):
        """RGB with Kelvin zero selects direct RGB. Native white carries big-endian
        Kelvin and a companion RGB preview. Colour and brightness masks are
        little-endian: whole 0x03ff, left 0x001f, right 0x03e0.
        Masked brightness and the complete ten-value brightness vector are
        independent operations. Kelvin candidates span 2000..9000 K; zero is
        not an absent field. Product admission belongs to the exact-SKU profile.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.StaticColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.operation = KaitaiStream.resolve_enum(H6046CommandWrite.StaticOperation, self._io.read_u1())
            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.red = self._io.read_u1()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.green = self._io.read_u1()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.blue = self._io.read_u1()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.kelvin = self._io.read_u2be()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.preview = govee_shared.GoveeShared.Rgb(self._io)
                self.preview._read()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.segment_mask = self._io.read_u2le()

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass
                self.brightness_percent = self._io.read_u1()
                if not self.brightness_percent <= 100:
                    raise kaitaistruct.ValidationGreaterThanError(100, self.brightness_percent, self._io, u"/types/static_colour_body/seq/7")

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass
                self.brightness_segment_mask = self._io.read_u2le()

            if self.operation == H6046CommandWrite.StaticOperation.brightness_vector:
                pass
                self.brightness_values = []
                for i in range(10):
                    self.brightness_values.append(self._io.read_u1())
                    if not self.brightness_values[i] <= 100:
                        raise kaitaistruct.ValidationGreaterThanError(100, self.brightness_values[i], self._io, u"/types/static_colour_body/seq/9")


            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.preview._fetch_instances()

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.brightness_vector:
                pass
                for i in range(len(self.brightness_values)):
                    pass




        def _write__seq(self, io=None):
            super(H6046CommandWrite.StaticColourBody, self)._write__seq(io)
            self._io.write_u1(int(self.operation))
            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.red)

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.green)

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.blue)

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u2be(self.kelvin)

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self.preview._write__seq(self._io)

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u2le(self.segment_mask)

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass
                self._io.write_u1(self.brightness_percent)

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass
                self._io.write_u2le(self.brightness_segment_mask)

            if self.operation == H6046CommandWrite.StaticOperation.brightness_vector:
                pass
                for i in range(len(self.brightness_values)):
                    pass
                    self._io.write_u1(self.brightness_values[i])


            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass
                if not self.brightness_percent <= 100:
                    raise kaitaistruct.ValidationGreaterThanError(100, self.brightness_percent, None, u"/types/static_colour_body/seq/7")

            if self.operation == H6046CommandWrite.StaticOperation.brightness:
                pass

            if self.operation == H6046CommandWrite.StaticOperation.brightness_vector:
                pass
                if len(self.brightness_values) != 10:
                    raise kaitaistruct.ConsistencyError(u"brightness_values", 10, len(self.brightness_values))
                for i in range(len(self.brightness_values)):
                    pass
                    if not self.brightness_values[i] <= 100:
                        raise kaitaistruct.ValidationGreaterThanError(100, self.brightness_values[i], None, u"/types/static_colour_body/seq/9")


            self._dirty = False


    class SwapBody(ReadWriteKaitaiStruct):
        """Empty logical body. The remaining envelope octets are opaque.
        This swaps bar coordinates, not an absolute direction setting.
        Repeating it can undo the first action; an ACK is not position readback.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6046CommandWrite.SwapBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6046CommandWrite.SwapBody, self)._write__seq(io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



