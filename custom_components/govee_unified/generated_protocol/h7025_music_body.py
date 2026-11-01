# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_shared
from custom_components.govee_unified.generated_protocol import h617a_control_payload
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H7025MusicBody(ReadWriteKaitaiStruct):
    """SPECULATIVE H7025, issue #148.
    The reporter's working snapshot replays corroborate the IDs and tail prefixes
    selected by Android 7.6.01 H7025 music authoring.  This is not an H617A body alias.
    Its exact caller supplies Hopping ID 48, independently of the shared Hopping
    builder's default ID 5E, and emits background RGB, brightness, and two zero
    bytes.  Rolling and Separation similarly emit direction and two zero bytes,
    and Sway and Twinkle emit three zero bytes.  These bytes belong to the
    serialised body, but their firmware meaning remains unknown.
    Flow emits direction, group count, and ICs per group.  Star emits background
    RGB and a field named distance; the reported brightness interpretation of
    that byte is unconfirmed.  Piano and Day/Night reuse the named shared tails
    with exact-H7025 defaults and editor permissions.  Palette counts do not
    establish physical IC count.
    The app's multi-packet uploader emits 15 initial stream bytes and up to 17
    final bytes.  The reporter's eight-byte final threshold remains a separate,
    unresolved snapshot/firmware observation; it does not change shared framing.
    Unresolved: revision differences, raw snapshot sequences, all field bounds
    on hardware, rendering, and the necessity of body zeros versus frame padding.
    """

    class Direction(IntEnum):
        left = 6
        right = 7
        spread = 8
        gather = 9

    class FlowDirection(IntEnum):
        clockwise = 0
        counterclockwise = 1

    class MusicMode(IntEnum):
        piano_keys = 52
        day_and_night = 55
        hopping = 72
        flow = 89
        rolling = 90
        separation = 93
        sway = 142
        twinkle = 143
        star = 152
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H7025MusicBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = govee_common.GoveeCommon.A3Header(self._io)
        self.header._read()
        self.command = self._io.read_bytes(1)
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, self._io, u"/seq/1")
        self.mode = KaitaiStream.resolve_enum(H7025MusicBody.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == H7025MusicBody.MusicMode.day_and_night:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.DayAndNightTail(_io__raw_tail)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.flow:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.FlowTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.hopping:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.HoppingTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.piano_keys:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.PianoKeysTail(_io__raw_tail)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.rolling:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.DirectionTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.separation:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.DirectionTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.star:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.StarTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.sway:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.ColourOnlyTail(_io__raw_tail, self, self._root)
            self.tail._read()
        elif _on == H7025MusicBody.MusicMode.twinkle:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = H7025MusicBody.ColourOnlyTail(_io__raw_tail, self, self._root)
            self.tail._read()
        else:
            pass
            self.tail = self._io.read_bytes(self.tail_len)
        self.padding = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == H7025MusicBody.MusicMode.day_and_night:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.flow:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.hopping:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.piano_keys:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.rolling:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.star:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.sway:
            pass
            self.tail._fetch_instances()
        elif _on == H7025MusicBody.MusicMode.twinkle:
            pass
            self.tail._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H7025MusicBody, self)._write__seq(io)
        self.header._write__seq(self._io)
        self._io.write_bytes(self.command)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == H7025MusicBody.MusicMode.day_and_night:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.flow:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.hopping:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.piano_keys:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.rolling:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.separation:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.star:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.sway:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        elif _on == H7025MusicBody.MusicMode.twinkle:
            pass
            _io__raw_tail = KaitaiStream(BytesIO(bytearray(self.tail_len)))
            self._io.add_child_stream(_io__raw_tail)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.tail_len))
            def handler(parent, _io__raw_tail=_io__raw_tail):
                self._raw_tail = _io__raw_tail.to_byte_array()
                if len(self._raw_tail) != self.tail_len:
                    raise kaitaistruct.ConsistencyError(u"raw(tail)", self.tail_len, len(self._raw_tail))
                parent.write_bytes(self._raw_tail)
            _io__raw_tail.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.tail._write__seq(_io__raw_tail)
        else:
            pass
            self._io.write_bytes(self.tail)
        self._io.write_bytes(self.padding)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"padding", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.command) != 1:
            raise kaitaistruct.ConsistencyError(u"command", 1, len(self.command))
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, None, u"/seq/1")
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == H7025MusicBody.MusicMode.day_and_night:
            pass
        elif _on == H7025MusicBody.MusicMode.flow:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.hopping:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.piano_keys:
            pass
        elif _on == H7025MusicBody.MusicMode.rolling:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.separation:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.star:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.sway:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H7025MusicBody.MusicMode.twinkle:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        else:
            pass
            if len(self.tail) != self.tail_len:
                raise kaitaistruct.ConsistencyError(u"tail", self.tail_len, len(self.tail))
        self._dirty = False

    class ColourOnlyTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7025MusicBody.ColourOnlyTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unknown = self._io.read_bytes(3)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7025MusicBody.ColourOnlyTail, self)._write__seq(io)
            self._io.write_bytes(self.unknown)


        def _check(self):
            if len(self.unknown) != 3:
                raise kaitaistruct.ConsistencyError(u"unknown", 3, len(self.unknown))
            self._dirty = False


    class DirectionTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7025MusicBody.DirectionTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.direction = KaitaiStream.resolve_enum(H7025MusicBody.Direction, self._io.read_u1())
            self.unknown = self._io.read_bytes(2)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7025MusicBody.DirectionTail, self)._write__seq(io)
            self._io.write_u1(int(self.direction))
            self._io.write_bytes(self.unknown)


        def _check(self):
            if len(self.unknown) != 2:
                raise kaitaistruct.ConsistencyError(u"unknown", 2, len(self.unknown))
            self._dirty = False


    class FlowTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7025MusicBody.FlowTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.direction = KaitaiStream.resolve_enum(H7025MusicBody.FlowDirection, self._io.read_u1())
            self.group_count = self._io.read_u1()
            self.ics_per_group = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H7025MusicBody.FlowTail, self)._write__seq(io)
            self._io.write_u1(int(self.direction))
            self._io.write_u1(self.group_count)
            self._io.write_u1(self.ics_per_group)


        def _check(self):
            self._dirty = False


    class HoppingTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7025MusicBody.HoppingTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.background = govee_shared.GoveeShared.Rgb(self._io)
            self.background._read()
            self.rel_brightness = self._io.read_u1()
            self.unknown = self._io.read_bytes(2)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.background._fetch_instances()


        def _write__seq(self, io=None):
            super(H7025MusicBody.HoppingTail, self)._write__seq(io)
            self.background._write__seq(self._io)
            self._io.write_u1(self.rel_brightness)
            self._io.write_bytes(self.unknown)


        def _check(self):
            if len(self.unknown) != 2:
                raise kaitaistruct.ConsistencyError(u"unknown", 2, len(self.unknown))
            self._dirty = False


    class StarTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H7025MusicBody.StarTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.background = govee_shared.GoveeShared.Rgb(self._io)
            self.background._read()
            self.distance = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.background._fetch_instances()


        def _write__seq(self, io=None):
            super(H7025MusicBody.StarTail, self)._write__seq(io)
            self.background._write__seq(self._io)
            self._io.write_u1(self.distance)


        def _check(self):
            self._dirty = False


    @property
    def tail_len(self):
        if hasattr(self, '_m_tail_len'):
            return self._m_tail_len

        self._m_tail_len = (6 if self.mode == H7025MusicBody.MusicMode.hopping else (4 if self.mode == H7025MusicBody.MusicMode.star else (5 if self.mode == H7025MusicBody.MusicMode.piano_keys else 3)))
        return getattr(self, '_m_tail_len', None)

    def _invalidate_tail_len(self):
        del self._m_tail_len

