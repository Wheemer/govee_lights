# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6DiyBody(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 native DIY body for #402.  Compatibility hypothesis:
    family 797 uses a complete 0x50-prefixed body with a little-endian payload
    length, background palette and length-delimited typed layers.  This is not
    an A3 logical header.  Each recognised layer has a speed byte and a
    colour-count-prefixed RGB palette.  A payload length of 32 also produces a
    0x50 0x20 prefix; use exact family metadata rather than prefix-only routing.
    Unresolved assumptions: no exact-model BLE capture qualifies these layouts,
    parameter meanings, background flag, editor limits or firmware coverage.
    Unmapped parameters, unknown layer kinds and trailing layer data remain opaque.
    """

    class LayerKind(IntEnum):
        area_flow = 1
        line_flow = 2
        spread_gather = 3
        rotation = 4
        random_breathing = 5
        meteor = 6
        random_gradient = 7
        fade = 8
        breathing = 9
        flashing = 10
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6DiyBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.marker = self._io.read_bytes(1)
        if not self.marker == b"\x50":
            raise kaitaistruct.ValidationNotEqualError(b"\x50", self.marker, self._io, u"/seq/0")
        self.payload_length = self._io.read_u2le()
        self._raw_payload = self._io.read_bytes(self.payload_length)
        _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
        self.payload = H60a6DiyBody.Payload(_io__raw_payload, self, self._root)
        self.payload._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.payload._fetch_instances()


    def _write__seq(self, io=None):
        super(H60a6DiyBody, self)._write__seq(io)
        self._io.write_bytes(self.marker)
        self._io.write_u2le(self.payload_length)
        _io__raw_payload = KaitaiStream(BytesIO(bytearray(self.payload_length)))
        self._io.add_child_stream(_io__raw_payload)
        _pos2 = self._io.pos()
        self._io.seek(self._io.pos() + (self.payload_length))
        def handler(parent, _io__raw_payload=_io__raw_payload):
            self._raw_payload = _io__raw_payload.to_byte_array()
            if len(self._raw_payload) != self.payload_length:
                raise kaitaistruct.ConsistencyError(u"raw(payload)", self.payload_length, len(self._raw_payload))
            parent.write_bytes(self._raw_payload)
        _io__raw_payload.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
        self.payload._write__seq(_io__raw_payload)


    def _check(self):
        if len(self.marker) != 1:
            raise kaitaistruct.ConsistencyError(u"marker", 1, len(self.marker))
        if not self.marker == b"\x50":
            raise kaitaistruct.ValidationNotEqualError(b"\x50", self.marker, None, u"/seq/0")
        if self.payload._root != self._root:
            raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
        if self.payload._parent != self:
            raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        self._dirty = False

    class AreaFlow(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.AreaFlow, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameters = self._io.read_bytes(13)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.AreaFlow, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.unknown_parameters) != 13:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 13, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class Layer(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.Layer, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.length = self._io.read_u2le()
            self.kind = KaitaiStream.resolve_enum(H60a6DiyBody.LayerKind, self._io.read_u1())
            _on = self.kind
            if _on == H60a6DiyBody.LayerKind.area_flow:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.AreaFlow(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.breathing:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.SingleParameter(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.fade:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.SingleParameter(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.flashing:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.SingleParameter(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.line_flow:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.LineFlow(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.meteor:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.Meteor(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.random_breathing:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.RandomBreathing(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.random_gradient:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.RandomGradient(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.rotation:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.Rotation(_io__raw_body, self, self._root)
                self.body._read()
            elif _on == H60a6DiyBody.LayerKind.spread_gather:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.SpreadGather(_io__raw_body, self, self._root)
                self.body._read()
            else:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6DiyBody.OpaqueBody(_io__raw_body, self, self._root)
                self.body._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.kind
            if _on == H60a6DiyBody.LayerKind.area_flow:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.breathing:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.fade:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.flashing:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.line_flow:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.meteor:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.random_breathing:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.random_gradient:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.rotation:
                pass
                self.body._fetch_instances()
            elif _on == H60a6DiyBody.LayerKind.spread_gather:
                pass
                self.body._fetch_instances()
            else:
                pass
                self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.Layer, self)._write__seq(io)
            self._io.write_u2le(self.length)
            self._io.write_u1(int(self.kind))
            _on = self.kind
            if _on == H60a6DiyBody.LayerKind.area_flow:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.breathing:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.fade:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.flashing:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.line_flow:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.meteor:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.random_breathing:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.random_gradient:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.rotation:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            elif _on == H60a6DiyBody.LayerKind.spread_gather:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)
            else:
                pass
                _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 1)))
                self._io.add_child_stream(_io__raw_body)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.length - 1))
                def handler(parent, _io__raw_body=_io__raw_body):
                    self._raw_body = _io__raw_body.to_byte_array()
                    if len(self._raw_body) != self.length - 1:
                        raise kaitaistruct.ConsistencyError(u"raw(body)", self.length - 1, len(self._raw_body))
                    parent.write_bytes(self._raw_body)
                _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                self.body._write__seq(_io__raw_body)


        def _check(self):
            _on = self.kind
            if _on == H60a6DiyBody.LayerKind.area_flow:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.breathing:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.fade:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.flashing:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.line_flow:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.meteor:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.random_breathing:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.random_gradient:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.rotation:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == H60a6DiyBody.LayerKind.spread_gather:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            else:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            self._dirty = False


    class LineFlow(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.LineFlow, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameter = self._io.read_u1()
            self.unknown_flag = self._io.read_u1()
            self.point_count = self._io.read_u1()
            self.points = []
            for i in range(self.point_count):
                self.points.append(self._io.read_u1())

            self.unknown_parameters = self._io.read_bytes(5)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.points)):
                pass

            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.LineFlow, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.unknown_parameter)
            self._io.write_u1(self.unknown_flag)
            self._io.write_u1(self.point_count)
            for i in range(len(self.points)):
                pass
                self._io.write_u1(self.points[i])

            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.points) != self.point_count:
                raise kaitaistruct.ConsistencyError(u"points", self.point_count, len(self.points))
            for i in range(len(self.points)):
                pass

            if len(self.unknown_parameters) != 5:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 5, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class Meteor(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.Meteor, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameters = self._io.read_bytes(5)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.Meteor, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.unknown_parameters) != 5:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 5, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class OpaqueBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.OpaqueBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6DiyBody.OpaqueBody, self)._write__seq(io)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Palette(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.Palette, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.colour_count = self._io.read_u1()
            self.colours = []
            for i in range(self.colour_count):
                _t_colours = govee_shared.GoveeShared.Rgb(self._io)
                try:
                    _t_colours._read()
                finally:
                    self.colours.append(_t_colours)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.colours)):
                pass
                self.colours[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H60a6DiyBody.Palette, self)._write__seq(io)
            self._io.write_u1(self.colour_count)
            for i in range(len(self.colours)):
                pass
                self.colours[i]._write__seq(self._io)



        def _check(self):
            if len(self.colours) != self.colour_count:
                raise kaitaistruct.ConsistencyError(u"colours", self.colour_count, len(self.colours))
            for i in range(len(self.colours)):
                pass

            self._dirty = False


    class Payload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.Payload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.layer_count = self._io.read_u1()
            self.background_count = self._io.read_u1()
            self.backgrounds = []
            for i in range(self.background_count):
                _t_backgrounds = govee_shared.GoveeShared.Rgb(self._io)
                try:
                    _t_backgrounds._read()
                finally:
                    self.backgrounds.append(_t_backgrounds)

            self.background_flag = self._io.read_u1()
            self.layers = []
            for i in range(self.layer_count):
                _t_layers = H60a6DiyBody.Layer(self._io, self, self._root)
                try:
                    _t_layers._read()
                finally:
                    self.layers.append(_t_layers)

            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.backgrounds)):
                pass
                self.backgrounds[i]._fetch_instances()

            for i in range(len(self.layers)):
                pass
                self.layers[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H60a6DiyBody.Payload, self)._write__seq(io)
            self._io.write_u1(self.layer_count)
            self._io.write_u1(self.background_count)
            for i in range(len(self.backgrounds)):
                pass
                self.backgrounds[i]._write__seq(self._io)

            self._io.write_u1(self.background_flag)
            for i in range(len(self.layers)):
                pass
                self.layers[i]._write__seq(self._io)

            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.backgrounds) != self.background_count:
                raise kaitaistruct.ConsistencyError(u"backgrounds", self.background_count, len(self.backgrounds))
            for i in range(len(self.backgrounds)):
                pass

            if len(self.layers) != self.layer_count:
                raise kaitaistruct.ConsistencyError(u"layers", self.layer_count, len(self.layers))
            for i in range(len(self.layers)):
                pass
                if self.layers[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"layers", self._root, self.layers[i]._root)
                if self.layers[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"layers", self, self.layers[i]._parent)

            self._dirty = False


    class RandomBreathing(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.RandomBreathing, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameters = self._io.read_bytes(2)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.RandomBreathing, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.unknown_parameters) != 2:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 2, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class RandomGradient(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.RandomGradient, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameters = self._io.read_bytes(2)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.RandomGradient, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.unknown_parameters) != 2:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 2, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class Rotation(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.Rotation, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.direction = self._io.read_u1()
            self.angle = self._io.read_u2le()
            self.unknown_flag = self._io.read_u1()
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.Rotation, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.direction)
            self._io.write_u2le(self.angle)
            self._io.write_u1(self.unknown_flag)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class SingleParameter(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.SingleParameter, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameter = self._io.read_u1()
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.SingleParameter, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_u1(self.unknown_parameter)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False


    class SpreadGather(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6DiyBody.SpreadGather, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.speed = self._io.read_u1()
            self.unknown_parameters = self._io.read_bytes(7)
            self.palette = H60a6DiyBody.Palette(self._io, self, self._root)
            self.palette._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.palette._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6DiyBody.SpreadGather, self)._write__seq(io)
            self._io.write_u1(self.speed)
            self._io.write_bytes(self.unknown_parameters)
            self.palette._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.unknown_parameters) != 7:
                raise kaitaistruct.ConsistencyError(u"unknown_parameters", 7, len(self.unknown_parameters))
            if self.palette._root != self._root:
                raise kaitaistruct.ConsistencyError(u"palette", self._root, self.palette._root)
            if self.palette._parent != self:
                raise kaitaistruct.ConsistencyError(u"palette", self, self.palette._parent)
            self._dirty = False



