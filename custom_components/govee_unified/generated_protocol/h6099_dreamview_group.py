# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6099DreamviewGroup(ReadWriteKaitaiStruct):
    """SPECULATIVE H6099 issue #258, H66A0 issue #408.  Android 7.6.01 MovieFeastV2
    group upload over A3 type 0x50 supports at most seven sub-devices on H6099
    (goods type 191) and ten sub-devices on H66A0 (goods type 327).  The payload
    prefixes a member count followed by the member records below.  MAC bytes use
    reversed display order, and name bytes use UTF-8.  cmd_ver is supplied
    externally, never inferred.  The protocol maps UI areas 1..20 onto wire
    values 1..10; zero is unassigned and 0xff disables an area.  Area counts must
    be supplied explicitly.  Zero-area records and single-area disabled behaviour
    remain unresolved and are not enabled.  The H66A0 owner reports in issue #408
    that MAC-addressed 0x50 group uploads match official-app captures.
    Attributable raw captures are not attached; name-addressed records remain
    structurally evidenced candidates.  No
    membership readback exists, and a successful upload is not confirmation.
    H6097 issue #431 independently selects this membership format with at most
    seven members.  Its actual member compatibility and restoration remain
    unqualified.
    H6199 issue #438 independently uses these member records and A3 type 0x50,
    with a five-member product fallback.  Its group completion and actual
    synchronisation still require owner qualification.
    """

    class IdentityKind(IntEnum):
        mac = 0
        name = 1
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6099DreamviewGroup, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.num_members = self._io.read_u1()
        self.members = []
        for i in range(self.num_members):
            _t_members = H6099DreamviewGroup.Member(self._io, self, self._root)
            try:
                _t_members._read()
            finally:
                self.members.append(_t_members)

        self.unknown = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.members)):
            pass
            self.members[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(H6099DreamviewGroup, self)._write__seq(io)
        self._io.write_u1(self.num_members)
        for i in range(len(self.members)):
            pass
            self.members[i]._write__seq(self._io)

        self._io.write_bytes(self.unknown)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"unknown", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.members) != self.num_members:
            raise kaitaistruct.ConsistencyError(u"members", self.num_members, len(self.members))
        for i in range(len(self.members)):
            pass
            if self.members[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"members", self._root, self.members[i]._root)
            if self.members[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"members", self, self.members[i]._parent)

        self._dirty = False

    class Member(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H6099DreamviewGroup.Member, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_rgbic = self._io.read_u1()
            self.identity_kind = KaitaiStream.resolve_enum(H6099DreamviewGroup.IdentityKind, self._io.read_u1())
            self.cmd_ver = self._io.read_u1()
            if self.identity_kind == H6099DreamviewGroup.IdentityKind.mac:
                pass
                self.reversed_mac = self._io.read_bytes(6)

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass
                self.name_len = self._io.read_u1()

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass
                self.name_bytes = self._io.read_bytes(self.name_len)

            self.area_count = self._io.read_u1()
            self.area_values = []
            for i in range(self.area_count):
                self.area_values.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.identity_kind == H6099DreamviewGroup.IdentityKind.mac:
                pass

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass

            for i in range(len(self.area_values)):
                pass



        def _write__seq(self, io=None):
            super(H6099DreamviewGroup.Member, self)._write__seq(io)
            self._io.write_u1(self.is_rgbic)
            self._io.write_u1(int(self.identity_kind))
            self._io.write_u1(self.cmd_ver)
            if self.identity_kind == H6099DreamviewGroup.IdentityKind.mac:
                pass
                self._io.write_bytes(self.reversed_mac)

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass
                self._io.write_u1(self.name_len)

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass
                self._io.write_bytes(self.name_bytes)

            self._io.write_u1(self.area_count)
            for i in range(len(self.area_values)):
                pass
                self._io.write_u1(self.area_values[i])



        def _check(self):
            if self.identity_kind == H6099DreamviewGroup.IdentityKind.mac:
                pass
                if len(self.reversed_mac) != 6:
                    raise kaitaistruct.ConsistencyError(u"reversed_mac", 6, len(self.reversed_mac))

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass

            if self.identity_kind == H6099DreamviewGroup.IdentityKind.name:
                pass
                if len(self.name_bytes) != self.name_len:
                    raise kaitaistruct.ConsistencyError(u"name_bytes", self.name_len, len(self.name_bytes))

            if len(self.area_values) != self.area_count:
                raise kaitaistruct.ConsistencyError(u"area_values", self.area_count, len(self.area_values))
            for i in range(len(self.area_values)):
                pass

            self._dirty = False


    @property
    def group_type(self):
        if hasattr(self, '_m_group_type'):
            return self._m_group_type

        self._m_group_type = 80
        return getattr(self, '_m_group_type', None)

    def _invalidate_group_type(self):
        del self._m_group_type

