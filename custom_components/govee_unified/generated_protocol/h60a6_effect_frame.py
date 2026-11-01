# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h60a6_diy_body
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6EffectFrame(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 support for issue #402.  Compatibility hypothesis:
    native paint bodies use A4, a sixteen-bit frame index/count and subtype 58.
    Frames have a trailing XOR byte.  The start frame contains marker 01,
    count and subtype; the final frame has index FFFF.  Single-data-frame
    uploads include an empty four-byte terminator.  Final frames are not
    padded.  MTU negotiation, acknowledgement timing, other revisions and
    hardware rendering require capture qualification.  A3 DIY uses the same
    subtype but a different body family and framing.  Its reassembled envelope
    embeds the length-bounded DIY body separately from transport fill.
    """

    class Subtype(IntEnum):
        native_effect = 88
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6EffectFrame, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\xA4":
            raise kaitaistruct.ValidationNotEqualError(b"\xA4", self.header, self._io, u"/seq/0")
        self.index = self._io.read_u2le()
        _on = self.index
        if _on == 0:
            pass
            self._raw_body = self._io.read_bytes(self._io.size() - 4)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H60a6EffectFrame.StartBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(self._io.size() - 4)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.index
        if _on == 0:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H60a6EffectFrame, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u2le(self.index)
        _on = self.index
        if _on == 0:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(self._io.size() - 4)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - 4))
            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != self._io.size() - 4:
                    raise kaitaistruct.ConsistencyError(u"raw(body)", self._io.size() - 4, len(self._raw_body))
                parent.write_bytes(self._raw_body)
            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.body._write__seq(_io__raw_body)
        else:
            pass
            if len(self.body) != self._io.size() - 4:
                raise kaitaistruct.ConsistencyError(u"body", self._io.size() - 4, len(self.body))
            self._io.write_bytes(self.body)
        self._io.write_u1(self.checksum)


    def _check(self):
        if len(self.header) != 1:
            raise kaitaistruct.ConsistencyError(u"header", 1, len(self.header))
        if not self.header == b"\xA4":
            raise kaitaistruct.ValidationNotEqualError(b"\xA4", self.header, None, u"/seq/0")
        _on = self.index
        if _on == 0:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        else:
            pass
        self._dirty = False

    class A3Body(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6EffectFrame.A3Body, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.subtype = KaitaiStream.resolve_enum(H60a6EffectFrame.Subtype, self._io.read_u1())
            self.payload = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6EffectFrame.A3Body, self)._write__seq(io)
            self._io.write_u1(int(self.subtype))
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"payload", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class A3Envelope(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6EffectFrame.A3Envelope, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.marker = self._io.read_bytes(1)
            if not self.marker == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.marker, self._io, u"/types/a3_envelope/seq/0")
            self.frame_count = self._io.read_u1()
            self.subtype = KaitaiStream.resolve_enum(H60a6EffectFrame.Subtype, self._io.read_u1())
            if not self.subtype == H60a6EffectFrame.Subtype.native_effect:
                raise kaitaistruct.ValidationNotEqualError(H60a6EffectFrame.Subtype.native_effect, self.subtype, self._io, u"/types/a3_envelope/seq/2")
            self.body = h60a6_diy_body.H60a6DiyBody(self._io)
            self.body._read()
            self.padding = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(H60a6EffectFrame.A3Envelope, self)._write__seq(io)
            self._io.write_bytes(self.marker)
            self._io.write_u1(self.frame_count)
            self._io.write_u1(int(self.subtype))
            self.body._write__seq(self._io)
            self._io.write_bytes(self.padding)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.marker) != 1:
                raise kaitaistruct.ConsistencyError(u"marker", 1, len(self.marker))
            if not self.marker == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.marker, None, u"/types/a3_envelope/seq/0")
            if not self.subtype == H60a6EffectFrame.Subtype.native_effect:
                raise kaitaistruct.ValidationNotEqualError(H60a6EffectFrame.Subtype.native_effect, self.subtype, None, u"/types/a3_envelope/seq/2")
            self._dirty = False


    class StartBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6EffectFrame.StartBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.marker = self._io.read_bytes(1)
            if not self.marker == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.marker, self._io, u"/types/start_body/seq/0")
            self.frame_count = self._io.read_u2le()
            self.subtype = KaitaiStream.resolve_enum(H60a6EffectFrame.Subtype, self._io.read_u1())
            self.payload = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6EffectFrame.StartBody, self)._write__seq(io)
            self._io.write_bytes(self.marker)
            self._io.write_u2le(self.frame_count)
            self._io.write_u1(int(self.subtype))
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"payload", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.marker) != 1:
                raise kaitaistruct.ConsistencyError(u"marker", 1, len(self.marker))
            if not self.marker == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.marker, None, u"/types/start_body/seq/0")
            self._dirty = False



