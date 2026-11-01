# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099CommandWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 command frame for issue #258, checked against Android 7.6.01
    H6099 command behaviour.  Mode 0x15 supplies static colours and segment masks,
    mode 0x00 supplies the six-byte video body, mode 0x0a supplies the
    little-endian DIY selector, and mode 0x13 distinguishes legacy and
    companion-backed music selectors.  Display setting A9 06 writes scalar white
    balance.  This is the logical frame before encryption; owner acceptance,
    firmware differences, and unused bytes remain unqualified.  Installation
    direction writes 33 30 value with candidate values 2, 3, 4, and 5; image
    orientations remain unqualified and no corner names or calibration-display
    commands are implied.
    H6097 issue #431 independently shares these non-music command layouts,
    including fourteen-zone masks and six-byte video.  Its Kelvin producer uses
    direct white RGB and a device-table companion, and its distinct music root
    overrides this envelope's legacy Energetic selector.
    """

    class BlankScreenDetection(IntEnum):
        low_brightness = 1
        same_tone = 2

    class CommandOp(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        installation_direction = 48
        display_setting = 169
        relative_brightness = 174

    class DisplaySetting(IntEnum):
        scalar_white_balance = 6
        blank_screen = 10
        black_border = 11

    class ModeSel(IntEnum):
        video = 0
        scene = 4
        diy = 10
        music = 19
        static_colour = 21

    class MusicMode(IntEnum):
        rhythm = 3
        spectrum = 4
        energetic = 5
        rolling = 6
        bloom = 48
        shiny = 49
        separation = 50
        hopping = 51
        piano_keys = 52
        fountain = 53
        day_and_night = 55

    class StaticOperation(IntEnum):
        colour = 1
        brightness = 2

    class VideoRegion(IntEnum):
        part = 8
        all = 9

    class VideoSource(IntEnum):
        movie = 0
        game = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099CommandWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6099CommandWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H6099CommandWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099CommandWrite.CommandOp.display_setting:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.DisplaySettingBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099CommandWrite.CommandOp.installation_direction:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.InstallationDirectionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099CommandWrite.CommandOp.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099CommandWrite.CommandOp.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099CommandWrite.CommandOp.relative_brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099CommandWrite.RelativeBrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6099CommandWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6099CommandWrite.CommandOp.display_setting:
            pass
            self.body._fetch_instances()
        elif _on == H6099CommandWrite.CommandOp.installation_direction:
            pass
            self.body._fetch_instances()
        elif _on == H6099CommandWrite.CommandOp.mode:
            pass
            self.body._fetch_instances()
        elif _on == H6099CommandWrite.CommandOp.power:
            pass
            self.body._fetch_instances()
        elif _on == H6099CommandWrite.CommandOp.relative_brightness:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6099CommandWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6099CommandWrite.CommandOp.brightness:
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
        elif _on == H6099CommandWrite.CommandOp.display_setting:
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
        elif _on == H6099CommandWrite.CommandOp.installation_direction:
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
        elif _on == H6099CommandWrite.CommandOp.mode:
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
        elif _on == H6099CommandWrite.CommandOp.power:
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
        elif _on == H6099CommandWrite.CommandOp.relative_brightness:
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
        if _on == H6099CommandWrite.CommandOp.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099CommandWrite.CommandOp.display_setting:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099CommandWrite.CommandOp.installation_direction:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099CommandWrite.CommandOp.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099CommandWrite.CommandOp.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099CommandWrite.CommandOp.relative_brightness:
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

    class BlackBorderPayload(ReadWriteKaitaiStruct):
        """Android 7.6.01 H6099 black-border control writes A9 0B 01 enabled."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.BlackBorderPayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.BlackBorderPayload, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class BlankScreenPayload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.BlankScreenPayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self.detection = KaitaiStream.resolve_enum(H6099CommandWrite.BlankScreenDetection, self._io.read_u1())
            self.low_brightness_duration_seconds = self._io.read_u2le()
            self.same_tone_duration_seconds = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.BlankScreenPayload, self)._write__seq(io)
            self._io.write_u1(self.is_on)
            self._io.write_u1(int(self.detection))
            self._io.write_u2le(self.low_brightness_duration_seconds)
            self._io.write_u2le(self.same_tone_duration_seconds)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class BrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)


        def _check(self):
            self._dirty = False


    class DisplaySettingBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.DisplaySettingBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.setting = KaitaiStream.resolve_enum(H6099CommandWrite.DisplaySetting, self._io.read_u1())
            self.len = self._io.read_u1()
            _on = self.setting
            if _on == H6099CommandWrite.DisplaySetting.black_border:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099CommandWrite.BlackBorderPayload(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6099CommandWrite.DisplaySetting.blank_screen:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099CommandWrite.BlankScreenPayload(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6099CommandWrite.DisplaySetting.scalar_white_balance:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099CommandWrite.ScalarWhiteBalancePayload(_io__raw_payload, self, self._root)
                self.payload._read()
            else:
                pass
                self.payload = self._io.read_bytes(self.len)
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.setting
            if _on == H6099CommandWrite.DisplaySetting.black_border:
                pass
                self.payload._fetch_instances()
            elif _on == H6099CommandWrite.DisplaySetting.blank_screen:
                pass
                self.payload._fetch_instances()
            elif _on == H6099CommandWrite.DisplaySetting.scalar_white_balance:
                pass
                self.payload._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.DisplaySettingBody, self)._write__seq(io)
            self._io.write_u1(int(self.setting))
            self._io.write_u1(self.len)
            _on = self.setting
            if _on == H6099CommandWrite.DisplaySetting.black_border:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(self.len)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.len))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != self.len:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", self.len, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6099CommandWrite.DisplaySetting.blank_screen:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(self.len)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.len))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != self.len:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", self.len, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            elif _on == H6099CommandWrite.DisplaySetting.scalar_white_balance:
                pass
                _io__raw_payload = KaitaiStream(BytesIO(bytearray(self.len)))
                self._io.add_child_stream(_io__raw_payload)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.len))
                def handler(parent, _io__raw_payload=_io__raw_payload):
                    self._raw_payload = _io__raw_payload.to_byte_array()
                    if len(self._raw_payload) != self.len:
                        raise kaitaistruct.ConsistencyError(u"raw(payload)", self.len, len(self._raw_payload))
                    parent.write_bytes(self._raw_payload)
                _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.payload._write__seq(_io__raw_payload)
            else:
                pass
                self._io.write_bytes(self.payload)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            _on = self.setting
            if _on == H6099CommandWrite.DisplaySetting.black_border:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6099CommandWrite.DisplaySetting.blank_screen:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6099CommandWrite.DisplaySetting.scalar_white_balance:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            else:
                pass
                if len(self.payload) != self.len:
                    raise kaitaistruct.ConsistencyError(u"payload", self.len, len(self.payload))
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.code)


        def _check(self):
            self._dirty = False


    class InstallationDirectionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.InstallationDirectionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.InstallationDirectionBody, self)._write__seq(io)
            self._io.write_u1(self.value)


        def _check(self):
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub_mode = KaitaiStream.resolve_enum(H6099CommandWrite.ModeSel, self._io.read_u1())
            _on = self.sub_mode
            if _on == H6099CommandWrite.ModeSel.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099CommandWrite.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099CommandWrite.ModeSel.music:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099CommandWrite.MusicBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099CommandWrite.ModeSel.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099CommandWrite.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099CommandWrite.ModeSel.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099CommandWrite.StaticColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099CommandWrite.ModeSel.video:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099CommandWrite.VideoBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub_mode
            if _on == H6099CommandWrite.ModeSel.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H6099CommandWrite.ModeSel.music:
                pass
                self.detail._fetch_instances()
            elif _on == H6099CommandWrite.ModeSel.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H6099CommandWrite.ModeSel.static_colour:
                pass
                self.detail._fetch_instances()
            elif _on == H6099CommandWrite.ModeSel.video:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.sub_mode))
            _on = self.sub_mode
            if _on == H6099CommandWrite.ModeSel.diy:
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
            elif _on == H6099CommandWrite.ModeSel.music:
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
            elif _on == H6099CommandWrite.ModeSel.scene:
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
            elif _on == H6099CommandWrite.ModeSel.static_colour:
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
            elif _on == H6099CommandWrite.ModeSel.video:
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
            if _on == H6099CommandWrite.ModeSel.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099CommandWrite.ModeSel.music:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099CommandWrite.ModeSel.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099CommandWrite.ModeSel.static_colour:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099CommandWrite.ModeSel.video:
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
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.MusicBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6099CommandWrite.MusicMode, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            if self.is_legacy:
                pass
                self.is_calm = self._io.read_u1()

            if self.is_legacy:
                pass
                self.has_fixed_colour = self._io.read_u1()

            if self.is_legacy:
                pass
                self.fixed_colour = govee_shared.GoveeShared.Rgb(self._io)
                self.fixed_colour._read()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if self.is_legacy:
                pass
                self.fixed_colour._fetch_instances()



        def _write__seq(self, io=None):
            super(H6099CommandWrite.MusicBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            self._io.write_u1(self.sensitivity)
            if self.is_legacy:
                pass
                self._io.write_u1(self.is_calm)

            if self.is_legacy:
                pass
                self._io.write_u1(self.has_fixed_colour)

            if self.is_legacy:
                pass
                self.fixed_colour._write__seq(self._io)



        def _check(self):
            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            if self.is_legacy:
                pass

            self._dirty = False

        @property
        def is_legacy(self):
            if hasattr(self, '_m_is_legacy'):
                return self._m_is_legacy

            self._m_is_legacy =  ((self.mode == H6099CommandWrite.MusicMode.rhythm) or (self.mode == H6099CommandWrite.MusicMode.spectrum) or (self.mode == H6099CommandWrite.MusicMode.energetic) or (self.mode == H6099CommandWrite.MusicMode.rolling)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy

    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)


        def _check(self):
            self._dirty = False


    class RelativeBrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.RelativeBrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, self._io, u"/types/relative_brightness_body/seq/0")
            self.edge_count = self._io.read_u1()
            self.left_percent = self._io.read_u1()
            self.top_percent = self._io.read_u1()
            self.right_percent = self._io.read_u1()
            self.bottom_percent = self._io.read_u1()
            self.strip_left_percent = self._io.read_u1()
            self.strip_right_percent = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.RelativeBrightnessBody, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            self._io.write_u1(self.edge_count)
            self._io.write_u1(self.left_percent)
            self._io.write_u1(self.top_percent)
            self._io.write_u1(self.right_percent)
            self._io.write_u1(self.bottom_percent)
            self._io.write_u1(self.strip_left_percent)
            self._io.write_u1(self.strip_right_percent)


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.selector, None, u"/types/relative_brightness_body/seq/0")
            self._dirty = False


    class ScalarWhiteBalancePayload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.ScalarWhiteBalancePayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.ScalarWhiteBalancePayload, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)


        def _check(self):
            self._dirty = False


    class StaticColourBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.StaticColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.operation = KaitaiStream.resolve_enum(H6099CommandWrite.StaticOperation, self._io.read_u1())
            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.red = self._io.read_u1()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.green = self._io.read_u1()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.blue = self._io.read_u1()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.kelvin = self._io.read_u2be()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.preview = govee_shared.GoveeShared.Rgb(self._io)
                self.preview._read()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.segment_mask = self._io.read_u2le()

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass
                self.brightness_percent = self._io.read_u1()

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass
                self.brightness_segment_mask = self._io.read_u2le()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.preview._fetch_instances()

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass



        def _write__seq(self, io=None):
            super(H6099CommandWrite.StaticColourBody, self)._write__seq(io)
            self._io.write_u1(int(self.operation))
            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.red)

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.green)

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u1(self.blue)

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u2be(self.kelvin)

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self.preview._write__seq(self._io)

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass
                self._io.write_u2le(self.segment_mask)

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass
                self._io.write_u1(self.brightness_percent)

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass
                self._io.write_u2le(self.brightness_segment_mask)



        def _check(self):
            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.colour:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass

            if self.operation == H6099CommandWrite.StaticOperation.brightness:
                pass

            self._dirty = False


    class VideoBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099CommandWrite.VideoBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.source = KaitaiStream.resolve_enum(H6099CommandWrite.VideoSource, self._io.read_u1())
            self.region = KaitaiStream.resolve_enum(H6099CommandWrite.VideoRegion, self._io.read_u1())
            self.saturation = self._io.read_u1()
            self.sound_effects = self._io.read_u1()
            self.sound_type = self._io.read_bytes(1)
            if not self.sound_type == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.sound_type, self._io, u"/types/video_body/seq/4")
            self.softness = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099CommandWrite.VideoBody, self)._write__seq(io)
            self._io.write_u1(int(self.source))
            self._io.write_u1(int(self.region))
            self._io.write_u1(self.saturation)
            self._io.write_u1(self.sound_effects)
            self._io.write_bytes(self.sound_type)
            self._io.write_u1(self.softness)


        def _check(self):
            if len(self.sound_type) != 1:
                raise kaitaistruct.ConsistencyError(u"sound_type", 1, len(self.sound_type))
            if not self.sound_type == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.sound_type, None, u"/types/video_body/seq/4")
            self._dirty = False



