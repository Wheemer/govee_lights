# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H601cCommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H601C support request (#329, #403).  H601C uses mode 0D with
    direct RGB, big-endian Kelvin, and companion RGB; mode 04 with a 16-bit
    little-endian scene selector; and mode 0A with a 16-bit little-endian DIY
    selector.  Explicit Kelvin uses direct FFFFFF and the first ordered entry
    from the shared Kelvin-to-RGB table.  Shared single-frame commands supply 01
    power and 04 brightness, zero-padded to 19 bytes with an XOR checksum.
    Compatibility hypothesis: all identifiable H601C revisions use this command
    format, independently of Matter configuration.  This is the logical frame;
    encryption selection, physical scene/DIY acceptance, revision differences,
    and reply availability remain unqualified.  No official-app BLE captures supplied.
    """

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        mode = 5

    class ModeSel(IntEnum):
        scene = 4
        diy = 10
        static_colour = 13
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H601cCommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H601cCommandWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H601cCommandWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H601cCommandWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H601cCommandWrite.CommandOp.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H601cCommandWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H601cCommandWrite.CommandOp.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H601cCommandWrite.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H601cCommandWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H601cCommandWrite.CommandOp.mode:
            pass
            self.body._fetch_instances()
        elif _on == H601cCommandWrite.CommandOp.power:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H601cCommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H601cCommandWrite.CommandOp.brightness:
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
        elif _on == H601cCommandWrite.CommandOp.mode:
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
        elif _on == H601cCommandWrite.CommandOp.power:
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
        if _on == H601cCommandWrite.CommandOp.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H601cCommandWrite.CommandOp.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H601cCommandWrite.CommandOp.power:
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
            super(H601cCommandWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, self._io, u"/types/brightness_body/seq/0")
            self.padding = self._io.read_bytes(16)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/brightness_body/seq/1")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H601cCommandWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)
            self._io.write_bytes(self.padding)


        def _check(self):
            if not self.percent <= 100:
                raise kaitaistruct.ValidationGreaterThanError(100, self.percent, None, u"/types/brightness_body/seq/0")
            if len(self.padding) != 16:
                raise kaitaistruct.ConsistencyError(u"padding", 16, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/brightness_body/seq/1")
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H601cCommandWrite.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.padding = self._io.read_bytes(14)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/diy_body/seq/1")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H601cCommandWrite.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.padding)


        def _check(self):
            if len(self.padding) != 14:
                raise kaitaistruct.ConsistencyError(u"padding", 14, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/diy_body/seq/1")
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H601cCommandWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub_mode = KaitaiStream.resolve_enum(H601cCommandWrite.ModeSel, self._io.read_u1())
            _on = self.sub_mode
            if _on == H601cCommandWrite.ModeSel.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H601cCommandWrite.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H601cCommandWrite.ModeSel.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H601cCommandWrite.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H601cCommandWrite.ModeSel.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H601cCommandWrite.StaticColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub_mode
            if _on == H601cCommandWrite.ModeSel.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H601cCommandWrite.ModeSel.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H601cCommandWrite.ModeSel.static_colour:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H601cCommandWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.sub_mode))
            _on = self.sub_mode
            if _on == H601cCommandWrite.ModeSel.diy:
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
            elif _on == H601cCommandWrite.ModeSel.scene:
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
            elif _on == H601cCommandWrite.ModeSel.static_colour:
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
            if _on == H601cCommandWrite.ModeSel.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H601cCommandWrite.ModeSel.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H601cCommandWrite.ModeSel.static_colour:
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


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H601cCommandWrite.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            if not  ((self.is_on == 0) or (self.is_on == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_on, self._io, u"/types/power_body/seq/0")
            self.padding = self._io.read_bytes(16)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/power_body/seq/1")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H601cCommandWrite.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.padding)


        def _check(self):
            if not  ((self.is_on == 0) or (self.is_on == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_on, None, u"/types/power_body/seq/0")
            if len(self.padding) != 16:
                raise kaitaistruct.ConsistencyError(u"padding", 16, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/power_body/seq/1")
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H601cCommandWrite.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.padding = self._io.read_bytes(14)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/scene_body/seq/1")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H601cCommandWrite.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.padding)


        def _check(self):
            if len(self.padding) != 14:
                raise kaitaistruct.ConsistencyError(u"padding", 14, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/scene_body/seq/1")
            self._dirty = False


    class StaticColourBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H601cCommandWrite.StaticColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.kelvin = self._io.read_u2be()
            self.companion_rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.companion_rgb._read()
            self.padding = self._io.read_bytes(8)
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/static_colour_body/seq/3")
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()
            self.companion_rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H601cCommandWrite.StaticColourBody, self)._write__seq(io)
            self.rgb._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.companion_rgb._write__seq(self._io)
            self._io.write_bytes(self.padding)


        def _check(self):
            if len(self.padding) != 8:
                raise kaitaistruct.ConsistencyError(u"padding", 8, len(self.padding))
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, None, u"/types/static_colour_body/seq/3")
            self._dirty = False


    @property
    def is_static(self):
        if hasattr(self, '_m_is_static'):
            return self._m_is_static

        self._m_is_static =  ((self.opcode == H601cCommandWrite.CommandOp.mode) and (self.body.sub_mode == H601cCommandWrite.ModeSel.static_colour)) 
        return getattr(self, '_m_is_static', None)

    def _invalidate_is_static(self):
        del self._m_is_static

