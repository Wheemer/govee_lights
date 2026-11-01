# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199ControlPayload(ReadWriteKaitaiStruct):
    """SPECULATIVE H6199 additions for issue #294.  Android 7.6.01 exact-model
    camera settings and light control behaviour plus direct register tests on HW3.02.01,
    FW1.10.04, WiFi HW1.03.00/FW1.00.33, Pact2/1 establish the hypothesis.
    These are NOT official-app BLE captures or schema promotion evidence.
    Direction 0/1 means clockwise/anticlockwise; camera position 0/1 top/bottom.
    Camera 0 absent and 2 incompatible are app-only; only 1 healthy was tested.
    A3 and static detail expose Color > Subsection > Gradient, not HA transition
    duration or a proven visual blending algorithm.  DIY code254 readback does
    not establish populated content, uploads or playback.  Other revisions and
    unknown tails remain unqualified.
    """

    class CameraStatus(IntEnum):
        absent = 0
        healthy = 1
        incompatible = 2
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6199ControlPayload, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.value = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6199ControlPayload, self)._write__seq(io)
        self._io.write_u1(self.value)
        self._io.write_bytes(self.unknown_tail)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


    def _check(self):
        self._dirty = False

    class CameraState(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199ControlPayload.CameraState, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = KaitaiStream.resolve_enum(H6199ControlPayload.CameraStatus, self._io.read_u1())
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199ControlPayload.CameraState, self)._write__seq(io)
            self._io.write_u1(int(self.value))
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class DiySelector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199ControlPayload.DiySelector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.code = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199ControlPayload.DiySelector, self)._write__seq(io)
            self._io.write_u2le(self.code)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class StaticDetail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199ControlPayload.StaticDetail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.gradient = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199ControlPayload.StaticDetail, self)._write__seq(io)
            self._io.write_u1(self.gradient)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class WriteValue(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199ControlPayload.WriteValue, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199ControlPayload.WriteValue, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



