# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import h60a_bulk
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H60a6Control(ReadWriteKaitaiStruct):
    """SPECULATIVE H60A6 support for issue #402.  Compatibility hypothesis:
    independently writable panel/ring enable registers are available on Pact
    1/1, 1/2 and 1/3, independent of segmented-colour geometry.  EE30 reports
    master, panel and ring flags independently; only bit zero is interpreted.
    No master wake, sibling rewrite or illumination relationship is inferred.
    Power-on behaviour has three states, rather than a boolean memory setting.
    Other flag bits and suffixes are opaque.  Hardware capture qualification,
    other revisions and reply timing remain unresolved.
    """

    class Command(IntEnum):
        zone_enable = 48
        power_on_behaviour = 65

    class Zone(IntEnum):
        panel_enabled = 0
        ring_enabled = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H60a6Control, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = self._io.read_bytes(1)
        if not self.header == b"\x33":
            raise kaitaistruct.ValidationNotEqualError(b"\x33", self.header, self._io, u"/seq/0")
        self.opcode = KaitaiStream.resolve_enum(H60a6Control.Command, self._io.read_u1())
        if not  ((self.opcode == H60a6Control.Command.zone_enable) or (self.opcode == H60a6Control.Command.power_on_behaviour)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.opcode, self._io, u"/seq/1")
        _on = self.opcode
        if _on == H60a6Control.Command.power_on_behaviour:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H60a6Control.PowerOnCommand(_io__raw_body, self, self._root)
            self.body._read()
        elif _on == H60a6Control.Command.zone_enable:
            pass
            self._raw_body = self._io.read_bytes(17)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = H60a6Control.ZoneCommand(_io__raw_body, self, self._root)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(17)
        self.checksum = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.opcode
        if _on == H60a6Control.Command.power_on_behaviour:
            pass
            self.body._fetch_instances()
        elif _on == H60a6Control.Command.zone_enable:
            pass
            self.body._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H60a6Control, self)._write__seq(io)
        self._io.write_bytes(self.header)
        self._io.write_u1(int(self.opcode))
        _on = self.opcode
        if _on == H60a6Control.Command.power_on_behaviour:
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
        elif _on == H60a6Control.Command.zone_enable:
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
        if not  ((self.opcode == H60a6Control.Command.zone_enable) or (self.opcode == H60a6Control.Command.power_on_behaviour)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.opcode, None, u"/seq/1")
        _on = self.opcode
        if _on == H60a6Control.Command.power_on_behaviour:
            pass
            if self.body._root != self._root:
                raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
            if self.body._parent != self:
                raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
        elif _on == H60a6Control.Command.zone_enable:
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

    class PowerOnCommand(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6Control.PowerOnCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.selector = self._io.read_bytes(1)
            if not self.selector == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.selector, self._io, u"/types/power_on_command/seq/0")
            self.state = KaitaiStream.resolve_enum(h60a_bulk.H60aBulk.PowerOnState, self._io.read_u1())
            if not  ((self.state == h60a_bulk.H60aBulk.PowerOnState.previous) or (self.state == h60a_bulk.H60aBulk.PowerOnState.on) or (self.state == h60a_bulk.H60aBulk.PowerOnState.off)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.state, self._io, u"/types/power_on_command/seq/1")
            self.unknown_tail = self._io.read_bytes(15)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6Control.PowerOnCommand, self)._write__seq(io)
            self._io.write_bytes(self.selector)
            self._io.write_u1(int(self.state))
            self._io.write_bytes(self.unknown_tail)


        def _check(self):
            if len(self.selector) != 1:
                raise kaitaistruct.ConsistencyError(u"selector", 1, len(self.selector))
            if not self.selector == b"\x02":
                raise kaitaistruct.ValidationNotEqualError(b"\x02", self.selector, None, u"/types/power_on_command/seq/0")
            if not  ((self.state == h60a_bulk.H60aBulk.PowerOnState.previous) or (self.state == h60a_bulk.H60aBulk.PowerOnState.on) or (self.state == h60a_bulk.H60aBulk.PowerOnState.off)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.state, None, u"/types/power_on_command/seq/1")
            if len(self.unknown_tail) != 15:
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 15, len(self.unknown_tail))
            self._dirty = False


    class ZoneCommand(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6Control.ZoneCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.zone = KaitaiStream.resolve_enum(H60a6Control.Zone, self._io.read_u1())
            if not  ((self.zone == H60a6Control.Zone.panel_enabled) or (self.zone == H60a6Control.Zone.ring_enabled)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.zone, self._io, u"/types/zone_command/seq/0")
            self.enabled = self._io.read_u1()
            if not  ((self.enabled == 0) or (self.enabled == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.enabled, self._io, u"/types/zone_command/seq/1")
            self.unknown_tail = self._io.read_bytes(15)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6Control.ZoneCommand, self)._write__seq(io)
            self._io.write_u1(int(self.zone))
            self._io.write_u1(self.enabled)
            self._io.write_bytes(self.unknown_tail)


        def _check(self):
            if not  ((self.zone == H60a6Control.Zone.panel_enabled) or (self.zone == H60a6Control.Zone.ring_enabled)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.zone, None, u"/types/zone_command/seq/0")
            if not  ((self.enabled == 0) or (self.enabled == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.enabled, None, u"/types/zone_command/seq/1")
            if len(self.unknown_tail) != 15:
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 15, len(self.unknown_tail))
            self._dirty = False


    class ZoneNotification(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H60a6Control.ZoneNotification, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = self._io.read_bytes(3)
            if not self.header == b"\xEE\x30\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\xEE\x30\x01", self.header, self._io, u"/types/zone_notification/seq/0")
            self.total_flags = self._io.read_u1()
            self.panel_flags = self._io.read_u1()
            self.ring_flags = self._io.read_u1()
            self.unknown_tail = self._io.read_bytes(13)
            self.checksum = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H60a6Control.ZoneNotification, self)._write__seq(io)
            self._io.write_bytes(self.header)
            self._io.write_u1(self.total_flags)
            self._io.write_u1(self.panel_flags)
            self._io.write_u1(self.ring_flags)
            self._io.write_bytes(self.unknown_tail)
            self._io.write_u1(self.checksum)


        def _check(self):
            if len(self.header) != 3:
                raise kaitaistruct.ConsistencyError(u"header", 3, len(self.header))
            if not self.header == b"\xEE\x30\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\xEE\x30\x01", self.header, None, u"/types/zone_notification/seq/0")
            if len(self.unknown_tail) != 13:
                raise kaitaistruct.ConsistencyError(u"unknown_tail", 13, len(self.unknown_tail))
            self._dirty = False

        @property
        def is_on(self):
            if hasattr(self, '_m_is_on'):
                return self._m_is_on

            self._m_is_on = self.total_flags & 1 != 0
            return getattr(self, '_m_is_on', None)

        def _invalidate_is_on(self):
            del self._m_is_on
        @property
        def panel_enabled(self):
            if hasattr(self, '_m_panel_enabled'):
                return self._m_panel_enabled

            self._m_panel_enabled = self.panel_flags & 1 != 0
            return getattr(self, '_m_panel_enabled', None)

        def _invalidate_panel_enabled(self):
            del self._m_panel_enabled
        @property
        def ring_enabled(self):
            if hasattr(self, '_m_ring_enabled'):
                return self._m_ring_enabled

            self._m_ring_enabled = self.ring_flags & 1 != 0
            return getattr(self, '_m_ring_enabled', None)

        def _invalidate_ring_enabled(self):
            del self._m_ring_enabled


