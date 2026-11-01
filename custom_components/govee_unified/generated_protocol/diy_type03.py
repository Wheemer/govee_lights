# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class DiyType03(ReadWriteKaitaiStruct):

    class Effect(IntEnum):
        cycle = 2
        clockwise = 9
        counter_clockwise = 10
        twinkle = 15
        gradient = 19
        breathe = 20
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiyType03, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = govee_common.GoveeCommon.A3Header(self._io)
        self.header._read()
        self.body_type = self._io.read_bytes(1)
        if not self.body_type == b"\x03":
            raise kaitaistruct.ValidationNotEqualError(b"\x03", self.body_type, self._io, u"/seq/1")
        self.effect = KaitaiStream.resolve_enum(DiyType03.Effect, self._io.read_u1())
        self.speed = self._io.read_u1()
        self.brightness = self._io.read_u1()
        self.background = govee_shared.GoveeShared.Rgb(self._io)
        self.background._read()
        self.num_groups = self._io.read_u1()
        self.groups = []
        for i in range(self.num_groups):
            _t_groups = DiyType03.PaintGroup(self._io, self, self._root)
            try:
                _t_groups._read()
            finally:
                self.groups.append(_t_groups)

        self.padding = []
        i = 0
        while not self._io.is_eof():
            self.padding.append(self._io.read_u1())
            if not self.padding[i] == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding[i], self._io, u"/seq/8")
            i += 1

        self._dirty = False


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.background._fetch_instances()
        for i in range(len(self.groups)):
            pass
            self.groups[i]._fetch_instances()

        for i in range(len(self.padding)):
            pass



    def _write__seq(self, io=None):
        super(DiyType03, self)._write__seq(io)
        self.header._write__seq(self._io)
        self._io.write_bytes(self.body_type)
        self._io.write_u1(int(self.effect))
        self._io.write_u1(self.speed)
        self._io.write_u1(self.brightness)
        self.background._write__seq(self._io)
        self._io.write_u1(self.num_groups)
        for i in range(len(self.groups)):
            pass
            self.groups[i]._write__seq(self._io)

        for i in range(len(self.padding)):
            pass
            if self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())
            self._io.write_u1(self.padding[i])

        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.body_type) != 1:
            raise kaitaistruct.ConsistencyError(u"body_type", 1, len(self.body_type))
        if not self.body_type == b"\x03":
            raise kaitaistruct.ValidationNotEqualError(b"\x03", self.body_type, None, u"/seq/1")
        if len(self.groups) != self.num_groups:
            raise kaitaistruct.ConsistencyError(u"groups", self.num_groups, len(self.groups))
        for i in range(len(self.groups)):
            pass
            if self.groups[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"groups", self._root, self.groups[i]._root)
            if self.groups[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"groups", self, self.groups[i]._parent)

        for i in range(len(self.padding)):
            pass
            if not self.padding[i] == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding[i], None, u"/seq/8")

        self._dirty = False

    class PaintGroup(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiyType03.PaintGroup, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_segment_indices = self._io.read_u1()
            self.fill = govee_shared.GoveeShared.Rgb(self._io)
            self.fill._read()
            self.segment_indices = []
            for i in range(self.num_segment_indices):
                self.segment_indices.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.fill._fetch_instances()
            for i in range(len(self.segment_indices)):
                pass



        def _write__seq(self, io=None):
            super(DiyType03.PaintGroup, self)._write__seq(io)
            self._io.write_u1(self.num_segment_indices)
            self.fill._write__seq(self._io)
            for i in range(len(self.segment_indices)):
                pass
                self._io.write_u1(self.segment_indices[i])



        def _check(self):
            if len(self.segment_indices) != self.num_segment_indices:
                raise kaitaistruct.ConsistencyError(u"segment_indices", self.num_segment_indices, len(self.segment_indices))
            for i in range(len(self.segment_indices)):
                pass

            self._dirty = False



