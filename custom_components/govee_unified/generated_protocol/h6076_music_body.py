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

class H6076MusicBody(ReadWriteKaitaiStruct):
    """SPECULATIVE H6076, issue #343.
    Evidence source classes: a reporter's decrypted Android HCI snoop of the Govee
    app driving an H6076 (hardware 3.05.00, software 1.04.05, V1 encrypted
    session), which shows the Torch and Separation bodies in full, and Android
    Govee 7.5.30 music companion upload behaviour.
    Compatibility hypothesis: the app's default bodies for the five companion-backed
    effects other than Separation are the A3 command 0x41 body, a palette count and
    that many RGB triples, with no further field.  Separation appends the
    three-byte tail it shares with H617A: a split point, a fade flag and a speed
    byte that the app sets to 94 or 97 below 30 ICs and to 98 or 99 from 30, for
    fade on or off.  The selector that follows is described by h6076_music_write.ksy
    and the lamp's reply by h6076_music_ack.ksy.
    Skittles, Candy Crush, Fusion and Shiny were not captured in full.  Their bodies
    follow the Torch layout in the app producer code.  The reporter's separate LAN
    integration (scroom/ha-govee-local-segments) builds byte-identical bodies and
    reports that all twelve effects react on the lamp; that is plaintext replay, not
    a Bluetooth capture.
    Unresolved assumptions: the H6076's physical IC count, which decides the
    Separation speed byte beyond the captured 0x61 (fewer than 30 ICs, fade off),
    palette bounds per effect, the value of the unused bytes after the written
    fields, and the behaviour of firmware older than 1.02.00.
    """

    class MusicMode(IntEnum):
        separation = 50
        skittles = 77
        candy_crush = 78
        fusion = 79
        torch = 80
        shiny = 81
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6076MusicBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = govee_common.GoveeCommon.A3Header(self._io)
        self.header._read()
        self.command = self._io.read_bytes(1)
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, self._io, u"/seq/1")
        self.mode = KaitaiStream.resolve_enum(H6076MusicBody.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == H6076MusicBody.MusicMode.separation:
            pass
            self._raw_tail = self._io.read_bytes(self.tail_len)
            _io__raw_tail = KaitaiStream(BytesIO(self._raw_tail))
            self.tail = h617a_control_payload.H617aControlPayload.SeparationTail(_io__raw_tail)
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
        if _on == H6076MusicBody.MusicMode.separation:
            pass
            self.tail._fetch_instances()
        else:
            pass


    def _write__seq(self, io=None):
        super(H6076MusicBody, self)._write__seq(io)
        self.header._write__seq(self._io)
        self._io.write_bytes(self.command)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == H6076MusicBody.MusicMode.separation:
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
        if _on == H6076MusicBody.MusicMode.separation:
            pass
        else:
            pass
            if len(self.tail) != self.tail_len:
                raise kaitaistruct.ConsistencyError(u"tail", self.tail_len, len(self.tail))
        self._dirty = False

    @property
    def tail_len(self):
        if hasattr(self, '_m_tail_len'):
            return self._m_tail_len

        self._m_tail_len = (3 if self.mode == H6076MusicBody.MusicMode.separation else 0)
        return getattr(self, '_m_tail_len', None)

    def _invalidate_tail_len(self):
        del self._m_tail_len

