"""Pure-Python regression tests for local model-profile evidence policy."""

import importlib.util
from pathlib import Path
import sys

_MODULE_PATH = Path(__file__).parents[1] / "custom_components" / "govee_lights" / "models.py"
_SPEC = importlib.util.spec_from_file_location("govee_lights_models", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_MODELS = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _MODELS
_SPEC.loader.exec_module(_MODELS)

SupportQuality = _MODELS.SupportQuality
get_model_profile = _MODELS.get_model_profile


def test_h613e_profile_is_verified_and_uses_its_bk_family() -> None:
    profile = get_model_profile("h613e")

    assert profile.support_quality is SupportQuality.VERIFIED
    assert profile.family == "legacy_0d_bk"
    assert profile.features["colour_d"] is True


def test_h617f_uses_the_explicit_h617a_compatible_experimental_profile() -> None:
    profile = get_model_profile("h617f")

    assert profile.support_quality is SupportQuality.EXPERIMENTAL
    assert profile.family == "legacy_h617a"
    assert profile.features == {
        "segmented": True,
        "brightness_percent": True,
        "advert_state": True,
    }


def test_h6076_keeps_its_known_seven_segment_h617a_write_profile_experimental() -> None:
    profile = get_model_profile("H6076")

    assert profile.support_quality is SupportQuality.EXPERIMENTAL
    assert profile.family == "legacy_h617a"
    assert profile.features == {
        "segmented": True,
        "segments": 7,
        "brightness_percent": True,
    }


def test_unlisted_model_remains_a_generic_fallback() -> None:
    profile = get_model_profile("H9999")

    assert profile.support_quality is SupportQuality.GENERIC
    assert profile.family == "legacy_default"
    assert dict(profile.features) == {}
