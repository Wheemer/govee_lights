"""Camera register diagnostic, independent of light availability."""

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorStateClass
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import GoveeBLEConfigEntry
from .appliance_coordinator import GoveeApplianceCoordinator
from .appliance_entity import GoveeApplianceEntity
from .appliance_entity import GoveePassiveSensorEntity
from .const import ICE_MAKER_MODELS
from .coordinator import GoveeBLECoordinator
from .passive_sensor_coordinator import GoveePassiveSensorCoordinator
from .effect_contracts import CapabilityState
from .entity import GoveeBLEEntity
from .video_applicability import h6199_camera_controls_state

PARALLEL_UPDATES = 0


async def async_setup_entry(
    hass: HomeAssistant, entry: GoveeBLEConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator = entry.runtime_data
    if isinstance(coordinator, GoveePassiveSensorCoordinator):
        async_add_entities(
            [
                GoveePassiveTemperatureSensor(coordinator),
                GoveePassiveHumiditySensor(coordinator),
                GoveePassiveBatterySensor(coordinator),
            ]
        )
        return
    if isinstance(coordinator, GoveeApplianceCoordinator):
        if coordinator.model in ICE_MAKER_MODELS:
            async_add_entities([GoveeIceMakerWorkStatus(coordinator)])
        return
    if coordinator.model != "H6199":
        return
    added = False

    def add_qualified() -> None:
        nonlocal added
        if not added and h6199_camera_controls_state(coordinator.model, coordinator) is CapabilityState.SUPPORTED:
            added = True
            async_add_entities([GoveeBLECameraStatus(coordinator)])

    add_qualified()
    entry.async_on_unload(coordinator.async_add_listener(add_qualified))


class GoveeBLECameraStatus(GoveeBLEEntity, SensorEntity):
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_translation_key = "camera_status"
    _attr_options = ["absent", "healthy", "incompatible", "unknown"]

    def __init__(self, coordinator: GoveeBLECoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_camera_status"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> str:
        if h6199_camera_controls_state(self.coordinator.model, self.coordinator) is not CapabilityState.SUPPORTED:
            return "unknown"
        return self.coordinator.camera_status


class GoveeIceMakerWorkStatus(GoveeApplianceEntity, SensorEntity):
    _attr_name = "Work Status"
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_options = ["idle", "ice_making", "ice_full", "washing", "wash_finished", "scheduled", "unknown"]

    def __init__(self, coordinator: GoveeApplianceCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_work_status"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> str:
        return self.coordinator.work_status


class _GoveePassiveClimateSensor(GoveePassiveSensorEntity, SensorEntity):
    """Common entity plumbing for a passive Govee climate advertisement."""

    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, suffix: str) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_{suffix}"
        self._attr_device_info = coordinator.device_info


class GoveePassiveTemperatureSensor(_GoveePassiveClimateSensor):
    _attr_name = "Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "temperature")

    @property
    def native_value(self) -> float | None:
        return self.coordinator.data.temperature_c if self.coordinator.data is not None else None


class GoveePassiveHumiditySensor(_GoveePassiveClimateSensor):
    _attr_name = "Humidity"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "humidity")

    @property
    def native_value(self) -> float | None:
        return self.coordinator.data.humidity_pct if self.coordinator.data is not None else None


class GoveePassiveBatterySensor(_GoveePassiveClimateSensor):
    _attr_name = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "battery")

    @property
    def native_value(self) -> int | None:
        return self.coordinator.data.battery_pct if self.coordinator.data is not None else None
