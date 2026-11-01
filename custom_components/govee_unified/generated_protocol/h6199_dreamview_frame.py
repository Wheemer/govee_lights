# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199DreamviewFrame(ReadWriteKaitaiStruct):
    """SPECULATIVE H6199 issue #438.  Legacy group controls use independent
    command opcodes and seventeen-byte bodies, not the newer module-0x60
    group layout.  Same brightness alone uses module 0x60 command 0x04;
    its admission requires main hardware 3.02.01 and firmware 1.09.00.
    The product fallback is five members, independently of the seventeen
    brightness bytes and ten connection bytes returned by individual reads.
    Member records use the shared A3 type-0x50 layout.  Completion replies
    match protocol and command with a zero success byte; they establish
    acceptance, not membership, rendering or synchronisation.
    Issue #294 reports an enable-query response, not group qualification.
    Official-app captures, revision differences, negative completion replies,
    reply tails, slot identity and maximum capacity remain unqualified.
    """

    class AckHeader(IntEnum):
        write = 51
        upload = 163

    class AckOperation(IntEnum):
        replace_group = 80
        delete_group = 86

    class ApplyArea(IntEnum):
        all = 0
        part = 1

    class Command(IntEnum):
        member_connect = 67
        member_brightness = 80
        saturation = 81
        video_settings = 82
        sound = 83
        switch_group = 84
        delete_group = 86
        same_brightness = 96

    class ContentMode(IntEnum):
        game = 0
        movie = 1

    class Header(IntEnum):
        write = 51
        read = 170
    def __init__(self, is_query, _io=None, _parent=None, _root=None):
        super(H6199DreamviewFrame, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.is_query = is_query

    def _read(self):
        self.header = KaitaiStream.resolve_enum(H6199DreamviewFrame.Header, self._io.read_u1())
        if not  ((self.header == H6199DreamviewFrame.Header.write) or (self.header == H6199DreamviewFrame.Header.read)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.header, self._io, u"/seq/0")
        self.command = KaitaiStream.resolve_enum(H6199DreamviewFrame.Command, self._io.read_u1())
        if not  ((self.command == H6199DreamviewFrame.Command.member_connect) or (self.command == H6199DreamviewFrame.Command.member_brightness) or (self.command == H6199DreamviewFrame.Command.saturation) or (self.command == H6199DreamviewFrame.Command.video_settings) or (self.command == H6199DreamviewFrame.Command.sound) or (self.command == H6199DreamviewFrame.Command.switch_group) or (self.command == H6199DreamviewFrame.Command.delete_group) or (self.command == H6199DreamviewFrame.Command.same_brightness)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.command, self._io, u"/seq/1")
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6199DreamviewFrame.QueryBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == 170:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6199DreamviewFrame.StatusBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == 51:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6199DreamviewFrame.WriteBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
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
        super(H6199DreamviewFrame, self)._write__seq(io)
        self._io.write_u1(int(self.header))
        self._io.write_u1(int(self.command))
        _on = (0 if self.is_query else int(self.header))
        if _on == 0:
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
        elif _on == 170:
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
        elif _on == 51:
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
        if not  ((self.header == H6199DreamviewFrame.Header.write) or (self.header == H6199DreamviewFrame.Header.read)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.header, None, u"/seq/0")
        if not  ((self.command == H6199DreamviewFrame.Command.member_connect) or (self.command == H6199DreamviewFrame.Command.member_brightness) or (self.command == H6199DreamviewFrame.Command.saturation) or (self.command == H6199DreamviewFrame.Command.video_settings) or (self.command == H6199DreamviewFrame.Command.sound) or (self.command == H6199DreamviewFrame.Command.switch_group) or (self.command == H6199DreamviewFrame.Command.delete_group) or (self.command == H6199DreamviewFrame.Command.same_brightness)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.command, None, u"/seq/1")
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
            if len(self.body) != 17:
                raise kaitaistruct.ConsistencyError(u"body", 17, len(self.body))
        self._dirty = False

    class Acknowledgement(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199DreamviewFrame.Acknowledgement, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = KaitaiStream.resolve_enum(H6199DreamviewFrame.AckHeader, self._io.read_u1())
            if not  ((self.header == H6199DreamviewFrame.AckHeader.upload) or (self.header == H6199DreamviewFrame.AckHeader.write)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.header, self._io, u"/types/acknowledgement/seq/0")
            self.operation = KaitaiStream.resolve_enum(H6199DreamviewFrame.AckOperation, self._io.read_u1())
            _ = self.operation
            if not  (( ((self.header == H6199DreamviewFrame.AckHeader.upload) and (self.operation == H6199DreamviewFrame.AckOperation.replace_group)) ) or ( ((self.header == H6199DreamviewFrame.AckHeader.write) and (self.operation == H6199DreamviewFrame.AckOperation.delete_group)) )) :
                raise kaitaistruct.ValidationExprError(self.operation, self._io, u"/types/acknowledgement/seq/1")
            self.status = self._io.read_u1()
            self.unknown = self._io.read_bytes(16)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199DreamviewFrame.Acknowledgement, self)._write__seq(io)
            self._io.write_u1(int(self.header))
            self._io.write_u1(int(self.operation))
            self._io.write_u1(self.status)
            self._io.write_bytes(self.unknown)
            self._io.write_u1(self.checksum)


        def _check(self):
            if not  ((self.header == H6199DreamviewFrame.AckHeader.upload) or (self.header == H6199DreamviewFrame.AckHeader.write)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.header, None, u"/types/acknowledgement/seq/0")
            _ = self.operation
            if not  (( ((self.header == H6199DreamviewFrame.AckHeader.upload) and (self.operation == H6199DreamviewFrame.AckOperation.replace_group)) ) or ( ((self.header == H6199DreamviewFrame.AckHeader.write) and (self.operation == H6199DreamviewFrame.AckOperation.delete_group)) )) :
                raise kaitaistruct.ValidationExprError(self.operation, None, u"/types/acknowledgement/seq/1")
            if len(self.unknown) != 16:
                raise kaitaistruct.ConsistencyError(u"unknown", 16, len(self.unknown))
            self._dirty = False

        @property
        def is_success(self):
            if hasattr(self, '_m_is_success'):
                return self._m_is_success

            self._m_is_success = self.status == 0
            return getattr(self, '_m_is_success', None)

        def _invalidate_is_success(self):
            del self._m_is_success

    class QueryBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199DreamviewFrame.QueryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self.discriminator = self._io.read_bytes(1)
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, self._io, u"/types/query_body/seq/0")

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass



        def _write__seq(self, io=None):
            super(H6199DreamviewFrame.QueryBody, self)._write__seq(io)
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self._io.write_bytes(self.discriminator)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                if len(self.discriminator) != 1:
                    raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, None, u"/types/query_body/seq/0")

            self._dirty = False


    class StatusBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199DreamviewFrame.StatusBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self.discriminator = self._io.read_bytes(1)
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, self._io, u"/types/status_body/seq/0")

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass
                self.enabled = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass
                self.brightness_bytes = self._io.read_bytes(17)

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass
                self.connection_bytes = self._io.read_bytes(10)

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass
                self.saturation = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self.apply_area = KaitaiStream.resolve_enum(H6199DreamviewFrame.ApplyArea, self._io.read_u1())

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self.content_mode = KaitaiStream.resolve_enum(H6199DreamviewFrame.ContentMode, self._io.read_u1())

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass
                self.softness = self._io.read_u1()

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass



        def _write__seq(self, io=None):
            super(H6199DreamviewFrame.StatusBody, self)._write__seq(io)
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self._io.write_bytes(self.discriminator)

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass
                self._io.write_u1(self.enabled)

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass
                self._io.write_bytes(self.brightness_bytes)

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass
                self._io.write_bytes(self.connection_bytes)

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass
                self._io.write_u1(self.saturation)

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.apply_area))

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.content_mode))

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass
                self._io.write_u1(self.softness)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                if len(self.discriminator) != 1:
                    raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, None, u"/types/status_body/seq/0")

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass
                if len(self.brightness_bytes) != 17:
                    raise kaitaistruct.ConsistencyError(u"brightness_bytes", 17, len(self.brightness_bytes))

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass
                if len(self.connection_bytes) != 10:
                    raise kaitaistruct.ConsistencyError(u"connection_bytes", 10, len(self.connection_bytes))

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass

            self._dirty = False


    class UploadFrame(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199DreamviewFrame.UploadFrame, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = self._io.read_bytes(1)
            if not self.header == b"\xA3":
                raise kaitaistruct.ValidationNotEqualError(b"\xA3", self.header, self._io, u"/types/upload_frame/seq/0")
            self.index = self._io.read_u1()
            self.chunk = self._io.read_bytes(17)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199DreamviewFrame.UploadFrame, self)._write__seq(io)
            self._io.write_bytes(self.header)
            self._io.write_u1(self.index)
            self._io.write_bytes(self.chunk)
            self._io.write_u1(self.checksum)


        def _check(self):
            if len(self.header) != 1:
                raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
            if not self.header == b"\xA3":
                raise kaitaistruct.ValidationNotEqualError(b"\xA3", self.header, None, u"/types/upload_frame/seq/0")
            if len(self.chunk) != 17:
                raise kaitaistruct.ConsistencyError(u"chunk", 17, len(self.chunk))
            self._dirty = False


    class WriteBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199DreamviewFrame.WriteBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self.discriminator = self._io.read_bytes(1)
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, self._io, u"/types/write_body/seq/0")

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass
                self.enabled = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass
                self.level = self._io.read_u1()

            if  ((self._root.command == H6199DreamviewFrame.Command.member_brightness) or (self._root.command == H6199DreamviewFrame.Command.member_connect)) :
                pass
                self.index = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass
                self.connected = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass
                self.saturation = self._io.read_u1()

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self.apply_area = KaitaiStream.resolve_enum(H6199DreamviewFrame.ApplyArea, self._io.read_u1())

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self.content_mode = KaitaiStream.resolve_enum(H6199DreamviewFrame.ContentMode, self._io.read_u1())

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass
                self.softness = self._io.read_u1()

            self.unknown = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass

            if  ((self._root.command == H6199DreamviewFrame.Command.member_brightness) or (self._root.command == H6199DreamviewFrame.Command.member_connect)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass



        def _write__seq(self, io=None):
            super(H6199DreamviewFrame.WriteBody, self)._write__seq(io)
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                self._io.write_bytes(self.discriminator)

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass
                self._io.write_u1(self.enabled)

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass
                self._io.write_u1(self.level)

            if  ((self._root.command == H6199DreamviewFrame.Command.member_brightness) or (self._root.command == H6199DreamviewFrame.Command.member_connect)) :
                pass
                self._io.write_u1(self.index)

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass
                self._io.write_u1(self.connected)

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass
                self._io.write_u1(self.saturation)

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.apply_area))

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass
                self._io.write_u1(int(self.content_mode))

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass
                self._io.write_u1(self.softness)

            self._io.write_bytes(self.unknown)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self._root.command == H6199DreamviewFrame.Command.same_brightness:
                pass
                if len(self.discriminator) != 1:
                    raise kaitaistruct.ConsistencyError(u"discriminator", 1, len(self.discriminator))
                if not self.discriminator == b"\x04":
                    raise kaitaistruct.ValidationNotEqualError(b"\x04", self.discriminator, None, u"/types/write_body/seq/0")

            if  ((self._root.command == H6199DreamviewFrame.Command.switch_group) or (self._root.command == H6199DreamviewFrame.Command.same_brightness) or (self._root.command == H6199DreamviewFrame.Command.sound)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_brightness:
                pass

            if  ((self._root.command == H6199DreamviewFrame.Command.member_brightness) or (self._root.command == H6199DreamviewFrame.Command.member_connect)) :
                pass

            if self._root.command == H6199DreamviewFrame.Command.member_connect:
                pass

            if self._root.command == H6199DreamviewFrame.Command.saturation:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.video_settings:
                pass

            if self._root.command == H6199DreamviewFrame.Command.sound:
                pass

            self._dirty = False


    @property
    def body_size(self):
        if hasattr(self, '_m_body_size'):
            return self._m_body_size

        self._m_body_size = 17
        return getattr(self, '_m_body_size', None)

    def _invalidate_body_size(self):
        del self._m_body_size
    @property
    def discriminator_size(self):
        if hasattr(self, '_m_discriminator_size'):
            return self._m_discriminator_size

        self._m_discriminator_size = (1 if self.command == H6199DreamviewFrame.Command.same_brightness else 0)
        return getattr(self, '_m_discriminator_size', None)

    def _invalidate_discriminator_size(self):
        del self._m_discriminator_size
    @property
    def discriminator_value(self):
        if hasattr(self, '_m_discriminator_value'):
            return self._m_discriminator_value

        self._m_discriminator_value = 4
        return getattr(self, '_m_discriminator_value', None)

    def _invalidate_discriminator_value(self):
        del self._m_discriminator_value

