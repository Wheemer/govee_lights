"""Event entities for Govee's encrypted advertisement-only sensors."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.event import EventDeviceClass, EventEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .sensor_protocol import EncryptedEventAdvertisement

if TYPE_CHECKING:
    from . import GoveeBLEConfigEntry
    from .passive_sensor_coordinator import GoveePassiveSensorCoordinator

_MOTION_MODELS = frozenset({"H5121"})
_VIBRATION_MODELS = frozenset({"H5124"})
_BUTTON_MODELS = frozenset({"H5122", "H5125", "H5126", "H5130"})


def encrypted_event_details(reading: EncryptedEventAdvertisement) -> tuple[str, dict[str, int]] | None:
    """Map the exact decrypted status byte to a Home Assistant event.

    This deliberately preserves the portable parser's semantics: H5121 and
    H5124 report their event only with value 1; H5130 reports a button press
    in bit 0x10, independent of its persistent pressure bit.
    """
    if reading.model in _MOTION_MODELS and reading.status == 1:
        return "motion", {}
    if reading.model in _VIBRATION_MODELS and reading.status == 1:
        return "vibration", {}
    if reading.model == "H5130":
        return ("press", {"button": 0}) if reading.status & 0x10 else None
    if reading.model in _BUTTON_MODELS:
        return "press", {"button": reading.status}
    return None


async def async_setup_entry(
    hass: HomeAssistant, entry: GoveeBLEConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator = entry.runtime_data
    # This platform is forwarded only for passive entries; keeping the
    # runtime check structural avoids importing Home Assistant's Bluetooth
    # component simply to load the event mapping.
    if not hasattr(coordinator, "model") or not hasattr(coordinator, "async_add_listener"):
        return
    if coordinator.model in _MOTION_MODELS | _VIBRATION_MODELS | _BUTTON_MODELS:
        async_add_entities([GoveeEncryptedAdvertisementEvent(coordinator)])


class GoveeEncryptedAdvertisementEvent(EventEntity):
    """Publish momentary encrypted BLE actions as Home Assistant events."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        self.coordinator = coordinator
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_event"
        self._attr_device_info = coordinator.device_info
        self._last_reading: EncryptedEventAdvertisement | None = None
        if coordinator.model in _MOTION_MODELS:
            self._attr_name = "Motion"
            self._attr_device_class = EventDeviceClass.MOTION
            self._attr_event_types = ["motion"]
        elif coordinator.model in _BUTTON_MODELS:
            self._attr_name = "Button"
            self._attr_device_class = EventDeviceClass.BUTTON
            self._attr_event_types = ["press"]
        else:
            self._attr_name = "Vibration"
            self._attr_event_types = ["vibration"]

    @property
    def available(self) -> bool:
        return self.coordinator.data is not None and self.coordinator.last_update_success

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))

    @callback
    def _handle_coordinator_update(self) -> None:
        reading = self.coordinator.data
        if not isinstance(reading, EncryptedEventAdvertisement) or reading == self._last_reading:
            self.async_write_ha_state()
            return
        self._last_reading = reading
        if details := encrypted_event_details(reading):
            event_type, attributes = details
            self._trigger_event(event_type, attributes or None)
        self.async_write_ha_state()
