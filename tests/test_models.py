"""Pure-Python regression tests for local model-profile evidence policy."""

import importlib.util
from pathlib import Path
import sys

import pytest

_MODULE_PATH = Path(__file__).parents[1] / "custom_components" / "govee_lights" / "models.py"
_SPEC = importlib.util.spec_from_file_location("govee_lights_models", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_MODELS = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _MODELS
_SPEC.loader.exec_module(_MODELS)

SupportQuality = _MODELS.SupportQuality
get_model_profile = _MODELS.get_model_profile
get_segment_readback_group_size = _MODELS.get_segment_readback_group_size
get_brightness_wire_range = _MODELS.get_brightness_wire_range
supports_segment_brightness = _MODELS.supports_segment_brightness
uses_h617a_segment_grammar = _MODELS.uses_h617a_segment_grammar


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
        "h617a_segment_grammar": True,
        "segment_brightness": True,
    }


def test_h6076_keeps_its_known_seven_segment_h617a_write_profile_experimental() -> None:
    profile = get_model_profile("H6076")

    assert profile.support_quality is SupportQuality.EXPERIMENTAL
    assert profile.family == "legacy_h617a"
    assert profile.features == {
        "segmented": True,
        "segments": 7,
        "brightness_percent": True,
        "h617a_segment_grammar": True,
        "segment_readback_group_size": 4,
        "segment_brightness": True,
    }


@pytest.mark.parametrize(
    ("model", "segments"),
    [("H1A42", 5), ("H61F5", 10)],
)
def test_h617a_command_siblings_keep_their_known_segment_geometry(
    model: str, segments: int
) -> None:
    profile = get_model_profile(model)

    assert profile.support_quality is SupportQuality.EXPERIMENTAL
    assert profile.family == "legacy_h617a"
    assert profile.features == {
        "segmented": True,
        "segments": segments,
        "brightness_percent": True,
        "h617a_segment_grammar": True,
        "segment_readback_group_size": 4,
        "segment_brightness": True,
    }


@pytest.mark.parametrize("model", ["H6076", "H6102", "H617A", "H617C", "H617E", "H617F"])
def test_known_h617a_command_models_opt_into_the_segmented_white_grammar(model: str) -> None:
    assert uses_h617a_segment_grammar(model)


def test_unrelated_segmented_model_does_not_inherit_h617a_white_grammar() -> None:
    assert not uses_h617a_segment_grammar("H6199")


@pytest.mark.parametrize("model", ["H6076", "H1A42", "H61F5"])
def test_newer_h617a_siblings_use_four_segment_readback_groups(model: str) -> None:
    assert get_segment_readback_group_size(model) == 4


def test_legacy_h617a_readback_group_size_remains_three() -> None:
    assert get_segment_readback_group_size("H617A") == 3


def test_h6102_declares_its_documented_brightness_register_range() -> None:
    assert get_brightness_wire_range("H6102") == (20, 254)
    assert get_brightness_wire_range("H617A") is None
    assert supports_segment_brightness("H6102")
    assert supports_segment_brightness("H617A")


@pytest.mark.parametrize("model", ["H6076", "H617A", "H617C", "H617E", "H617F", "H1A42", "H61F5"])
def test_h617a_command_siblings_expose_native_segment_brightness(model: str) -> None:
    assert supports_segment_brightness(model)


def test_unlisted_model_remains_a_generic_fallback() -> None:
    profile = get_model_profile("H9999")

    assert profile.support_quality is SupportQuality.GENERIC
    assert profile.family == "legacy_default"
    assert dict(profile.features) == {}
