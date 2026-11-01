# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_segment_page
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099StatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 reply frame for issue #258, checked against Android 7.6.01
    H6099 status parsing.  AA 05 15 contains a flag followed by big-endian Kelvin
    (zero for RGB).  Companion-backed music replies carry only mode and
    sensitivity; trailing bytes are not legacy style or fixed colour.  Mode 0x0a
    reads a little-endian DIY code.  Segment pages carry 14 logical zones across
    four four-slot pages, with unused final records kept opaque.  AA40 carries the
    signed big-endian physical IC count in its first two payload bytes.  AA20 and
    AA21 decode ASCII Wi-Fi hardware and software identity, and A9 0B length 01
    carries the black-border enabled byte.  AA30 reads the installation direction
    in its first payload byte, and AA32 reads camera health (0 absent, 1 healthy,
    2 incompatible; missing replies are not evidence of absence).  Direction
    orientations, other camera values, owner qualification, firmware differences,
    and unknown tails remain unresolved; 31 is camera position, not health.
    """

    class BlankScreenDetection(IntEnum):
        low_brightness = 1
        same_tone = 2

    class CameraHealth(IntEnum):
        absent = 0
        healthy = 1
        incompatible = 2

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

    class StatusDomain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
        firmware = 6
        hardware = 7
        subordinate_20 = 32
        subordinate_21 = 33
        installation_direction = 48
        camera_health = 50
        physical_ic_count = 64
        segments = 165
        display_setting = 169
        relative_brightness = 174

    class VideoRegion(IntEnum):
        part = 8
        all = 9

    class VideoSource(IntEnum):
        movie = 0
        game = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099StatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6099StatusReply.StatusDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6099StatusReply.StatusDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.camera_health:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.CameraHealthBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.colour_mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.ColourModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.display_setting:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.DisplaySettingBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.HardwareVersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.installation_direction:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.InstallationDirectionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.physical_ic_count:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.PhysicalIcCountBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.relative_brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.RelativeBrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.segments:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = govee_segment_page.GoveeSegmentPage(14, 4, False, _io__raw_body)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.subordinate_20:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6099StatusReply.StatusDomain.subordinate_21:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099StatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6099StatusReply.StatusDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.camera_health:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.colour_mode:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.display_setting:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.installation_direction:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.physical_ic_count:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.relative_brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.segments:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.subordinate_20:
            pass
            self.body._fetch_instances()
        elif _on == H6099StatusReply.StatusDomain.subordinate_21:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6099StatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6099StatusReply.StatusDomain.brightness:
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
        elif _on == H6099StatusReply.StatusDomain.camera_health:
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
        elif _on == H6099StatusReply.StatusDomain.colour_mode:
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
        elif _on == H6099StatusReply.StatusDomain.display_setting:
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
        elif _on == H6099StatusReply.StatusDomain.firmware:
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
        elif _on == H6099StatusReply.StatusDomain.hardware:
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
        elif _on == H6099StatusReply.StatusDomain.installation_direction:
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
        elif _on == H6099StatusReply.StatusDomain.physical_ic_count:
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
        elif _on == H6099StatusReply.StatusDomain.power:
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
        elif _on == H6099StatusReply.StatusDomain.relative_brightness:
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
        elif _on == H6099StatusReply.StatusDomain.segments:
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
        elif _on == H6099StatusReply.StatusDomain.subordinate_20:
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
        elif _on == H6099StatusReply.StatusDomain.subordinate_21:
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
        if _on == H6099StatusReply.StatusDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.camera_health:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.colour_mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.display_setting:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.firmware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.hardware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.installation_direction:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.physical_ic_count:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.relative_brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.segments:
            pass
            if self.body.segment_count != 14:
                raise kaitaistruct.ConsistencyError(u"body", 14, self.body.segment_count)
            if self.body.group_size != 4:
                raise kaitaistruct.ConsistencyError(u"body", 4, self.body.group_size)
            if self.body.unused_must_be_zero != False:
                raise kaitaistruct.ConsistencyError(u"body", False, self.body.unused_must_be_zero)
        elif _on == H6099StatusReply.StatusDomain.subordinate_20:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6099StatusReply.StatusDomain.subordinate_21:
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

    class BlackBorderState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.BlackBorderState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_enabled = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.BlackBorderState, self)._write__seq(io)
            self._io.write_u1(self.is_enabled)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class BlankScreenState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.BlankScreenState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_enabled = self._io.read_u1()
            self.detection = KaitaiStream.resolve_enum(H6099StatusReply.BlankScreenDetection, self._io.read_u1())
            self.low_brightness_duration_seconds = self._io.read_u2le()
            self.same_tone_duration_seconds = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.BlankScreenState, self)._write__seq(io)
            self._io.write_u1(self.is_enabled)
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
            super(H6099StatusReply.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)


        def _check(self):
            self._dirty = False


    class CameraHealthBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.CameraHealthBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = KaitaiStream.resolve_enum(H6099StatusReply.CameraHealth, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.CameraHealthBody, self)._write__seq(io)
            self._io.write_u1(int(self.value))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ColourModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.ColourModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6099StatusReply.ModeSel, self._io.read_u1())
            _on = self.mode
            if _on == H6099StatusReply.ModeSel.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099StatusReply.DiyState(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099StatusReply.ModeSel.music:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099StatusReply.MusicState(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099StatusReply.ModeSel.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099StatusReply.SceneState(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099StatusReply.ModeSel.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099StatusReply.StaticState(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6099StatusReply.ModeSel.video:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6099StatusReply.VideoState(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H6099StatusReply.ModeSel.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H6099StatusReply.ModeSel.music:
                pass
                self.detail._fetch_instances()
            elif _on == H6099StatusReply.ModeSel.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H6099StatusReply.ModeSel.static_colour:
                pass
                self.detail._fetch_instances()
            elif _on == H6099StatusReply.ModeSel.video:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.ColourModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H6099StatusReply.ModeSel.diy:
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
            elif _on == H6099StatusReply.ModeSel.music:
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
            elif _on == H6099StatusReply.ModeSel.scene:
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
            elif _on == H6099StatusReply.ModeSel.static_colour:
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
            elif _on == H6099StatusReply.ModeSel.video:
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
            if _on == H6099StatusReply.ModeSel.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099StatusReply.ModeSel.music:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099StatusReply.ModeSel.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099StatusReply.ModeSel.static_colour:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6099StatusReply.ModeSel.video:
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


    class DisplaySettingBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.DisplaySettingBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.setting = KaitaiStream.resolve_enum(H6099StatusReply.DisplaySetting, self._io.read_u1())
            self.len = self._io.read_u1()
            _on = self.setting
            if _on == H6099StatusReply.DisplaySetting.black_border:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099StatusReply.BlackBorderState(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6099StatusReply.DisplaySetting.blank_screen:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099StatusReply.BlankScreenState(_io__raw_payload, self, self._root)
                self.payload._read()
            elif _on == H6099StatusReply.DisplaySetting.scalar_white_balance:
                pass
                self._raw_payload = self._io.read_bytes(self.len)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = H6099StatusReply.ScalarWhiteBalanceState(_io__raw_payload, self, self._root)
                self.payload._read()
            else:
                pass
                self.payload = self._io.read_bytes(self.len)
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.setting
            if _on == H6099StatusReply.DisplaySetting.black_border:
                pass
                self.payload._fetch_instances()
            elif _on == H6099StatusReply.DisplaySetting.blank_screen:
                pass
                self.payload._fetch_instances()
            elif _on == H6099StatusReply.DisplaySetting.scalar_white_balance:
                pass
                self.payload._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.DisplaySettingBody, self)._write__seq(io)
            self._io.write_u1(int(self.setting))
            self._io.write_u1(self.len)
            _on = self.setting
            if _on == H6099StatusReply.DisplaySetting.black_border:
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
            elif _on == H6099StatusReply.DisplaySetting.blank_screen:
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
            elif _on == H6099StatusReply.DisplaySetting.scalar_white_balance:
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
            if _on == H6099StatusReply.DisplaySetting.black_border:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6099StatusReply.DisplaySetting.blank_screen:
                pass
                if self.payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
                if self.payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
            elif _on == H6099StatusReply.DisplaySetting.scalar_white_balance:
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


    class DiyState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.DiyState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.DiyState, self)._write__seq(io)
            self._io.write_u2le(self.code)


        def _check(self):
            self._dirty = False


    class HardwareVersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.HardwareVersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.prefix = self._io.read_bytes(1)
            if not self.prefix == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.prefix, self._io, u"/types/hardware_version_body/seq/0")
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.HardwareVersionBody, self)._write__seq(io)
            self._io.write_bytes(self.prefix)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)


        def _check(self):
            if len(self.prefix) != 1:
                raise kaitaistruct.ConsistencyError(u"prefix", 1, len(self.prefix))
            if not self.prefix == b"\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x03", self.prefix, None, u"/types/hardware_version_body/seq/0")
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class InstallationDirectionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.InstallationDirectionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.InstallationDirectionBody, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class MusicState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.MusicState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6099StatusReply.MusicMode, self._io.read_u1())
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

            self.unknown_tail = self._io.read_bytes_full()
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
            super(H6099StatusReply.MusicState, self)._write__seq(io)
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

            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


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

            self._m_is_legacy =  ((self.mode == H6099StatusReply.MusicMode.rhythm) or (self.mode == H6099StatusReply.MusicMode.spectrum) or (self.mode == H6099StatusReply.MusicMode.energetic) or (self.mode == H6099StatusReply.MusicMode.rolling)) 
            return getattr(self, '_m_is_legacy', None)

        def _invalidate_is_legacy(self):
            del self._m_is_legacy

    class PhysicalIcCountBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.PhysicalIcCountBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.count = self._io.read_s2be()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.PhysicalIcCountBody, self)._write__seq(io)
            self._io.write_s2be(self.count)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)


        def _check(self):
            self._dirty = False


    class RelativeBrightnessBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.RelativeBrightnessBody, self).__init__(_io)
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
            super(H6099StatusReply.RelativeBrightnessBody, self)._write__seq(io)
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


    class ScalarWhiteBalanceState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.ScalarWhiteBalanceState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.ScalarWhiteBalanceState, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SceneState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.SceneState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.SceneState, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)


        def _check(self):
            self._dirty = False


    class StaticState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.StaticState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub = self._io.read_u1()
            self.kelvin = self._io.read_u2be()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.StaticState, self)._write__seq(io)
            self._io.write_u1(self.sub)
            self._io.write_u2be(self.kelvin)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class VersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.VersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.VersionBody, self)._write__seq(io)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class VideoState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099StatusReply.VideoState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.source = KaitaiStream.resolve_enum(H6099StatusReply.VideoSource, self._io.read_u1())
            self.region = KaitaiStream.resolve_enum(H6099StatusReply.VideoRegion, self._io.read_u1())
            self.saturation = self._io.read_u1()
            self.sound_effects = self._io.read_u1()
            self.sound_type = self._io.read_u1()
            self.softness = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6099StatusReply.VideoState, self)._write__seq(io)
            self._io.write_u1(int(self.source))
            self._io.write_u1(int(self.region))
            self._io.write_u1(self.saturation)
            self._io.write_u1(self.sound_effects)
            self._io.write_u1(self.sound_type)
            self._io.write_u1(self.softness)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



