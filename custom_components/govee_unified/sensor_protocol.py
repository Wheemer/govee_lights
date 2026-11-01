"""Passive BLE advertisement decoding for common Govee climate sensors.

The packet formats are source-portable from the MIT-licensed
``Bluetooth-Devices/govee-ble`` parser.  These formats are advertisement-only:
they deliberately do not open a GATT connection or share the controllable
light/appliance transport.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
import struct
from collections.abc import Mapping

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


_MODEL_RE = re.compile(r"H[0-9A-F]{4}", re.IGNORECASE)
_PACKED_TEMP_HUMID_BATTERY = struct.Struct("<hHB")
_TEMP_HUMID_6 = frozenset({"H5072", "H5075", "H5129"})
_TEMP_HUMID_7 = frozenset({"H5074"})
_TEMP_HUMID_9 = frozenset({"H5051", "H5052", "H5071"})
_TEMP_HUMID_PACKED = frozenset(
    {"H5100", "H5101", "H5102", "H5103", "H5104", "H5105", "H5108", "H5110", "H5174", "H5177", "H5179"}
)

PASSIVE_CLIMATE_SENSOR_MODELS = _TEMP_HUMID_6 | _TEMP_HUMID_7 | _TEMP_HUMID_9 | _TEMP_HUMID_PACKED
PASSIVE_PROBE_SENSOR_MODELS = frozenset({"H5181", "H5182", "H5183", "H5184", "H5185", "H5191", "H5198"})
PASSIVE_ENVIRONMENT_SENSOR_MODELS = frozenset({"H5106", "H5140"})
PASSIVE_DUAL_PROBE_SENSOR_MODELS = frozenset({"H5112"})
PASSIVE_PRESENCE_SENSOR_MODELS = frozenset({"H5127"})
PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS = frozenset({"H5121", "H5122", "H5123", "H5124", "H5125", "H5126", "H5130"})
PASSIVE_SENSOR_MODELS = PASSIVE_CLIMATE_SENSOR_MODELS | PASSIVE_PROBE_SENSOR_MODELS | PASSIVE_ENVIRONMENT_SENSOR_MODELS | PASSIVE_DUAL_PROBE_SENSOR_MODELS | PASSIVE_PRESENCE_SENSOR_MODELS | PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS
_PROBE_COUNT = {"H5181": 1, "H5182": 2, "H5183": 1, "H5184": 4, "H5185": 2, "H5191": 1, "H5198": 4}
_FOUR_PROBE_IDS = {1: (1, 2), 65: (1, 2), 129: (1, 2), 193: (1, 2), 2: (3, 4), 66: (3, 4), 130: (3, 4), 194: (3, 4)}


@dataclass(frozen=True, slots=True)
class ClimateAdvertisement:
    """A validated passive sensor reading from one Govee advertisement."""

    model: str
    temperature_c: float
    humidity_pct: float
    battery_pct: int


@dataclass(frozen=True, slots=True)
class ProbeAdvertisement:
    """Temperatures broadcast by a Govee wired-probe sensor."""

    model: str
    probes_c: dict[int, float]


@dataclass(frozen=True, slots=True)
class EnvironmentAdvertisement:
    """A local air-quality advertisement with common climate fields."""

    model: str
    temperature_c: float
    humidity_pct: float
    co2_ppm: int | None = None
    pm25_ug_m3: int | None = None


@dataclass(frozen=True, slots=True)
class PresenceAdvertisement:
    """Occupancy and motion values from the H5127 passive advertisement."""

    model: str
    occupied: bool
    motion: bool


@dataclass(frozen=True, slots=True)
class DualProbeAdvertisement:
    """One rotating H5112 probe reading; the coordinator merges consecutive packets."""

    model: str
    probes_c: dict[int, float]
    humidity_pct: float | None
    battery_pct: int


@dataclass(frozen=True, slots=True)
class EncryptedEventAdvertisement:
    model: str
    battery_pct: int
    status: int


def sensor_model_from_ble_name(name: str | None) -> str | None:
    """Return a supported passive-climate model encoded in a local name."""
    if not name:
        return None
    normalized = name.upper()
    # The H5140's own reference advertisement is named ``GV5140xxxx``.
    # Unlike the other Govee names it omits the literal model-prefix H.
    if "5140" in normalized:
        return "H5140"
    for model in PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS:
        if model[1:] in normalized:
            return model
    match = _MODEL_RE.search(normalized)
    if match is None:
        return None
    model = match.group(0)
    return model if model in PASSIVE_SENSOR_MODELS else None


def _decode_packed_temp_humidity(data: bytes) -> tuple[float, float, int, bool]:
    """Decode Govee's 24-bit signed temperature/humidity/battery payload."""
    value = (data[0] << 16) + (data[1] << 8) + data[2]
    temperature = int((value & 0x7FFFFF) / 1000) / 10.0
    if value & 0x800000:
        temperature = -temperature
    humidity = ((value & 0x7FFFFF) % 1000) / 10.0
    return temperature, humidity, data[3] & 0x7F, bool(data[3] & 0x80)


def _decode_temp_humidity(data: bytes) -> tuple[float, float]:
    value = (data[0] << 16) + (data[1] << 8) + data[2]
    temperature = int((value & 0x7FFFFF) / 1000) / 10.0
    if value & 0x800000:
        temperature = -temperature
    return temperature, ((value & 0x7FFFFF) % 1000) / 10.0


def parse_climate_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> ClimateAdvertisement | None:
    """Parse the common temperature/humidity sensor formats for *name*.

    Matching is model-first.  That avoids treating a same-length Govee light
    advertisement as a climate reading merely because it shares a company id.
    """
    model = sensor_model_from_ble_name(name)
    if model is None:
        return None
    for payload in manufacturer_data.values():
        if model in _TEMP_HUMID_6 and len(payload) == 6:
            temperature, humidity, battery, error = _decode_packed_temp_humidity(payload[1:5])
        elif model in _TEMP_HUMID_7 and len(payload) == 7:
            temp_raw, humidity_raw, battery = _PACKED_TEMP_HUMID_BATTERY.unpack(payload[1:6])
            temperature, humidity, error = temp_raw / 100, humidity_raw / 100, False
        elif model in _TEMP_HUMID_9 and len(payload) == 9:
            temp_raw, humidity_raw, battery = _PACKED_TEMP_HUMID_BATTERY.unpack(payload[1:6])
            temperature, humidity, error = temp_raw / 100, humidity_raw / 100, False
        elif model in _TEMP_HUMID_PACKED and len(payload) in {6, 8}:
            temperature, humidity, battery, error = _decode_packed_temp_humidity(payload[2:6])
        else:
            continue
        if error or not -40 <= temperature <= 100 or not 0 <= humidity <= 100 or not 0 <= battery <= 100:
            continue
        return ClimateAdvertisement(model, temperature, humidity, battery)
    return None


def probe_count(model: str) -> int:
    """Return the maximum number of advertised probes for a supported model."""
    return _PROBE_COUNT[model]


def _probe_temperature(value: int) -> float | None:
    return None if value < 0 else value / 100


def parse_probe_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> ProbeAdvertisement | None:
    """Decode fixed-layout wired-probe formats from the MIT reference parser."""
    model = sensor_model_from_ble_name(name)
    if model not in PASSIVE_PROBE_SENSOR_MODELS:
        return None
    for payload in manufacturer_data.values():
        probes: dict[int, float | None]
        if model in {"H5181", "H5183"} and len(payload) == 14:
            (first, _alarm) = struct.unpack(">hh", payload[8:12])
            probes = {1: _probe_temperature(first)}
        elif model == "H5182" and len(payload) == 17:
            first, _first_alarm, _gap, second, _second_alarm = struct.unpack(">hhbhh", payload[8:17])
            probes = {1: _probe_temperature(first), 2: _probe_temperature(second)}
        elif model == "H5185" and len(payload) == 20:
            first, _first_alarm, _gap, second, _second_alarm = struct.unpack(">hhhhh", payload[8:18])
            probes = {1: _probe_temperature(first), 2: _probe_temperature(second)}
        elif model == "H5191" and len(payload) == 20:
            first, _alarm, _gap, _ambient = struct.unpack(">hhhh", payload[8:16])
            probes = {1: _probe_temperature(first)}
        elif model in {"H5184", "H5198"} and len(payload) in {17, 20}:
            ids = _FOUR_PROBE_IDS.get(payload[6])
            if ids is None:
                continue
            first, _first_alarm, _gap, second, _second_alarm = struct.unpack(">hhbhh", payload[8:17])
            probes = {ids[0]: _probe_temperature(first), ids[1]: _probe_temperature(second)}
        else:
            continue
        valid = {probe: temperature for probe, temperature in probes.items() if temperature is not None}
        if valid:
            return ProbeAdvertisement(model, valid)
    return None


def parse_environment_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> EnvironmentAdvertisement | None:
    """Decode H5140 CO2 and H5106 PM2.5 advertisements without connecting."""
    model = sensor_model_from_ble_name(name)
    if model not in PASSIVE_ENVIRONMENT_SENSOR_MODELS:
        return None
    for payload in manufacturer_data.values():
        if model == "H5140" and len(payload) == 8:
            temperature, humidity = _decode_temp_humidity(payload[2:5])
            co2 = int.from_bytes(payload[5:7], "big")
            if not payload[7] and -40 <= temperature <= 100 and 0 <= humidity <= 100:
                return EnvironmentAdvertisement(model, temperature, humidity, co2_ppm=co2)
        elif model == "H5106" and len(payload) == 6:
            value = int.from_bytes(payload[2:6], "big")
            magnitude = value & 0x7FFFFFFF
            temperature = int(magnitude / 1_000_000) / 10.0
            if value & 0x80000000:
                temperature = -temperature
            humidity = int((magnitude % 1_000_000) / 1000) / 10.0
            pm25 = magnitude % 1000
            if -40 <= temperature <= 100 and 0 <= humidity <= 100:
                return EnvironmentAdvertisement(model, temperature, humidity, pm25_ug_m3=pm25)
    return None


def parse_presence_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> PresenceAdvertisement | None:
    model = sensor_model_from_ble_name(name)
    if model != "H5127":
        return None
    for payload in manufacturer_data.values():
        if len(payload) == 6 and payload.startswith((b"\xec\x00\x01\x01", b"\xec\x00\x02\x01")):
            return PresenceAdvertisement(model, payload[4] == 1, payload[5] == 17)
    return None


def parse_dual_probe_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> DualProbeAdvertisement | None:
    model = sensor_model_from_ble_name(name)
    if model != "H5112":
        return None
    for payload in manufacturer_data.values():
        if len(payload) != 8:
            continue
        probe = 1 if payload[7] == 0x41 else 2 if payload[7] == 0x82 else 0
        if probe == 0:
            continue
        temperature, humidity, battery, error = _decode_packed_temp_humidity(payload[2:6])
        if not error and -40 <= temperature <= 100 and 0 <= humidity <= 100:
            return DualProbeAdvertisement(model, {probe: temperature}, humidity if probe == 1 else None, battery)
    return None


def _crc16(data: bytes) -> int:
    crc = 0x1D0F
    for byte in data:
        for bit in range(7, -1, -1):
            crc = ((crc << 1) ^ (0x1021 if ((crc >> 15) ^ (byte >> bit)) & 1 else 0)) & 0xFFFF
    return crc


def parse_encrypted_event_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> EncryptedEventAdvertisement | None:
    """Decode the app/reference AES-ECB advertisement used by H512x/H5130."""
    model = sensor_model_from_ble_name(name)
    if model not in PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS:
        return None
    for payload in manufacturer_data.values():
        if len(payload) != 24 or _crc16(payload[6:22]) != int.from_bytes(payload[22:24], "big"):
            continue
        key = payload[2:6] + bytes(12)
        decryptor = Cipher(algorithms.AES(key[::-1]), modes.ECB()).decryptor()
        decoded = (decryptor.update(payload[6:22][::-1]) + decryptor.finalize())[::-1]
        decoded_model = {3: "H5121", 8: "H5122", 2: "H5123", 9: "H5124", 10: "H5125", 11: "H5126", 13: "H5130"}.get(decoded[2])
        if decoded_model == model:
            return EncryptedEventAdvertisement(model, decoded[4], decoded[5])
    return None


def parse_passive_sensor_advertisement(name: str | None, manufacturer_data: Mapping[int, bytes]) -> ClimateAdvertisement | ProbeAdvertisement | EnvironmentAdvertisement | PresenceAdvertisement | DualProbeAdvertisement | EncryptedEventAdvertisement | None:
    """Decode any currently supported advertisement-only Govee sensor family."""
    return (
        parse_climate_advertisement(name, manufacturer_data)
        or parse_probe_advertisement(name, manufacturer_data)
        or parse_environment_advertisement(name, manufacturer_data)
        or parse_presence_advertisement(name, manufacturer_data)
        or parse_dual_probe_advertisement(name, manufacturer_data)
        or parse_encrypted_event_advertisement(name, manufacturer_data)
    )
