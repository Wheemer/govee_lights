"""Advertisement-only coordinator for Govee climate sensors."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components import bluetooth
from homeassistant.core import CALLBACK_TYPE, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN
from .sensor_protocol import ClimateAdvertisement, DualProbeAdvertisement, EnvironmentAdvertisement, MultiSensorAdvertisement, PresenceAdvertisement, ProbeAdvertisement, SixProbeAdvertisement, parse_passive_sensor_advertisement

_LOGGER = logging.getLogger(__name__)


class GoveePassiveSensorCoordinator(DataUpdateCoordinator[ClimateAdvertisement | ProbeAdvertisement | EnvironmentAdvertisement | PresenceAdvertisement | DualProbeAdvertisement | SixProbeAdvertisement | MultiSensorAdvertisement | None]):
    """Maintain state from BLE advertisements without opening GATT."""

    def __init__(self, hass, address: str, model: str) -> None:
        super().__init__(hass, _LOGGER, name=f"Govee {model} ({address})")
        self.address = address
        self.model = model
        self._unsubscribe: CALLBACK_TYPE | None = None

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.address)},
            name=f"Govee {self.model}",
            manufacturer="Govee",
            model=self.model,
        )

    async def async_setup(self) -> None:
        self._unsubscribe = bluetooth.async_register_callback(
            self.hass,
            self._async_on_advertisement,
            bluetooth.BluetoothCallbackMatcher(address=self.address, connectable=False),
            bluetooth.BluetoothScanningMode.PASSIVE,
        )

    async def _async_update_data(self) -> ClimateAdvertisement | ProbeAdvertisement | EnvironmentAdvertisement | PresenceAdvertisement | DualProbeAdvertisement | SixProbeAdvertisement | MultiSensorAdvertisement | None:
        info = bluetooth.async_last_service_info(self.hass, self.address, connectable=False)
        return self._parse(info) if info is not None else self.data

    @callback
    def _async_on_advertisement(
        self, info: bluetooth.BluetoothServiceInfoBleak, _change: bluetooth.BluetoothChange
    ) -> None:
        if reading := self._parse(info):
            if isinstance(reading, DualProbeAdvertisement) and isinstance(self.data, DualProbeAdvertisement):
                # Retain the prior rotating-probe value until its next packet.
                reading = DualProbeAdvertisement(
                    reading.model,
                    {**self.data.probes_c, **reading.probes_c},
                    reading.humidity_pct if reading.humidity_pct is not None else self.data.humidity_pct,
                    reading.battery_pct,
                )
            elif isinstance(reading, MultiSensorAdvertisement) and isinstance(self.data, MultiSensorAdvertisement):
                reading = MultiSensorAdvertisement(reading.model, {**self.data.readings, **reading.readings})
            elif isinstance(reading, SixProbeAdvertisement) and isinstance(self.data, SixProbeAdvertisement):
                reading = SixProbeAdvertisement(reading.model, {**self.data.probes_c, **reading.probes_c}, reading.battery_pct)
            self.async_set_updated_data(reading)

    def _parse(self, info: bluetooth.BluetoothServiceInfoBleak) -> ClimateAdvertisement | ProbeAdvertisement | EnvironmentAdvertisement | PresenceAdvertisement | DualProbeAdvertisement | SixProbeAdvertisement | MultiSensorAdvertisement | None:
        reading = parse_passive_sensor_advertisement(info.name, info.manufacturer_data, tuple(info.service_uuids))
        if reading is None or reading.model != self.model:
            return None
        return reading

    async def async_shutdown(self) -> None:
        await super().async_shutdown()
        if self._unsubscribe is not None:
            self._unsubscribe()
            self._unsubscribe = None
