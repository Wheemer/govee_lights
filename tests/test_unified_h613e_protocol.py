"""Regression fixtures for the bounded H613E compatibility profile."""

from custom_components.govee_unified.const import MODEL_PROFILES
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
