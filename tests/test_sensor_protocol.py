"""Fixtures for Govee passive climate-sensor advertisement decoding."""

import importlib.util
from pathlib import Path
import sys
import types


ROOT = Path(__file__).parents[1] / "custom_components" / "govee_unified"
PACKAGE = "govee_unified_sensor_protocol_test"
package = types.ModuleType(PACKAGE)
package.__path__ = [str(ROOT)]
sys.modules[PACKAGE] = package
spec = importlib.util.spec_from_file_location(f"{PACKAGE}.sensor_protocol", ROOT / "sensor_protocol.py")
assert spec is not None and spec.loader is not None
protocol = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = protocol
spec.loader.exec_module(protocol)


def test_packed_sensors_decode_temperature_humidity_and_battery() -> None:
    reading = protocol.parse_climate_advertisement("GVH5075_2762", {60552: bytes.fromhex("000341c26400")})
    assert reading == protocol.ClimateAdvertisement("H5075", 21.3, 44.2, 100)


def test_little_endian_sensor_formats_are_model_gated() -> None:
    reading = protocol.parse_climate_advertisement("Govee_H5052_E81B", {60552: bytes.fromhex("001c01a7143b000002")})
    assert reading == protocol.ClimateAdvertisement("H5052", 2.84, 52.87, 59)
    assert protocol.parse_climate_advertisement("Govee_H613E_0001", {60552: bytes.fromhex("000341c26400")}) is None


def test_invalid_error_flag_or_out_of_range_reading_is_not_published() -> None:
    assert protocol.parse_climate_advertisement("GVH5075_2762", {60552: bytes.fromhex("000341c2e400")}) is None
