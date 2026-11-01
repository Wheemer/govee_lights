# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199Pact1WireWrite(ReadWriteKaitaiStruct):
    """SPECULATIVE H6199 Pact 1/1, issue #293.
    Compatibility hypothesis: the legacy producer uses a scaled 20..254 brightness
    register and static-colour selector 0x0b with RGB, a two-byte Kelvin field and
    a little-endian fifteen-bit segment mask.  Runtime authoring permits only
    whole-strip RGB with zero Kelvin; the shared H6199 logical commands retain
    capability checks and optimistic semantics before this wire transform.
    Unresolved assumptions: independent official-app captures at known brightness
    percentages, device qualification of both writes, unused frame bytes and
    command echoes.  This root does not qualify readback or other legacy modes.
    The final byte is the XOR of bytes 0 through 18.
    """

    class CommandOp(IntEnum):
        brightness = 4
        mode = 5

    class ModeSel(IntEnum):
        static_colour = 11
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6199Pact1WireWrite, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H6199Pact1WireWrite.CommandOp, self._io.read_u1())
        _on = self.opcode
        if _on == H6199Pact1WireWrite.CommandOp.brightness:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6199Pact1WireWrite.BrightnessBody(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H6199Pact1WireWrite.CommandOp.mode:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H6199Pact1WireWrite.ModeBody(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H6199Pact1WireWrite.CommandOp.brightness:
            pass
            self.body._fetch_instances()
        elif _on == H6199Pact1WireWrite.CommandOp.mode:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6199Pact1WireWrite, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H6199Pact1WireWrite.CommandOp.brightness:
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
        elif _on == H6199Pact1WireWrite.CommandOp.mode:
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
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, None, u"/seq/0")
        _on = self.opcode
        if _on == H6199Pact1WireWrite.CommandOp.brightness:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H6199Pact1WireWrite.CommandOp.mode:
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
            super(H6199Pact1WireWrite.BrightnessBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.register = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H6199Pact1WireWrite.BrightnessBody, self)._write__seq(io)
            self._io.write_u1(self.register)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ModeBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199Pact1WireWrite.ModeBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub_mode = KaitaiStream.resolve_enum(H6199Pact1WireWrite.ModeSel, self._io.read_u1())
            _on = self.sub_mode
            if _on == H6199Pact1WireWrite.ModeSel.static_colour:
                pass
                self._raw_detail = self._io.read_bytes(16)
                _io__raw_detail = KaitaiStream(BytesIO(self._raw_detail))
                self.detail = H6199Pact1WireWrite.StaticColourBody(_io__raw_detail, self, self._root)
                self.detail._read()
            else:
                pass
                self.detail = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            _on = self.sub_mode
            if _on == H6199Pact1WireWrite.ModeSel.static_colour:
                pass
                self.detail._fetch_instances()
            else:
                pass


        def _write__seq(self, io=None):
            super(H6199Pact1WireWrite.ModeBody, self)._write__seq(io)
            self._io.write_u1(int(self.sub_mode))
            _on = self.sub_mode
            if _on == H6199Pact1WireWrite.ModeSel.static_colour:
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
            _on = self.sub_mode
            if _on == H6199Pact1WireWrite.ModeSel.static_colour:
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


    class StaticColourBody(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6199Pact1WireWrite.StaticColourBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rgb = govee_shared.GoveeShared.Rgb(self._io)
            self.rgb._read()
            self.kelvin = self._io.read_u2be()
            self.segment_mask = self._io.read_u2le()
            self.unknown_tail = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.rgb._fetch_instances()


        def _write__seq(self, io=None):
            super(H6199Pact1WireWrite.StaticColourBody, self)._write__seq(io)
            self.rgb._write__seq(self._io)
            self._io.write_u2be(self.kelvin)
            self._io.write_u2le(self.segment_mask)
            self._io.write_bytes(self.unknown_tail)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



