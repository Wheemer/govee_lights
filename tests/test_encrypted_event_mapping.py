"""Regression coverage for decoded encrypted Govee event semantics."""

import importlib.util
from pathlib import Path
import sys
import types


ROOT = Path(__file__).parents[1] / "custom_components" / "govee_unified"
PACKAGE = "govee_unified_event_test"
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


sensor_protocol = _load("sensor_protocol")
event = _load("event")
Advertisement = sensor_protocol.EncryptedEventAdvertisement


def test_encrypted_event_mapping_keeps_momentary_events_out_of_binary_state() -> None:
    assert event.encrypted_event_details(Advertisement("H5121", 100, 1)) == ("motion", {})
    assert event.encrypted_event_details(Advertisement("H5124", 100, 1)) == ("vibration", {})
    assert event.encrypted_event_details(Advertisement("H5125", 100, 3)) == ("press", {"button": 3})
    assert event.encrypted_event_details(Advertisement("H5130", 100, 0x11)) == ("press", {"button": 0})
    assert event.encrypted_event_details(Advertisement("H5130", 100, 0x01)) is None
