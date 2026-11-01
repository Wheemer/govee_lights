# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class H6199WifiBody(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(H6199WifiBody, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.ssid_len = self._io.read_u1()
        self.ssid = (self._io.read_bytes(self.ssid_len)).decode(u"UTF-8")
        self.password_len = self._io.read_u1()
        self.password = (self._io.read_bytes(self.password_len)).decode(u"UTF-8")
        self.run_mode = self._io.read_u1()
        self.tz_hour = self._io.read_u1()
        self.iot_version = self._io.read_u1()
        self.tz_minute = self._io.read_u1()
        self.api_len = self._io.read_u2be()
        self.api = (self._io.read_bytes(self.api_len)).decode(u"UTF-8")
        self.matter_wifi_flag = self._io.read_u1()
        self.security_type = self._io.read_u1()
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(H6199WifiBody, self)._write__seq(io)
        self._io.write_u1(self.ssid_len)
        self._io.write_bytes((self.ssid).encode(u"UTF-8"))
        self._io.write_u1(self.password_len)
        self._io.write_bytes((self.password).encode(u"UTF-8"))
        self._io.write_u1(self.run_mode)
        self._io.write_u1(self.tz_hour)
        self._io.write_u1(self.iot_version)
        self._io.write_u1(self.tz_minute)
        self._io.write_u2be(self.api_len)
        self._io.write_bytes((self.api).encode(u"UTF-8"))
        self._io.write_u1(self.matter_wifi_flag)
        self._io.write_u1(self.security_type)


    def _check(self):
        if len((self.ssid).encode(u"UTF-8")) != self.ssid_len:
            raise kaitaistruct.ConsistencyError(u"ssid", self.ssid_len, len((self.ssid).encode(u"UTF-8")))
        if len((self.password).encode(u"UTF-8")) != self.password_len:
            raise kaitaistruct.ConsistencyError(u"password", self.password_len, len((self.password).encode(u"UTF-8")))
        if len((self.api).encode(u"UTF-8")) != self.api_len:
            raise kaitaistruct.ConsistencyError(u"api", self.api_len, len((self.api).encode(u"UTF-8")))
        self._dirty = False


