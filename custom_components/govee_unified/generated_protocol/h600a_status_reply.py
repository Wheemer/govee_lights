# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H600aStatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H600A support request #492, owner confirmations #494.
    Compatibility hypothesis: AA0501 queries return mode 0D direct RGB,
    big-endian Kelvin and companion RGB, or 16-bit little-endian scene/DIY
    selection. Shared power, percentage brightness and version domains
    describe the remaining basic state. Unknown modes, domains, hardware
    prefix and tails remain opaque. Response availability, identity encoding
    across revisions, encryption and physical behaviour remain unqualified.
    No attributable official-app BLE capture is available.
    """

    class AaDomain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
        firmware = 6
        hardware = 7

    class ColorMode(IntEnum):
        scene = 4
        diy = 10
        static_colour = 13
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H600aStatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H600aStatusReply.AaDomain, self._io.read_u1())
        _on = self.domain
        if _on == H600aStatusReply.AaDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H600aStatusReply.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H600aStatusReply.AaDomain.colour_mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H600aStatusReply.ColourModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H600aStatusReply.AaDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H600aStatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H600aStatusReply.AaDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H600aStatusReply.HardwareBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H600aStatusReply.AaDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H600aStatusReply.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H600aStatusReply.AaDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H600aStatusReply.AaDomain.colour_mode:
            pass
            self.body._fetch_instances()
        elif _on == H600aStatusReply.AaDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H600aStatusReply.AaDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H600aStatusReply.AaDomain.power:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H600aStatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H600aStatusReply.AaDomain.brightness:
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
        elif _on == H600aStatusReply.AaDomain.colour_mode:
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
        elif _on == H600aStatusReply.AaDomain.firmware:
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
        elif _on == H600aStatusReply.AaDomain.hardware:
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
        elif _on == H600aStatusReply.AaDomain.power:
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
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, None, u"/seq/0")
        _on = self.domain
        if _on == H600aStatusReply.AaDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H600aStatusReply.AaDomain.colour_mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H600aStatusReply.AaDomain.firmware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H600aStatusReply.AaDomain.hardware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H600aStatusReply.AaDomain.power:
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
            super(H600aStatusReply.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColourModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.ColourModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H600aStatusReply.ColorMode, self._io.read_u1())
            _on = self.mode
            if _on == H600aStatusReply.ColorMode.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H600aStatusReply.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H600aStatusReply.ColorMode.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H600aStatusReply.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H600aStatusReply.ColorMode.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H600aStatusReply.StaticColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H600aStatusReply.ColorMode.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H600aStatusReply.ColorMode.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H600aStatusReply.ColorMode.static_colour:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.ColourModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H600aStatusReply.ColorMode.diy:
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
            elif _on == H600aStatusReply.ColorMode.scene:
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
            elif _on == H600aStatusReply.ColorMode.static_colour:
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
            _on = self.mode
            if _on == H600aStatusReply.ColorMode.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H600aStatusReply.ColorMode.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H600aStatusReply.ColorMode.static_colour:
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


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class HardwareBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.HardwareBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown_prefix = self._io.read_u1()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.HardwareBody, self)._write__seq(io)
            self._io.write_u1(self.unknown_prefix)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class StaticColourBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.StaticColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.kelvin = self._io.read_u2be()
            self.companion_rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.companion_rgb._read()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()
            self.companion_rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H600aStatusReply.StaticColourBody, self)._write__seq(io)
            self.rgb._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.companion_rgb._write__seq(self._io)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class VersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H600aStatusReply.VersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H600aStatusReply.VersionBody, self)._write__seq(io)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False



