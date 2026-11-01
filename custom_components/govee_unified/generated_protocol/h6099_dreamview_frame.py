# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099DreamviewFrame(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 issue #258, H66A0 issue #408.  Android 7.6.01 MovieFeastV2
    control selects module 0x60.  Group switch writes {on, 1}, queries with
    discriminator 1, and reads the first reply byte as on.  Individual module 0x60
    commands establish the member brightness, member connection, same brightness,
    saturation, video settings, sound, and delete layouts.  Brightness reads consume all
    16 returned bytes; connection reads copy 10 bytes (goods type 191 supports
    seven members; goods type 327 H66A0 supports ten members).  Never trim zeros
    or infer membership from slots.  Video settings encode apply area (0 All,
    1 Part) and content mode (0 Game, 1 Movie).  Issue #430 reports H66A0
    Part/Game and Part/Movie writes and individual readback while the group stays
    connected.  Unknown values remain raw bytes.  Unknown trailing bytes,
    slot occupancy, and reply freshness beyond
    request timing are unresolved.  No digest 0x0c or camera heuristic is
    modelled.  The H66A0 owner reports in issue #408 that writes for 0x01, 0x03,
    0x04, 0x05, 0x09, 0x0b and 0x0d match official-app captures, alongside the
    brightness query and a parsed connection reply.  Attributable raw captures
    are not attached.  Other reads remain structurally evidenced candidates.
    No official-app capture or owner qualification exists
    for H6099.
    This root does not model command ACKs.
    H6097 issue #431 independently selects the same module and group-switch
    format, with a seven-member product ceiling.  Operation admission remains
    explicit in its own profile; no membership readback is implied.
    """

    class ApplyArea(IntEnum):
        all = 0
        part = 1

    class Command(IntEnum):
        switch_group = 1
        member_brightness = 3
        same_brightness = 4
        member_connect = 5
        saturation = 9
        video_settings = 10
        sound = 11
        delete_group = 13

    class ContentMode(IntEnum):
        game = 0
        movie = 1

    class Header(IntEnum):
        write = 51
        read = 170
    def __init__(self, is_query, _io=None, _parent=None, _root=None):
        super(H6099DreamviewFrame, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.is_query = is_query

    def _read(self):
        self.header = KaitaiStream.resolve_enum(H6099DreamviewFrame.Header, self._io.read_u1())
        self.module = self._io.read_bytes(1)
        if not self.module == b"\x60":
            raise kaitaistruct.ValidationNotEqualError(b"\x60", self.module, self._io, u"/seq/1")
        self.command = KaitaiStream.resolve_enum(H6099DreamviewFrame.Command, self._io.read_u1())
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
            pass
            self._raw_body = self._io.read_bytes(16)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099DreamviewFrame.QueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == 170:
            pass
            self._raw_body = self._io.read_bytes(16)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099DreamviewFrame.StatusBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == 51:
            pass
            self._raw_body = self._io.read_bytes(16)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6099DreamviewFrame.WriteBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(16)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
            pass
            self.body._fetch_instances()
        elif _on == 170:
            pass
            self.body._fetch_instances()
        elif _on == 51:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6099DreamviewFrame, self)._write__seq(io)
        self._io.write_u1(int(self.header))
        self._io.write_bytes(self.module)
        self._io.write_u1(int(self.command))
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(16)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (16))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 16, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        elif _on == 170:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(16)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (16))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 16, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        elif _on == 51:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(16)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (16))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != 16:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", 16, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        else:
            pass
            self._io.write_bytes(self.body)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.module) != 1:
            raise kaitaistruct.ConsistencyError(u"module", 1, len(self.module))
        if not self.module == b"\x60":
            raise kaitaistruct.ValidationNotEqualError(b"\x60", self.module, None, u"/seq/1")
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == 170:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == 51:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        else:
            pass
            if len(self.body) != 16:
                raise kaitaistruct.ConsistencyError(u"body", 16, len(self.body))
        self._dirty = False

    class QueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099DreamviewFrame.QueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                self.discriminator = self._io.read_bytes(1)
                if not self.discriminator == b"\x01":
                    raise kaitaistruct.ValidationNotEqualError(b"\x01", self.discriminator, self._io, u"/types/query_body/seq/0")

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass



        def _write__seq(self, io=None):
            super(H6099DreamviewFrame.QueryBody, self)._write__seq(io)
            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                self._io.write_bytes(self.discriminator)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                if len(self.discriminator) != 1:
                    raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
                if not self.discriminator == b"\x01":
                    raise kaitaistruct.ValidationNotEqualError(b"\x01", self.discriminator, None, u"/types/query_body/seq/0")

            self._dirty = False


    class StatusBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099DreamviewFrame.StatusBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass
                self.enabled = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass
                self.brightness_bytes = self._io.read_bytes(16)

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass
                self.connection_bytes = self._io.read_bytes(10)

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass
                self.saturation = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self.apply_area = KaitaiStream.resolve_enum(H6099DreamviewFrame.ApplyArea, self._io.read_u1())

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self.content_mode = KaitaiStream.resolve_enum(H6099DreamviewFrame.ContentMode, self._io.read_u1())

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass
                self.softness = self._io.read_u1()

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass



        def _write__seq(self, io=None):
            super(H6099DreamviewFrame.StatusBody, self)._write__seq(io)
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass
                self._io.write_u1(self.enabled)

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass
                self._io.write_bytes(self.brightness_bytes)

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass
                self._io.write_bytes(self.connection_bytes)

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass
                self._io.write_u1(self.saturation)

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.apply_area))

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.content_mode))

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass
                self._io.write_u1(self.softness)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass
                if len(self.brightness_bytes) != 16:
                    raise kaitaistruct.ConsistencyError(u"brightness_bytes", 16, len(self.brightness_bytes))

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass
                if len(self.connection_bytes) != 10:
                    raise kaitaistruct.ConsistencyError(u"connection_bytes", 10, len(self.connection_bytes))

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass

            self._dirty = False


    class WriteBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099DreamviewFrame.WriteBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass
                self.enabled = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                self.discriminator = self._io.read_bytes(1)
                if not self.discriminator == b"\x01":
                    raise kaitaistruct.ValidationNotEqualError(b"\x01", self.discriminator, self._io, u"/types/write_body/seq/1")

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass
                self.level = self._io.read_u1()

            if  ((self._root.command == H6099DreamviewFrame.Command.member_brightness) or (self._root.command == H6099DreamviewFrame.Command.member_connect)) :
                pass
                self.index = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass
                self.connected = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass
                self.saturation = self._io.read_u1()

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self.apply_area = KaitaiStream.resolve_enum(H6099DreamviewFrame.ApplyArea, self._io.read_u1())

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self.content_mode = KaitaiStream.resolve_enum(H6099DreamviewFrame.ContentMode, self._io.read_u1())

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass
                self.softness = self._io.read_u1()

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass

            if  ((self._root.command == H6099DreamviewFrame.Command.member_brightness) or (self._root.command == H6099DreamviewFrame.Command.member_connect)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass



        def _write__seq(self, io=None):
            super(H6099DreamviewFrame.WriteBody, self)._write__seq(io)
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass
                self._io.write_u1(self.enabled)

            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                self._io.write_bytes(self.discriminator)

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass
                self._io.write_u1(self.level)

            if  ((self._root.command == H6099DreamviewFrame.Command.member_brightness) or (self._root.command == H6099DreamviewFrame.Command.member_connect)) :
                pass
                self._io.write_u1(self.index)

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass
                self._io.write_u1(self.connected)

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass
                self._io.write_u1(self.saturation)

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.apply_area))

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.content_mode))

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass
                self._io.write_u1(self.softness)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if  ((self._root.command == H6099DreamviewFrame.Command.switch_group) or (self._root.command == H6099DreamviewFrame.Command.same_brightness) or (self._root.command == H6099DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.switch_group:
                pass
                if len(self.discriminator) != 1:
                    raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
                if not self.discriminator == b"\x01":
                    raise kaitaistruct.ValidationNotEqualError(b"\x01", self.discriminator, None, u"/types/write_body/seq/1")

            if self._root.command == H6099DreamviewFrame.Command.member_brightness:
                pass

            if  ((self._root.command == H6099DreamviewFrame.Command.member_brightness) or (self._root.command == H6099DreamviewFrame.Command.member_connect)) :
                pass

            if self._root.command == H6099DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6099DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6099DreamviewFrame.Command.sound:
                pass

            self._dirty = False


    @property
    def body_size(self):
        if hasattr(self, '_m_body_size'):
            return self._m_body_size

        self._m_body_size = 16
        return getattr(self, '_m_body_size', None)

    def _invalidate_body_size(self):
        del self._m_body_size
    @property
    def discriminator_size(self):
        if hasattr(self, '_m_discriminator_size'):
            return self._m_discriminator_size

        self._m_discriminator_size = (1 if self.command == H6099DreamviewFrame.Command.switch_group else 0)
        return getattr(self, '_m_discriminator_size', None)

    def _invalidate_discriminator_size(self):
        del self._m_discriminator_size
    @property
    def discriminator_value(self):
        if hasattr(self, '_m_discriminator_value'):
            return self._m_discriminator_value

        self._m_discriminator_value = 1
        return getattr(self, '_m_discriminator_value', None)

    def _invalidate_discriminator_value(self):
        del self._m_discriminator_value
    @property
    def module_value(self):
        if hasattr(self, '_m_module_value'):
            return self._m_module_value

        self._m_module_value = 96
        return getattr(self, '_m_module_value', None)

    def _invalidate_module_value(self):
        del self._m_module_value

