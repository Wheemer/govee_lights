"""Regression fixtures for the bounded H613E compatibility profile."""

from custom_components.govee_unified.const import _LEGACY_GENERIC_RGB_MODELS, MODEL_PROFILES
from custom_components.govee_unified.generated_protocol_adapter import (
    build_brightness,
    require_profile_packet,
)
from custom_components.govee_unified.light_commands import build_color_rgb, build_color_temp


def test_h613e_static_frames_preserve_the_validated_legacy_bk_wire_format() -> None:
    """The shared serializer needs the H613E companion-RGB transform for Kelvin."""
    profile = MODEL_PROFILES["H613E"]

    assert profile.command_operations == frozenset({"power", "brightness", "static"})
    assert profile.read_domains == frozenset()
    assert profile.write_with_response is True
    assert profile.connection_settle_seconds == 0.7
    assert profile.subscribe_all_control_notifications is True
    assert profile.outbound_transform is not None

    rgb = build_color_rgb(0, 255, 0, "H613E", profile=profile)
    kelvin = build_color_temp(5000, "H613E", profile=profile)

    assert rgb.hex() == "33050d00ff0000000000000000000000000000c4"
    # The H600A grammar selects its own table companion before the H613E
    # transport transform replaces that field with the APK-observed Bk value.
    assert kelvin.hex() == "33050dffffff1388ffe7cc00000000000000008b"
    assert profile.outbound_transform(rgb).hex() == rgb.hex()
    assert profile.outbound_transform(kelvin).hex() == "33050dffffff1388ffe4ce00000000000000008a"


def test_ported_legacy_rgb_families_preserve_their_documented_wire_shapes() -> None:
    """Capability-map families must not fall back to the generic RGB command."""
    expected = {
        "H6005": (
            "33050d0a141e000000000000000000000000003b",
            "33047f0000000000000000000000000000000048",
        ),
        "H6008": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
        "H6052": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
        "H6053": (
            "330515010a141e0000000000ff7f0000000000a2",
            "33047f0000000000000000000000000000000048",
        ),
        "H6058": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
        "H613A": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
        "H613B": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
        "H613D": (
            "33050d0a141e000000000000000000000000003b",
            "3304320000000000000000000000000000000005",
        ),
    }
    for model, (rgb_hex, brightness_hex) in expected.items():
        profile = MODEL_PROFILES[model]
        assert profile.supports_rgb
        assert not profile.supports_color_temperature
        rgb = build_color_rgb(10, 20, 30, model, profile=profile)
        brightness = build_brightness(50, model, profile=profile)
        require_profile_packet(rgb, profile)
        require_profile_packet(brightness, profile)
        assert profile.outbound_transform is not None
        assert profile.outbound_transform(rgb).hex() == rgb_hex
        assert profile.outbound_transform(brightness).hex() == brightness_hex


def test_h618c_basic_frames_match_the_documented_h617a_rgbic_family() -> None:
    """H618C shares the H617A write grammar, not the generic RGB command."""
    h617a = MODEL_PROFILES["H617A"]
    h618c = MODEL_PROFILES["H618C"]

    for builder, args in (
        (build_color_rgb, (10, 20, 30)),
        (build_brightness, (50,)),
    ):
        first = builder(*args, "H617A", profile=h617a)
        second = builder(*args, "H618C", profile=h618c)
        require_profile_packet(second, h618c)
        assert second == first


def test_h6172_and_h618f_preserve_the_documented_segment_family_frames() -> None:
    """The MQTT implementation explicitly groups these RGBIC products."""
    reference = MODEL_PROFILES["H617A"]
    for model, physical_ic_count in (("H6172", 40), ("H618F", 45)):
        profile = MODEL_PROFILES[model]
        assert profile.physical_ic_count == physical_ic_count
        assert profile.segment_count == 15
        assert profile.supports_segment_writes
        for builder, args in (
            (build_color_rgb, (10, 20, 30)),
            (build_brightness, (50,)),
        ):
            expected = builder(*args, "H617A", profile=reference)
            actual = builder(*args, model, profile=profile)
            require_profile_packet(actual, profile)
            assert actual == expected


def test_generic_legacy_family_uses_the_ported_raw_rgb_wire_format() -> None:
    """All APK-local members share the portable integration's basic envelope."""
    assert len(_LEGACY_GENERIC_RGB_MODELS) == 63
    for model in _LEGACY_GENERIC_RGB_MODELS:
        profile = MODEL_PROFILES[model]
        rgb = build_color_rgb(10, 20, 30, model, profile=profile)
        brightness = build_brightness(50, model, profile=profile)
        require_profile_packet(rgb, profile)
        require_profile_packet(brightness, profile)
        assert profile.outbound_transform is not None
        assert profile.outbound_transform(rgb).hex() == "3305020a141e0000000000000000000000000034"
        assert profile.outbound_transform(brightness).hex() == "33047f0000000000000000000000000000000048"
