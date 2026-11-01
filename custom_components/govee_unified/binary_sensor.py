"""LAN connectivity entity dispatch for Govee Unified."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .appliance_entity import GoveePassiveSensorEntity
from .passive_sensor_coordinator import GoveePassiveSensorCoordinator
from .sensor_protocol import EncryptedEventAdvertisement, PresenceAdvertisement


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Dispatch LAN connectivity and passive BLE binary sensors."""
    if isinstance(config_entry.runtime_data, GoveePassiveSensorCoordinator):
        coordinator = config_entry.runtime_data
        if coordinator.model == "H5127":
            async_add_entities([GoveePassiveOccupancySensor(coordinator), GoveePassiveMotionSensor(coordinator)])
        elif coordinator.model == "H5123":
            async_add_entities([GoveeEncryptedWindowSensor(coordinator)])
        return
    if "lan_ip" not in config_entry.data:
        return
    from .lan_binary_sensor import async_setup_entry as async_setup_lan_entry

    await async_setup_lan_entry(hass, config_entry, async_add_entities)


class _GoveePassivePresenceSensor(GoveePassiveSensorEntity, BinarySensorEntity):
    def __init__(self, coordinator: GoveePassiveSensorCoordinator, suffix: str) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_{suffix}"
        self._attr_device_info = coordinator.device_info


class GoveePassiveOccupancySensor(_GoveePassivePresenceSensor):
    _attr_name = "Occupancy"
    _attr_device_class = BinarySensorDeviceClass.OCCUPANCY

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "occupancy")

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        return data.occupied if isinstance(data, PresenceAdvertisement) else None


class GoveePassiveMotionSensor(_GoveePassivePresenceSensor):
    _attr_name = "Motion"
    _attr_device_class = BinarySensorDeviceClass.MOTION

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "motion")

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        return data.motion if isinstance(data, PresenceAdvertisement) else None


class GoveeEncryptedWindowSensor(_GoveePassivePresenceSensor):
    _attr_name = "Window"
    _attr_device_class = BinarySensorDeviceClass.WINDOW

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "window")

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        return data.status == 2 if isinstance(data, EncryptedEventAdvertisement) else None
