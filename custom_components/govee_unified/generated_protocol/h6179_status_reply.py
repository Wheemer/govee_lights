# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6179StatusReply(ReadWriteKaitaiStruct):
    """SPECULATIVE H6179 compatibility hypothesis, owner confirmations #448:
    exact-SKU status replies use a
    20-byte 0xaa envelope with the candidate domain, mode, timer, sleep, wake,
    limit, version, brightness, and colour layouts below.
    An owner report for hardware 1.00.01 and firmware 1.00.08 in
    jacobEAdamson/ha-govee-led-ble#1 identifies music replies containing a stored
    RGB triplet even in automatic-colour mode, plus static RGB/Kelvin replies.
    Only abbreviated payloads are available, not complete official-app captures.
    Unresolved assumptions include other revisions, selectors and field meanings,
    string encoding, timer count rules, opaque tails, and the XOR checksum byte.
    """

    class HardwareSelector(IntEnum):
        primary = 3

    class ModeSelector(IntEnum):
        scene = 4
        diy = 10
        static = 13
        music = 14

    class MusicEffect(IntEnum):
        mode_0 = 0
        mode_1 = 1

    class StatusDomain(IntEnum):
        power = 1
        brightness = 4
        mode = 5
        firmware = 6
        hardware = 7
        limit = 14
        sleep = 17
        wake = 18
        timers = 35
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6179StatusReply, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\xAA", self.header, self._io, u"/seq/0")
        self.domain = KaitaiStream.resolve_enum(H6179StatusReply.StatusDomain, self._io.read_u1())
        _on = self.domain
        if _on == H6179StatusReply.StatusDomain.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.firmware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.VersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.hardware:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.HardwareVersionBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.limit:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.LimitBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.power:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.PowerBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.sleep:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.SleepBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.timers:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.TimersBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6179StatusReply.StatusDomain.wake:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6179StatusReply.WakeBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.domain
        if _on == H6179StatusReply.StatusDomain.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.firmware:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.hardware:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.limit:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.mode:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.power:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.sleep:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.timers:
            pass
            self.body._fetch_instances()
        elif _on == H6179StatusReply.StatusDomain.wake:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6179StatusReply, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.domain))
        _on = self.domain
        if _on == H6179StatusReply.StatusDomain.brightness:
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
        elif _on == H6179StatusReply.StatusDomain.firmware:
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
        elif _on == H6179StatusReply.StatusDomain.hardware:
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
        elif _on == H6179StatusReply.StatusDomain.limit:
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
        elif _on == H6179StatusReply.StatusDomain.mode:
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
        elif _on == H6179StatusReply.StatusDomain.power:
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
        elif _on == H6179StatusReply.StatusDomain.sleep:
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
        elif _on == H6179StatusReply.StatusDomain.timers:
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
        elif _on == H6179StatusReply.StatusDomain.wake:
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
        if _on == H6179StatusReply.StatusDomain.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.firmware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.hardware:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.limit:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.mode:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.power:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.sleep:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.timers:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6179StatusReply.StatusDomain.wake:
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
            super(H6179StatusReply.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.raw_brightness = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.raw_brightness)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class DiyBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.DiyBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.diy_id = self._io.read_u2le()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.DiyBody, self)._write__seq(io)
            self._io.write_u2le(self.diy_id)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class HardwareVersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.HardwareVersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = KaitaiStream.resolve_enum(H6179StatusReply.HardwareSelector, self._io.read_u1())
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.HardwareVersionBody, self)._write__seq(io)
            self._io.write_u1(int(self.selector))
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class LimitBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.LimitBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.LimitBody, self)._write__seq(io)
            self._io.write_u1(self.value)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def is_enabled(self):
            if hasattr(self, '_m_is_enabled'):
                return self._m_is_enabled

            self._m_is_enabled = self.value == 1
            return getattr(self, '_m_is_enabled', None)

        def _invalidate_is_enabled(self):
            del self._m_is_enabled

    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mode = KaitaiStream.resolve_enum(H6179StatusReply.ModeSelector, self._io.read_u1())
            _on = self.mode
            if _on == H6179StatusReply.ModeSelector.diy:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6179StatusReply.DiyBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6179StatusReply.ModeSelector.music:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6179StatusReply.MusicBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6179StatusReply.ModeSelector.scene:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6179StatusReply.SceneBody(_io__raw_detail, self, self._root)
                self.detail._read()
            elif _on == H6179StatusReply.ModeSelector.static:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6179StatusReply.StaticBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.mode
            if _on == H6179StatusReply.ModeSelector.diy:
                pass
                self.detail._fetch_instances()
            elif _on == H6179StatusReply.ModeSelector.music:
                pass
                self.detail._fetch_instances()
            elif _on == H6179StatusReply.ModeSelector.scene:
                pass
                self.detail._fetch_instances()
            elif _on == H6179StatusReply.ModeSelector.static:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.mode))
            _on = self.mode
            if _on == H6179StatusReply.ModeSelector.diy:
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
            elif _on == H6179StatusReply.ModeSelector.music:
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
            elif _on == H6179StatusReply.ModeSelector.scene:
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
            elif _on == H6179StatusReply.ModeSelector.static:
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
            if _on == H6179StatusReply.ModeSelector.diy:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6179StatusReply.ModeSelector.music:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6179StatusReply.ModeSelector.scene:
                pass
                if self.detail._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"detail", self._root, self.detail._root)
                if self.detail._parent != self:
                    raise kaitaistruct.ConsistencyError(u"detail", self, self.detail._parent)
            elif _on == H6179StatusReply.ModeSelector.static:
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
            super(H6179StatusReply.MusicBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.music_id = KaitaiStream.resolve_enum(H6179StatusReply.MusicEffect, self._io.read_u1())
            self.sensitivity = self._io.read_u1()
            self.colour_mode = self._io.read_u1()
            self.fixed_colour = govee_shared.GoveeShared.Rgb(self._io)
            self.fixed_colour._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.fixed_colour._fetch_instances()


        def _write__seq(self, io=None):
            super(H6179StatusReply.MusicBody, self)._write__seq(io)
            self._io.write_u1(int(self.music_id))
            self._io.write_u1(self.sensitivity)
            self._io.write_u1(self.colour_mode)
            self.fixed_colour._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def automatic_colour(self):
            if hasattr(self, '_m_automatic_colour'):
                return self._m_automatic_colour

            self._m_automatic_colour = self.colour_mode == 0
            return getattr(self, '_m_automatic_colour', None)

        def _invalidate_automatic_colour(self):
            del self._m_automatic_colour

    class PowerBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.PowerBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.state = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.PowerBody, self)._write__seq(io)
            self._io.write_u1(self.state)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def is_on(self):
            if hasattr(self, '_m_is_on'):
                return self._m_is_on

            self._m_is_on = self.state == 1
            return getattr(self, '_m_is_on', None)

        def _invalidate_is_on(self):
            del self._m_is_on

    class SceneBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.SceneBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.scene_id = self._io.read_u2le()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.SceneBody, self)._write__seq(io)
            self._io.write_u2le(self.scene_id)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SleepBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.SleepBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.state = self._io.read_u1()
            self.start_brightness = self._io.read_u1()
            self.duration_minutes = self._io.read_u1()
            self.remaining_minutes = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.SleepBody, self)._write__seq(io)
            self._io.write_u1(self.state)
            self._io.write_u1(self.start_brightness)
            self._io.write_u1(self.duration_minutes)
            self._io.write_u1(self.remaining_minutes)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def is_enabled(self):
            if hasattr(self, '_m_is_enabled'):
                return self._m_is_enabled

            self._m_is_enabled = self.state == 1
            return getattr(self, '_m_is_enabled', None)

        def _invalidate_is_enabled(self):
            del self._m_is_enabled

    class StaticBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.StaticBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.colour = govee_shared.GoveeShared.Rgb(self._io)
            self.colour._read()
            self.kelvin = self._io.read_u2be()
            self.temperature_colour = govee_shared.GoveeShared.Rgb(self._io)
            self.temperature_colour._read()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.colour._fetch_instances()
            self.temperature_colour._fetch_instances()


        def _write__seq(self, io=None):
            super(H6179StatusReply.StaticBody, self)._write__seq(io)
            self.colour._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self.temperature_colour._write__seq(self._io)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class TimerRecord(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.TimerRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.enable_and_action = self._io.read_u1()
            self.hour = self._io.read_u1()
            self.minute = self._io.read_u1()
            self.repeat_mask = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.TimerRecord, self)._write__seq(io)
            self._io.write_u1(self.enable_and_action)
            self._io.write_u1(self.hour)
            self._io.write_u1(self.minute)
            self._io.write_u1(self.repeat_mask)


        def _check(self):
            self._dirty = False

        @property
        def explicit_weekday_mask(self):
            if hasattr(self, '_m_explicit_weekday_mask'):
                return self._m_explicit_weekday_mask

            self._m_explicit_weekday_mask = self.repeat_mask & 127
            return getattr(self, '_m_explicit_weekday_mask', None)

        def _invalidate_explicit_weekday_mask(self):
            del self._m_explicit_weekday_mask
        @property
        def has_explicit_weekdays(self):
            if hasattr(self, '_m_has_explicit_weekdays'):
                return self._m_has_explicit_weekdays

            self._m_has_explicit_weekdays =  ((self.repeat_mask & 128 != 0) and (self.repeat_mask & 127 != 0)) 
            return getattr(self, '_m_has_explicit_weekdays', None)

        def _invalidate_has_explicit_weekdays(self):
            del self._m_has_explicit_weekdays
        @property
        def is_enabled(self):
            if hasattr(self, '_m_is_enabled'):
                return self._m_is_enabled

            self._m_is_enabled = self.enable_and_action & 128 != 0
            return getattr(self, '_m_is_enabled', None)

        def _invalidate_is_enabled(self):
            del self._m_is_enabled
        @property
        def is_one_time(self):
            if hasattr(self, '_m_is_one_time'):
                return self._m_is_one_time

            self._m_is_one_time = self.repeat_mask == 128
            return getattr(self, '_m_is_one_time', None)

        def _invalidate_is_one_time(self):
            del self._m_is_one_time
        @property
        def repeats_every_day(self):
            if hasattr(self, '_m_repeats_every_day'):
                return self._m_repeats_every_day

            self._m_repeats_every_day = self.repeat_mask == 0
            return getattr(self, '_m_repeats_every_day', None)

        def _invalidate_repeats_every_day(self):
            del self._m_repeats_every_day
        @property
        def turns_on(self):
            if hasattr(self, '_m_turns_on'):
                return self._m_turns_on

            self._m_turns_on = self.enable_and_action & 1 != 0
            return getattr(self, '_m_turns_on', None)

        def _invalidate_turns_on(self):
            del self._m_turns_on
        @property
        def unknown_flags(self):
            if hasattr(self, '_m_unknown_flags'):
                return self._m_unknown_flags

            self._m_unknown_flags = self.enable_and_action & 126
            return getattr(self, '_m_unknown_flags', None)

        def _invalidate_unknown_flags(self):
            del self._m_unknown_flags

    class TimersBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.TimersBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_u1()
            self.slots = []
            for i in range((4 if self.selector == 255 else 1)):
                _t_slots = H6179StatusReply.TimerRecord(self._io, self, self._root)
                try:
                    _t_slots._read()
                finally:
                    self.slots.append(_t_slots)

            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.slots)):
                pass
                self.slots[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(H6179StatusReply.TimersBody, self)._write__seq(io)
            self._io.write_u1(self.selector)
            for i in range(len(self.slots)):
                pass
                self.slots[i]._write__seq(self._io)

            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.slots) != (4 if self.selector == 255 else 1):
                raise kaitaistruct.ConsistencyError(u"slots", (4 if self.selector == 255 else 1), len(self.slots))
            for i in range(len(self.slots)):
                pass
                if self.slots[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"slots", self._root, self.slots[i]._root)
                if self.slots[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"slots", self, self.slots[i]._parent)

            self._dirty = False


    class VersionBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.VersionBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.VersionBody, self)._write__seq(io)
            self._io.write_bytes((self.text).encode(u"ASCII"))
            self._io.write_u1(0)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"text", -1, KaitaiStream.byte_array_index_of((self.text).encode(u"ASCII"), 0))
            self._dirty = False


    class WakeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6179StatusReply.WakeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.state = self._io.read_u1()
            self.target_brightness = self._io.read_u1()
            self.hour = self._io.read_u1()
            self.minute = self._io.read_u1()
            self.repeat_mask = self._io.read_u1()
            self.duration_minutes = self._io.read_u1()
            self.opaque = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6179StatusReply.WakeBody, self)._write__seq(io)
            self._io.write_u1(self.state)
            self._io.write_u1(self.target_brightness)
            self._io.write_u1(self.hour)
            self._io.write_u1(self.minute)
            self._io.write_u1(self.repeat_mask)
            self._io.write_u1(self.duration_minutes)
            self._io.write_bytes(self.opaque)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"opaque", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def explicit_weekday_mask(self):
            if hasattr(self, '_m_explicit_weekday_mask'):
                return self._m_explicit_weekday_mask

            self._m_explicit_weekday_mask = self.repeat_mask & 127
            return getattr(self, '_m_explicit_weekday_mask', None)

        def _invalidate_explicit_weekday_mask(self):
            del self._m_explicit_weekday_mask
        @property
        def has_explicit_weekdays(self):
            if hasattr(self, '_m_has_explicit_weekdays'):
                return self._m_has_explicit_weekdays

            self._m_has_explicit_weekdays =  ((self.repeat_mask & 128 != 0) and (self.repeat_mask & 127 != 0)) 
            return getattr(self, '_m_has_explicit_weekdays', None)

        def _invalidate_has_explicit_weekdays(self):
            del self._m_has_explicit_weekdays
        @property
        def is_enabled(self):
            if hasattr(self, '_m_is_enabled'):
                return self._m_is_enabled

            self._m_is_enabled = self.state == 1
            return getattr(self, '_m_is_enabled', None)

        def _invalidate_is_enabled(self):
            del self._m_is_enabled
        @property
        def is_one_time(self):
            if hasattr(self, '_m_is_one_time'):
                return self._m_is_one_time

            self._m_is_one_time = self.repeat_mask == 128
            return getattr(self, '_m_is_one_time', None)

        def _invalidate_is_one_time(self):
            del self._m_is_one_time
        @property
        def repeats_every_day(self):
            if hasattr(self, '_m_repeats_every_day'):
                return self._m_repeats_every_day

            self._m_repeats_every_day = self.repeat_mask == 0
            return getattr(self, '_m_repeats_every_day', None)

        def _invalidate_repeats_every_day(self):
            del self._m_repeats_every_day


