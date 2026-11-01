"""Regression coverage for APK-derived local appliance BLE frames."""

import importlib.util
from pathlib import Path
import sys
import types


ROOT = Path(__file__).parents[1] / "custom_components" / "govee_unified"
PACKAGE = "govee_unified_appliance_test"
package = types.ModuleType(PACKAGE)
package.__path__ = [str(ROOT)]
sys.modules[PACKAGE] = package


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"{PACKAGE}.{name}", ROOT / f"{name}.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_load("transport")
protocol = _load("appliance_protocol")


def test_h7172_apk_power_frames_are_signed_20_byte_commands() -> None:
    assert protocol.build_h7172_power_query().hex() == "aa010000000000000000000000000000000000ab"
    assert protocol.build_h7172_power_write(True).hex() == "3301010100000000000000000000000000000032"
    assert protocol.build_h7172_power_write(False).hex() == "3301000000000000000000000000000000000032"
    assert protocol.build_standard_power_write(True).hex() == "3301010000000000000000000000000000000033"
    assert protocol.build_standard_power_write(False).hex() == "3301000000000000000000000000000000000032"


def test_h7172_status_parsers_reject_invalid_or_unrelated_frames() -> None:
    assert protocol.parse_h7172_power_reply(bytes.fromhex("aa010100000000000000000000000000000000aa")) is True
    assert protocol.parse_h7172_power_reply(bytes.fromhex("aa010000000000000000000000000000000000ab")) is False
    assert protocol.parse_h7172_power_reply(b"\xaa\x01") is None
    assert protocol.parse_h7172_work_status(bytes.fromhex("aa190300000000000000000000000000000000b0")) == "washing"
    assert protocol.parse_h7172_work_status(bytes.fromhex("aa190900000000000000000000000000000000ba")) == "unknown"
