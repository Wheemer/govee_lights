# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6PaintBody(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 native paint body for #402.  Compatibility hypothesis:
    family 798 uses a complete 0x50 0x20-prefixed body with background RGB,
    background brightness, show type and length-delimited layers.  Kind 3
    contains length-delimited colour groups followed by action, speed,
    brightness, priority, duration and four opaque bytes.  All lengths and
    counts wider than one byte are little-endian.  This is not an A3 header.
    Unresolved assumptions: no exact-model BLE capture qualifies every action,
    show type, duration unit, priority rule, editor limit or firmware revision.
    Candidate action codes are 1 through 7; their meanings remain unmapped.
    Unknown layer kinds, extension bytes and opaque fields are preserved.
    """

    class ActionCode(IntEnum):
        action_1 = 1
        action_2 = 2
        action_3 = 3
        action_4 = 4
        action_5 = 5
        action_6 = 6
        action_7 = 7

    class LayerKind(IntEnum):
        point_groups = 3
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6PaintBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.marker = self._io.read_bytes(2)
        if not self.marker == b"\x50\x20":
            raise kaitaistruct.ValidationNotEqualError(b"\x50\x20", self.marker, self._io, u"/seq/0")
        self.background = govee_shared.GoveeShared.Rgb(self._io)
        self.background._read()
        self.background_brightness = self._io.read_u1()
        self.show_type = self._io.read_u1()
        self.layer_count = self._io.read_u1()
        self.layers = []
        for i in range(self.layer_count):
            _t_layers = H60a6PaintBody.Layer(self._io, self, self._root)
            try:
                _t_layers._read()
            finally:
                self.layers.append(_t_layers)

        self.opaque = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.background._fetch_instances()
        for i in range(len(self.layers)):
            pass
            self.layers[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(H60a6PaintBody, self)._write__seq(io)
        self._io.write_bytes(self.marker)
        self.background._write__seq(self._io)
        self._io.write_u1(self.background_brightness)
        self._io.write_u1(self.show_type)
        self._io.write_u1(self.layer_count)
        for i in range(len(self.layers)):
            pass
            self.layers[i]._write__seq(self._io)

        self._io.write_bytes(self.opaque)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.marker) != 2:
            raise kaitaistruct.ConsistencyError(u"marker", 2, len(self.marker))
        if not self.marker == b"\x50\x20":
            raise kaitaistruct.ValidationNotEqualError(b"\x50\x20", self.marker, None, u"/seq/0")
        if len(self.layers) != self.layer_count:
            raise kaitaistruct.ConsistencyError(u"layers", self.layer_count, len(self.layers))
        for i in range(len(self.layers)):
            pass
            if self.layers[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"layers", self._root, self.layers[i]._root)
            if self.layers[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"layers", self, self.layers[i]._parent)

        self._dirty = False

    class ColourGroup(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6PaintBody.ColourGroup, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.point_count = self._io.read_u2le()
            self.colour = govee_shared.GoveeShared.Rgb(self._io)
            self.colour._read()
            self.indices = []
            for i in range(self.point_count):
                self.indices.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.colour._fetch_instances()
            for i in range(len(self.indices)):
                pass



        def _write__seq(self, io=None):
            super(H60a6PaintBody.ColourGroup, self)._write__seq(io)
            self._io.write_u2le(self.point_count)
            self.colour._write__seq(self._io)
            for i in range(len(self.indices)):
                pass
                self._io.write_u1(self.indices[i])



        def _check(self):
            if len(self.indices) != self.point_count:
                raise kaitaistruct.ConsistencyError(u"indices", self.point_count, len(self.indices))
            for i in range(len(self.indices)):
                pass

            self._dirty = False


    class ColourGroups(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6PaintBody.ColourGroups, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.group_count = self._io.read_u2le()
            self.groups = []
            for i in range(self.group_count):
                _t_groups = H60a6PaintBody.ColourGroup(self._io, self, self._root)
                try:
                    _t_groups._read()
                finally:
                    self.groups.append(_t_groups)

            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.groups)):
                pass
                self.groups[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H60a6PaintBody.ColourGroups, self)._write__seq(io)
            self._io.write_u2le(self.group_count)
            for i in range(len(self.groups)):
                pass
                self.groups[i]._write__seq(self._io)

            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.groups) != self.group_count:
                raise kaitaistruct.ConsistencyError(u"groups", self.group_count, len(self.groups))
            for i in range(len(self.groups)):
                pass
                if self.groups[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"groups", self._root, self.groups[i]._root)
                if self.groups[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"groups", self, self.groups[i]._parent)

            self._dirty = False


    class Layer(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6PaintBody.Layer, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.length = self._io.read_u2le()
            self.kind = KaitaiStream.resolve_enum(H60a6PaintBody.LayerKind, self._io.read_u1())
            _on = self.kind
            if _on == H60a6PaintBody.LayerKind.point_groups:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6PaintBody.PointGroups(_io__raw_body, self, self._root)
                self.body._read()
            else:
                pass
                self._raw_body = self._io.read_bytes(self.length - 1)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = H60a6PaintBody.OpaqueBody(_io__raw_body, self, self._root)
                self.body._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.kind
            if _on == H60a6PaintBody.LayerKind.point_groups:
                pass
                self.body._fetch_instances()
            else:
                pass
                self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6PaintBody.Layer, self)._write__seq(io)
            self._io.write_u2le(self.length)
            self._io.write_u1(int(self.kind))
            _on = self.kind
            if _on == H60a6PaintBody.LayerKind.point_groups:
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
            if _on == H60a6PaintBody.LayerKind.point_groups:
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


    class OpaqueBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6PaintBody.OpaqueBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6PaintBody.OpaqueBody, self)._write__seq(io)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class PointGroups(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6PaintBody.PointGroups, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data_length = self._io.read_u2le()
            self._raw_data = self._io.read_bytes(self.data_length)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = H60a6PaintBody.ColourGroups(_io__raw_data, self, self._root)
            self.data._read()
            self.action = KaitaiStream.resolve_enum(H60a6PaintBody.ActionCode, self._io.read_u1())
            self.speed = self._io.read_u1()
            self.brightness = self._io.read_u1()
            self.priority = self._io.read_u1()
            self.duration = self._io.read_u2le()
            self.opaque = self._io.read_bytes(4)
            self.trailing = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6PaintBody.PointGroups, self)._write__seq(io)
            self._io.write_u2le(self.data_length)
            _io__raw_data = KaitaiStream(BytesIO(bytearray(self.data_length)))
            self._io.add_child_stream(_io__raw_data)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.data_length))
            def handler(parent, _io__raw_data=_io__raw_data):
                self._raw_data = _io__raw_data.to_byte_array()
                if len(self._raw_data) != self.data_length:
                    raise kaitaistruct.ConsistencyError(u"raw(data)", self.data_length, len(self._raw_data))
                parent.write_bytes(self._raw_data)
            _io__raw_data.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.data._write__seq(_io__raw_data)
            self._io.write_u1(int(self.action))
            self._io.write_u1(self.speed)
            self._io.write_u1(self.brightness)
            self._io.write_u1(self.priority)
            self._io.write_u2le(self.duration)
            self._io.write_bytes(self.opaque)
            self._io.write_bytes(self.trailing)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"trailing", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.data._root != self._root:
                raise kaitaistruct.ConsistencyError(u"data", self._root, self.data._root)
            if self.data._parent != self:
                raise kaitaistruct.ConsistencyError(u"data", self, self.data._parent)
            if len(self.opaque) != 4:
                raise kaitaistruct.ConsistencyError(u"opaque", 4, len(self.opaque))
            self._dirty = False



