"""Regression fixtures for the bounded H613E compatibility profile."""

from custom_components.govee_unified.const import MODEL_PROFILES
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
