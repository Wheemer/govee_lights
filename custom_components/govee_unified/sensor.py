"""Camera register diagnostic, independent of light availability."""

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorStateClass
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import GoveeBLEConfigEntry
from .appliance_coordinator import GoveeApplianceCoordinator
from .appliance_entity import GoveeApplianceEntity
from .appliance_entity import GoveePassiveSensorEntity
from .const import ICE_MAKER_MODELS, KETTLE_TEMPERATURE_MODELS
from .coordinator import GoveeBLECoordinator
from .passive_sensor_coordinator import GoveePassiveSensorCoordinator
from .sensor_protocol import (
    ClimateAdvertisement,
    DualProbeAdvertisement,
    EncryptedEventAdvertisement,
    EnvironmentAdvertisement,
    MultiSensorAdvertisement,
    PASSIVE_CLIMATE_SENSOR_MODELS,
    PASSIVE_ENVIRONMENT_SENSOR_MODELS,
    PASSIVE_DUAL_PROBE_SENSOR_MODELS,
    PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS,
    PASSIVE_MULTI_SENSOR_MODELS,
    PASSIVE_PROBE_SENSOR_MODELS,
    PASSIVE_SIX_PROBE_SENSOR_MODELS,
    ProbeAdvertisement,
    SixProbeAdvertisement,
    probe_count,
)
from .effect_contracts import CapabilityState
from .entity import GoveeBLEEntity
from .video_applicability import h6199_camera_controls_state

PARALLEL_UPDATES = 0


async def async_setup_entry(
    hass: HomeAssistant, entry: GoveeBLEConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator = entry.runtime_data
    if isinstance(coordinator, GoveePassiveSensorCoordinator):
        if coordinator.model in PASSIVE_CLIMATE_SENSOR_MODELS:
            async_add_entities([
                GoveePassiveTemperatureSensor(coordinator),
                GoveePassiveHumiditySensor(coordinator),
                GoveePassiveBatterySensor(coordinator),
            ])
        elif coordinator.model in PASSIVE_ENCRYPTED_EVENT_SENSOR_MODELS:
            async_add_entities([GoveeEncryptedEventBatterySensor(coordinator)])
        elif coordinator.model in PASSIVE_PROBE_SENSOR_MODELS:
            entities = [GoveePassiveProbeTemperatureSensor(coordinator, probe) for probe in range(1, probe_count(coordinator.model) + 1)]
            if coordinator.model == "H5191":
                entities.append(GoveePassiveAmbientTemperatureSensor(coordinator))
            async_add_entities(entities)
        elif coordinator.model in PASSIVE_ENVIRONMENT_SENSOR_MODELS:
            entities = [GoveePassiveTemperatureSensor(coordinator), GoveePassiveHumiditySensor(coordinator)]
            if coordinator.model == "H5140":
                entities.append(GoveePassiveCO2Sensor(coordinator))
            else:
                entities.append(GoveePassivePM25Sensor(coordinator))
            async_add_entities(entities)
        elif coordinator.model in PASSIVE_DUAL_PROBE_SENSOR_MODELS:
            async_add_entities([GoveePassiveDualProbeTemperatureSensor(coordinator, 1), GoveePassiveDualProbeTemperatureSensor(coordinator, 2), GoveePassiveDualProbeHumiditySensor(coordinator), GoveePassiveDualProbeBatterySensor(coordinator)])
        elif coordinator.model in PASSIVE_SIX_PROBE_SENSOR_MODELS:
            async_add_entities([GoveeSixProbeTemperatureSensor(coordinator, probe) for probe in range(1, 7)] + [GoveeSixProbeBatterySensor(coordinator)])
        elif coordinator.model in PASSIVE_MULTI_SENSOR_MODELS:
            async_add_entities([
                GoveeMultiSensorTemperature(coordinator, role)
                for role in ("primary", "remote")
            ] + [
                GoveeMultiSensorHumidity(coordinator, role)
                for role in ("primary", "remote")
            ] + [
                GoveeMultiSensorBattery(coordinator, role)
                for role in ("primary", "remote")
            ])
        return
    if isinstance(coordinator, GoveeApplianceCoordinator):
        if coordinator.model in ICE_MAKER_MODELS:
            async_add_entities([GoveeIceMakerWorkStatus(coordinator)])
        elif coordinator.model in KETTLE_TEMPERATURE_MODELS:
            async_add_entities([GoveeKettleTemperatureSensor(coordinator)])
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


class GoveeKettleTemperatureSensor(GoveeApplianceEntity, SensorEntity):
    """Current kettle water temperature from the APK shared BLE controller."""

    _attr_name = "Water Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveeApplianceCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_water_temperature"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> float | None:
        return self.coordinator.temperature_c


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
        data = self.coordinator.data
        return data.temperature_c if isinstance(data, (ClimateAdvertisement, EnvironmentAdvertisement)) else None


class GoveePassiveHumiditySensor(_GoveePassiveClimateSensor):
    _attr_name = "Humidity"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "humidity")

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.humidity_pct if isinstance(data, (ClimateAdvertisement, EnvironmentAdvertisement)) else None


class GoveePassiveBatterySensor(_GoveePassiveClimateSensor):
    _attr_name = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "battery")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.battery_pct if isinstance(data, ClimateAdvertisement) else None


class GoveePassiveCO2Sensor(_GoveePassiveClimateSensor):
    _attr_name = "Carbon Dioxide"
    _attr_device_class = SensorDeviceClass.CO2
    _attr_native_unit_of_measurement = "ppm"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "carbon_dioxide")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.co2_ppm if isinstance(data, EnvironmentAdvertisement) else None


class GoveePassivePM25Sensor(_GoveePassiveClimateSensor):
    _attr_name = "PM2.5"
    _attr_device_class = SensorDeviceClass.PM25
    _attr_native_unit_of_measurement = "µg/m³"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "pm25")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.pm25_ug_m3 if isinstance(data, EnvironmentAdvertisement) else None


class GoveePassiveProbeTemperatureSensor(GoveePassiveSensorEntity, SensorEntity):
    """One temperature probe reported by a passive Govee probe sensor."""

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, probe: int) -> None:
        super().__init__(coordinator)
        self._probe = probe
        self._attr_name = f"Probe {probe} Temperature"
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_probe_{probe}_temperature"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.probes_c.get(self._probe) if isinstance(data, ProbeAdvertisement) else None


class GoveePassiveAmbientTemperatureSensor(GoveePassiveSensorEntity, SensorEntity):
    _attr_name = "Ambient Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_ambient_temperature"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.ambient_c if isinstance(data, ProbeAdvertisement) else None


class GoveePassiveDualProbeTemperatureSensor(GoveePassiveSensorEntity, SensorEntity):
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, probe: int) -> None:
        super().__init__(coordinator)
        self._probe = probe
        self._attr_name = f"Probe {probe} Temperature"
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_dual_probe_{probe}_temperature"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.probes_c.get(self._probe) if isinstance(data, DualProbeAdvertisement) else None


class GoveePassiveDualProbeHumiditySensor(_GoveePassiveClimateSensor):
    _attr_name = "Probe 1 Humidity"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "dual_probe_1_humidity")

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.humidity_pct if isinstance(data, DualProbeAdvertisement) else None


class GoveePassiveDualProbeBatterySensor(_GoveePassiveClimateSensor):
    _attr_name = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "dual_probe_battery")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.battery_pct if isinstance(data, DualProbeAdvertisement) else None


class GoveeSixProbeTemperatureSensor(GoveePassiveSensorEntity, SensorEntity):
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, probe: int) -> None:
        super().__init__(coordinator)
        self._probe = probe
        self._attr_name = f"Probe {probe} Temperature"
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_six_probe_{probe}_temperature"
        self._attr_device_info = coordinator.device_info

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        return data.probes_c.get(self._probe) if isinstance(data, SixProbeAdvertisement) else None


class GoveeSixProbeBatterySensor(_GoveePassiveClimateSensor):
    _attr_name = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "six_probe_battery")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.battery_pct if isinstance(data, SixProbeAdvertisement) else None


class _GoveeMultiSensorEntity(GoveePassiveSensorEntity, SensorEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, role: str, suffix: str) -> None:
        super().__init__(coordinator)
        self._role = role
        self._attr_name = f"{role.title()} {self._label}"
        self._attr_unique_id = f"{coordinator.address.replace(':', '').lower()}_{role}_{suffix}"
        self._attr_device_info = coordinator.device_info

    def _reading(self) -> ClimateAdvertisement | None:
        data = self.coordinator.data
        return data.readings.get(self._role) if isinstance(data, MultiSensorAdvertisement) else None


class GoveeMultiSensorTemperature(_GoveeMultiSensorEntity):
    _label = "Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = "°C"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, role: str) -> None:
        super().__init__(coordinator, role, "temperature")

    @property
    def native_value(self) -> float | None:
        reading = self._reading()
        return reading.temperature_c if reading else None


class GoveeMultiSensorHumidity(_GoveeMultiSensorEntity):
    _label = "Humidity"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, role: str) -> None:
        super().__init__(coordinator, role, "humidity")

    @property
    def native_value(self) -> float | None:
        reading = self._reading()
        return reading.humidity_pct if reading else None


class GoveeMultiSensorBattery(_GoveeMultiSensorEntity):
    _label = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator, role: str) -> None:
        super().__init__(coordinator, role, "battery")

    @property
    def native_value(self) -> int | None:
        reading = self._reading()
        return reading.battery_pct if reading else None


class GoveeEncryptedEventBatterySensor(_GoveePassiveClimateSensor):
    _attr_name = "Battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = "%"

    def __init__(self, coordinator: GoveePassiveSensorCoordinator) -> None:
        super().__init__(coordinator, "encrypted_event_battery")

    @property
    def native_value(self) -> int | None:
        data = self.coordinator.data
        return data.battery_pct if isinstance(data, EncryptedEventAdvertisement) else None
