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


_MODEL_RE = re.compile(r"H[0-9A-F]{4}", re.IGNORECASE)
_PACKED_TEMP_HUMID_BATTERY = struct.Struct("<hHB")
_TEMP_HUMID_6 = frozenset({"H5072", "H5075", "H5129"})
_TEMP_HUMID_7 = frozenset({"H5074"})
_TEMP_HUMID_9 = frozenset({"H5051", "H5052", "H5071"})
_TEMP_HUMID_PACKED = frozenset(
    {"H5100", "H5101", "H5102", "H5103", "H5104", "H5105", "H5108", "H5110", "H5174", "H5177", "H5179"}
)

PASSIVE_CLIMATE_SENSOR_MODELS = _TEMP_HUMID_6 | _TEMP_HUMID_7 | _TEMP_HUMID_9 | _TEMP_HUMID_PACKED


@dataclass(frozen=True, slots=True)
class ClimateAdvertisement:
    """A validated passive sensor reading from one Govee advertisement."""

    model: str
    temperature_c: float
    humidity_pct: float
    battery_pct: int


def sensor_model_from_ble_name(name: str | None) -> str | None:
    """Return a supported passive-climate model encoded in a local name."""
    if not name:
        return None
    match = _MODEL_RE.search(name.upper())
    if match is None:
        return None
    model = match.group(0)
    return model if model in PASSIVE_CLIMATE_SENSOR_MODELS else None


def _decode_packed_temp_humidity(data: bytes) -> tuple[float, float, int, bool]:
    """Decode Govee's 24-bit signed temperature/humidity/battery payload."""
    value = (data[0] << 16) + (data[1] << 8) + data[2]
    temperature = int((value & 0x7FFFFF) / 1000) / 10.0
    if value & 0x800000:
        temperature = -temperature
    humidity = ((value & 0x7FFFFF) % 1000) / 10.0
    return temperature, humidity, data[3] & 0x7F, bool(data[3] & 0x80)


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
