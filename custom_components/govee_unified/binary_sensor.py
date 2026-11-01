"""LAN connectivity entity dispatch for Govee Unified."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Only LAN entries expose the copied connectivity sensor."""
    if "lan_ip" not in config_entry.data:
        return
    from .lan_binary_sensor import async_setup_entry as async_setup_lan_entry

    await async_setup_lan_entry(hass, config_entry, async_add_entities)
