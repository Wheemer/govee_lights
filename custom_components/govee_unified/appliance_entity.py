"""Common entity base for local Govee appliances."""

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .appliance_coordinator import GoveeApplianceCoordinator


class GoveeApplianceEntity(CoordinatorEntity[GoveeApplianceCoordinator]):
    _attr_has_entity_name = True

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success and super().available
