# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from custom_components.govee_unified.generated_protocol import govee_shared
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H1a42MusicParameters(ReadWriteKaitaiStruct):
    """SPECULATIVE H1A42 issue #391.  Android 7.6.01 MusicModeNewH1A43 (goodsType 400)
    uploads this payload under A3 subtype 0x41 before the 33 05 13 music selector
    for palette-backed modes.
    """

    class MusicMode(IntEnum):
        splash = 132
        spring = 133
        ripple = 146
        orbit = 163
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H1a42MusicParameters, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.mode = KaitaiStream.resolve_enum(H1a42MusicParameters.MusicMode, self._io.read_u1())
        self.num_palette = self._io.read_u1()
        self.palette = []
        for i in range(self.num_palette):
            _t_palette = govee_shared.GoveeShared.Rgb(self._io)
            try:
                _t_palette._read()
            finally:
                self.palette.append(_t_palette)

        _on = self.mode
        if _on == H1a42MusicParameters.MusicMode.orbit:
            pass
            self.tail = H1a42MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H1a42MusicParameters.MusicMode.ripple:
            pass
            self.tail = H1a42MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H1a42MusicParameters.MusicMode.splash:
            pass
            self.tail = H1a42MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        elif _on == H1a42MusicParameters.MusicMode.spring:
            pass
            self.tail = H1a42MusicParameters.EmptyTail(self._io, self, self._root)
            self.tail._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        for i in range(len(self.palette)):
            pass
            self.palette[i]._fetch_instances()

        _on = self.mode
        if _on == H1a42MusicParameters.MusicMode.orbit:
            pass
            self.tail._fetch_instances()
        elif _on == H1a42MusicParameters.MusicMode.ripple:
            pass
            self.tail._fetch_instances()
        elif _on == H1a42MusicParameters.MusicMode.splash:
            pass
            self.tail._fetch_instances()
        elif _on == H1a42MusicParameters.MusicMode.spring:
            pass
            self.tail._fetch_instances()


    def _write__seq(self, io=None):
        super(H1a42MusicParameters, self)._write__seq(io)
        self._io.write_u1(int(self.mode))
        self._io.write_u1(self.num_palette)
        for i in range(len(self.palette)):
            pass
            self.palette[i]._write__seq(self._io)

        _on = self.mode
        if _on == H1a42MusicParameters.MusicMode.orbit:
            pass
            self.tail._write__seq(self._io)
        elif _on == H1a42MusicParameters.MusicMode.ripple:
            pass
            self.tail._write__seq(self._io)
        elif _on == H1a42MusicParameters.MusicMode.splash:
            pass
            self.tail._write__seq(self._io)
        elif _on == H1a42MusicParameters.MusicMode.spring:
            pass
            self.tail._write__seq(self._io)


    def _check(self):
        if len(self.palette) != self.num_palette:
            raise kaitaistruct.ConsistencyError(u"palette", self.num_palette, len(self.palette))
        for i in range(len(self.palette)):
            pass

        _on = self.mode
        if _on == H1a42MusicParameters.MusicMode.orbit:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H1a42MusicParameters.MusicMode.ripple:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H1a42MusicParameters.MusicMode.splash:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        elif _on == H1a42MusicParameters.MusicMode.spring:
            pass
            if self.tail._root != self._root:
                raise kaitaistruct.ConsistencyError(u"tail", self._root, self.tail._root)
            if self.tail._parent != self:
                raise kaitaistruct.ConsistencyError(u"tail", self, self.tail._parent)
        self._dirty = False

    class EmptyTail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(H1a42MusicParameters.EmptyTail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(H1a42MusicParameters.EmptyTail, self)._write__seq(io)


        def _check(self):
            self._dirty = False



