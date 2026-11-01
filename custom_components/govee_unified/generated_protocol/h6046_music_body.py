# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_common
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6046MusicBody(ReadWriteKaitaiStruct):
    """SPECULATIVE (audited prospective) H6046, support issue #479.
    Evidence class: exact-model behavioural audit, not captures or hardware
    qualification. Known Pact 1/1 and 2/1 admit four companion-backed modes.
    This is reassembled A3 content, not a 20-byte physical packet: the shared
    header gives marker 1 and transport line count, then command 0x41 and mode.
    Physical A3 fragments carry their own XOR envelope.
    Palette count precedes RGB triples and a mode-specific subeffect/style byte.
    Beat admits 2..8 colours (default red, green, blue); Torch 1..8 and Rainbow
    Ring 6..8. Glitter admits 1..8 and a style byte. Default subeffect/style is
    zero; the other three modes also retain their raw zero-default subeffect.
    Default palettes other than Beat contain red, orange (255,127,0), yellow,
    green, blue, cyan and violet (139,0,255); default sensitivity is 99 in the
    separate selector. No H6076 effect codebook is inherited.
    Upload must succeed before the mode/sensitivity selector is sent. The ACK
    echoes mode and places result at offset 3. Status cannot recover this body.
    Unresolved assumptions: nondefault subeffect meanings, suffixes, physical
    rendering and other revisions. Opaque padding is never required to be zero.
    """

    class MusicMode(IntEnum):
        beat = 73
        torch = 80
        rainbow_ring = 81
        glitter = 82
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6046MusicBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = govee_common.GoveeCommon.A3Header(self._io)
        self.header._read()
        self.command = self._io.read_bytes(1)
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, self._io, u"/seq/1")
        self.mode = KaitaiStream.resolve_enum(H6046MusicBody.MusicMode, self._io.read_u1())
        if not  ((self.mode == H6046MusicBody.MusicMode.beat) or (self.mode == H6046MusicBody.MusicMode.torch) or (self.mode == H6046MusicBody.MusicMode.rainbow_ring) or (self.mode == H6046MusicBody.MusicMode.glitter)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.mode, self._io, u"/seq/2")
        self.palette_count = self._io.read_u1()
        if not self.palette_count >= self.palette_min:
            raise kaitaistruct.ValidationLessThanError(self.palette_min, self.palette_count, self._io, u"/seq/3")
        if not self.palette_count <= 8:
            raise kaitaistruct.ValidationGreaterThanError(8, self.palette_count, self._io, u"/seq/3")
        self.palette = []
        for i in range(self.palette_count):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        self.subeffect = self._io.read_u1()
        self.unknown_tail = self._io.read_bytes_full()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(H6046MusicBody, self)._write__seq(io)
        self.header._write__seq(self._io)
        self._io.write_bytes(self.command)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.palette_count)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        self._io.write_u1(self.subeffect)
        self._io.write_bytes(self.unknown_tail)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"unknown_tail", 0, self._io.size() - self._io.pos())


    def _check(self):
        if len(self.command) != 1:
            raise kaitaistruct.ConsistencyError(u"command", 1, len(self.command))
        if not self.command == b"\x41":
            raise kaitaistruct.ValidationNotEqualError(b"\x41", self.command, None, u"/seq/1")
        if not  ((self.mode == H6046MusicBody.MusicMode.beat) or (self.mode == H6046MusicBody.MusicMode.torch) or (self.mode == H6046MusicBody.MusicMode.rainbow_ring) or (self.mode == H6046MusicBody.MusicMode.glitter)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.mode, None, u"/seq/2")
        if not self.palette_count >= self.palette_min:
            raise kaitaistruct.ValidationLessThanError(self.palette_min, self.palette_count, None, u"/seq/3")
        if not self.palette_count <= 8:
            raise kaitaistruct.ValidationGreaterThanError(8, self.palette_count, None, u"/seq/3")
        if len(self.palette) != self.palette_count:
            raise kaitaistruct.ConsistencyError(u"palette", self.palette_count, len(self.palette))
        for i in range(len(self.palette)):
            pass

        self._dirty = False

    @property
    def default_sensitivity(self):
        if hasattr(self, '_m_default_sensitivity'):
            return self._m_default_sensitivity

        self._m_default_sensitivity = 99
        return getattr(self, '_m_default_sensitivity', None)

    def _invalidate_default_sensitivity(self):
        del self._m_default_sensitivity
    @property
    def default_subeffect(self):
        if hasattr(self, '_m_default_subeffect'):
            return self._m_default_subeffect

        self._m_default_subeffect = 0
        return getattr(self, '_m_default_subeffect', None)

    def _invalidate_default_subeffect(self):
        del self._m_default_subeffect
    @property
    def palette_max(self):
        if hasattr(self, '_m_palette_max'):
            return self._m_palette_max

        self._m_palette_max = 8
        return getattr(self, '_m_palette_max', None)

    def _invalidate_palette_max(self):
        del self._m_palette_max
    @property
    def palette_min(self):
        if hasattr(self, '_m_palette_min'):
            return self._m_palette_min

        self._m_palette_min = (2 if self.mode == H6046MusicBody.MusicMode.beat else (6 if self.mode == H6046MusicBody.MusicMode.rainbow_ring else 1))
        return getattr(self, '_m_palette_min', None)

    def _invalidate_palette_min(self):
        del self._m_palette_min

