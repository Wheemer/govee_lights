"""Local LAN setup step imported from the Govee Lights implementation."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from .const import CONF_LAN_DEVICE_ID, CONF_LAN_IP, CONF_LAN_SKU
from .lan_coordinator import GoveeLANCoordinator


async def async_step_lan(flow: Any, user_input: dict[str, Any] | None = None) -> Any:
    """Discover or manually add a local Govee LAN device to the active flow.

    This is intentionally a narrow helper, not a second ConfigFlow subclass:
    the unified integration owns Bluetooth discovery and transport selection.
    """
    errors: dict[str, str] = {}
    discovered: dict[str, Any] = getattr(flow, "_lan_discovered", {})

    if not discovered:
        found = await GoveeLANCoordinator.discover_devices(flow.hass)
        discovered = {f"{device.sku} ({device.ip})": device for device in found}
        flow._lan_discovered = discovered

    if user_input is not None:
        choice = user_input.get("lan_device_key", "")
        manual_ip = (user_input.get(CONF_LAN_IP) or "").strip()
        manual_sku = (user_input.get(CONF_LAN_SKU) or "").strip()

        ip = device_id = sku = ""
        if choice and choice in discovered:
            device = discovered[choice]
            ip, device_id, sku = device.ip, device.fingerprint, device.sku
        elif manual_ip and manual_sku:
            ip, sku = manual_ip, manual_sku
        else:
            errors["base"] = "no_device_selected"

        if not errors:
            if not await GoveeLANCoordinator.test_connectivity(flow.hass, ip):
                errors["base"] = "cannot_connect"
            else:
                unique_id = (
                    device_id.replace(":", "").upper()
                    if device_id
                    else f"lan_{ip.replace('.', '_')}"
                )
                await flow.async_set_unique_id(unique_id, raise_on_progress=False)
                flow._abort_if_unique_id_configured()
                return flow.async_create_entry(
                    title=f"{sku} (LAN)",
                    data={CONF_LAN_IP: ip, CONF_LAN_DEVICE_ID: device_id, CONF_LAN_SKU: sku},
                )

    schema: dict[Any, Any] = {}
    if discovered:
        schema[vol.Optional("lan_device_key")] = vol.In(list(discovered))
    schema[vol.Optional(CONF_LAN_IP)] = str
    schema[vol.Optional(CONF_LAN_SKU)] = str
    return flow.async_show_form(
        step_id="lan",
        data_schema=vol.Schema(schema),
        description_placeholders={"discovered": str(len(discovered))},
        errors=errors,
    )
