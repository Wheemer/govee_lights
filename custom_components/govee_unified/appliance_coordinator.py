"""Small local-BLE coordinator for APK-verified Govee appliances."""

from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import Any

from bleak import BleakClient, BleakError
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .appliance_protocol import (
    build_h7172_power_query,
    build_h7172_power_write,
    parse_h7172_power_reply,
    parse_h7172_work_status,
)
from .ble_connection import async_establish_ble_connection
from .const import DOMAIN
from .transport import READ_UUID, WRITE_UUID

_LOGGER = logging.getLogger(__name__)


class GoveeApplianceCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Local Bluetooth control for the APK-confirmed H7172 ice-maker family."""

    def __init__(self, hass, address: str, model: str) -> None:
        super().__init__(hass, _LOGGER, name=f"Govee {model} ({address})", update_interval=timedelta(seconds=60))
        self.address = address
        self.model = model
        self.is_on: bool | None = None
        self.work_status: str = "unknown"
        self._client: BleakClient | None = None
        self._lock = asyncio.Lock()
        self._power_reply = asyncio.Event()

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.address)},
            name=f"Govee {self.model}",
            manufacturer="Govee",
            model=self.model,
        )

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            async with self._lock:
                await self._ensure_connected()
                self._power_reply.clear()
                await self._write(build_h7172_power_query())
                try:
                    async with asyncio.timeout(3):
                        await self._power_reply.wait()
                except TimeoutError:
                    # The APK permits connection even if a status response is delayed;
                    # retain a prior state rather than inventing one.
                    pass
                return self._snapshot()
        except (BleakError, TimeoutError) as err:
            raise UpdateFailed(f"Unable to read Govee {self.model}: {err}") from err

    async def async_set_power(self, enabled: bool) -> None:
        async with self._lock:
            await self._ensure_connected()
            self._power_reply.clear()
            await self._write(build_h7172_power_write(enabled))
            self.is_on = enabled
            self.async_set_updated_data(self._snapshot())
            # Read back with the exact APK query after an optimistic update.
            await self._write(build_h7172_power_query())

    async def _ensure_connected(self) -> None:
        if self._client is not None and self._client.is_connected:
            return
        self._client = await async_establish_ble_connection(self.hass, self.address)
        if self._client.services.get_characteristic(WRITE_UUID) is None:
            raise BleakError(f"Govee {self.model} has no APK control characteristic")
        if self._client.services.get_characteristic(READ_UUID) is not None:
            await self._client.start_notify(READ_UUID, self._notify)

    async def _write(self, frame: bytes) -> None:
        assert self._client is not None
        _LOGGER.debug("H7172 appliance tx %s: %s", self.address, frame.hex())
        await self._client.write_gatt_char(WRITE_UUID, frame, response=False)

    def _notify(self, _sender: int, data: bytearray) -> None:
        frame = bytes(data)
        _LOGGER.debug("H7172 appliance rx %s: %s", self.address, frame.hex())
        power = parse_h7172_power_reply(frame)
        if power is not None:
            self.is_on = power
            self._power_reply.set()
        status = parse_h7172_work_status(frame)
        if status is not None:
            self.work_status = status
        if power is not None or status is not None:
            self.async_set_updated_data(self._snapshot())

    def _snapshot(self) -> dict[str, Any]:
        return {"is_on": self.is_on, "work_status": self.work_status}

    async def async_shutdown(self) -> None:
        if self._client is not None:
            try:
                if self._client.is_connected:
                    await self._client.disconnect()
            except BleakError:
                pass
            self._client = None
