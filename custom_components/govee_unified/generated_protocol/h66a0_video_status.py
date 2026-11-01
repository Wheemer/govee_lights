# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h66a0_video_command
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H66a0VideoStatus(ReadWriteKaitaiStruct):
    """SPECULATIVE H66A0 minimal status fixture for issues #257 and #297.
    Contributor round2 reports aa 05 video replies share the command body.
    Only power, brightness and video read domains are represented. Independent
    captures and firmware coverage remain unresolved; no runtime model enabled.
    """

    class ModeSel(IntEnum):
        video = 0

    class ReadDomain(IntEnum):
        power = 1
        brightness = 4
        colour_mode = 5
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H66a0VideoStatus, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H66a0VideoStatus.ReadDomain, self._io.read_u1())
        _on = self.domain
        if _on == H66a0VideoStatus.ReadDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H66a0VideoStatus.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H66a0VideoStatus.ReadDomain.colour_mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H66a0VideoStatus.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H66a0VideoStatus.ReadDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H66a0VideoStatus.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H66a0VideoStatus.ReadDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H66a0VideoStatus.ReadDomain.colour_mode:
            pass
            self.body._fetch_instances()
        elif _on == H66a0VideoStatus.ReadDomain.power:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H66a0VideoStatus, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H66a0VideoStatus.ReadDomain.brightness:
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
        elif _on == H66a0VideoStatus.ReadDomain.colour_mode:
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
        elif _on == H66a0VideoStatus.ReadDomain.power:
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
        if _on == H66a0VideoStatus.ReadDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H66a0VideoStatus.ReadDomain.colour_mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H66a0VideoStatus.ReadDomain.power:
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
            super(H66a0VideoStatus.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.percent = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H66a0VideoStatus.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.percent)


        def _check(self):
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H66a0VideoStatus.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H66a0VideoStatus.ModeSel, self._io.read_u1())
            self._raw_detail = self._io.read_bytes(16)
            _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
            self.detail = h66a0_video_command.H66a0VideoCommand.VideoBody(_io__raw_detail)
            self.detail._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.detail._fetch_instances()


        def _write__seq(self, io=None):
            super(H66a0VideoStatus.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
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


        def _check(self):
            self._dirty = False


    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H66a0VideoStatus.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_on = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H66a0VideoStatus.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.is_on)


        def _check(self):
            self._dirty = False



