# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H66a0VideoCommand(ReadWriteKaitaiStruct):
    """SPECULATIVE H66A0 video-only fixture for issues #257 and #297.  Based on
    Fredde87/ha-govee-led-ble round2 command_write.ksy video_body_h66a0 and
    Android 7.6.01 TV-light video mode behaviour.  Contributor reports app preset reads
    08 Vivid, 09 Solid, 0a Smooth, 0b Delicate and a separate opaque byte.
    Independent captures, firmware coverage and owner qualification remain
    unresolved.  This codec does not register H66A0 as a supported model.
    """

    class PicturePreset(IntEnum):
        vivid = 8
        solid = 9
        smooth = 10
        delicate = 11

    class VideoSource(IntEnum):
        movie = 0
        game = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H66a0VideoCommand, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = self._io.read_bytes(1)
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, self._io, u"/seq/1")
        self.mode = self._io.read_bytes(1)
        if not self.mode == b"\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.mode, self._io, u"/seq/2")
        self._raw_detail = self._io.read_bytes(16)
        _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
        self.detail = H66a0VideoCommand.VideoBody(_io__raw_detail, self, self._root)
        self.detail._read()
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.detail._fetch_instances()


    def _write__seq(self, io=None):
        super(H66a0VideoCommand, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_bytes(self.opcode)
        self._io.write_bytes(self.mode)
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
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        if len(self.opcode) != 1:
            raise kaitaistruct.ConsistencyError(u"opcode", 1, len(self.opcode))
        if not self.opcode == b"\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\x05", self.opcode, None, u"/seq/1")
        if len(self.mode) != 1:
            raise kaitaistruct.ConsistencyError(u"mode", 1, len(self.mode))
        if not self.mode == b"\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.mode, None, u"/seq/2")
        if self.detail._root != self._root:
            raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
        if self.detail._parent != self:
            raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
        self._dirty = False

    class VideoBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H66a0VideoCommand.VideoBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.source = KaitaiStream.resolve_enum(H66a0VideoCommand.VideoSource, self._io.read_u1())
            self.picture_preset = KaitaiStream.resolve_enum(H66a0VideoCommand.PicturePreset, self._io.read_u1())
            self.saturation = self._io.read_u1()
            self.sound_effects = self._io.read_u1()
            self.opaque = self._io.read_u1()
            self.softness = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H66a0VideoCommand.VideoBody, self)._write__seq(io)
            self._io.write_u1(int(self.source))
            self._io.write_u1(int(self.picture_preset))
            self._io.write_u1(self.saturation)
            self._io.write_u1(self.sound_effects)
            self._io.write_u1(self.opaque)
            self._io.write_u1(self.softness)


        def _check(self):
            self._dirty = False



