"""Home Assistant schema compatibility."""

from importlib import import_module
from typing import Any

from homeassistant.helpers import typing as ha_typing

vol: Any = import_module("probatio" if hasattr(ha_typing, "probatio") else "voluptuous")
