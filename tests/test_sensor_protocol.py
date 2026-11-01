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


def test_probe_sensor_batch_decodes_fixed_and_rotating_probe_layouts() -> None:
    h5182 = bytes(8) + bytes.fromhex("00fa00000000c80000")
    assert protocol.parse_probe_advertisement("Govee_H5182_0001", {0x2730: h5182}) == protocol.ProbeAdvertisement(
        "H5182", {1: 2.5, 2: 2.0}
    )
    h5184 = bytes(6) + b"\x02" + bytes(1) + bytes.fromhex("00fa00000000c80000")
    assert protocol.parse_probe_advertisement("Govee_H5184_0001", {0x1B36: h5184}) == protocol.ProbeAdvertisement(
        "H5184", {3: 2.5, 4: 2.0}
    )


def test_environment_sensor_batch_decodes_co2_and_pm25() -> None:
    assert protocol.parse_environment_advertisement("GV5140303A", {1: bytes.fromhex("0101033dee023e00")}) == protocol.EnvironmentAdvertisement(
        "H5140", 21.2, 46.2, co2_ppm=574
    )


def test_h5127_presence_advertisement_is_strictly_payload_gated() -> None:
    assert protocol.parse_presence_advertisement("Govee_H5127_0001", {0x8843: bytes.fromhex("ec0002010111")}) == protocol.PresenceAdvertisement("H5127", True, True)
    assert protocol.parse_presence_advertisement("Govee_H5127_0001", {0x8843: bytes.fromhex("ec0002010010")}) == protocol.PresenceAdvertisement("H5127", False, False)


def test_h5112_rotating_probe_packet_decodes_the_selected_probe() -> None:
    assert protocol.parse_dual_probe_advertisement("GVH5112_0001", {1: bytes.fromhex("00000341c2640041")}) == protocol.DualProbeAdvertisement("H5112", {1: 21.3}, 44.2, 100)
    assert protocol.parse_environment_advertisement("Govee_H5106_0001", {1: bytes.fromhex("0000014a3b00")}) == protocol.EnvironmentAdvertisement(
        "H5106", 2.1, 64.1, pm25_ug_m3=984
    )
