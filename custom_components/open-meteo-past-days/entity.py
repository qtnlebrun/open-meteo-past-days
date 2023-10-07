"""BlueprintEntity class."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceEntryType

from homeassistant.const import CONF_NAME

from .const import ATTRIBUTION, DOMAIN, NAME, VERSION
from .coordinator import OpenMeteoPastDaysDataUpdateCoordinator


class OpenMeteoPastDaysEntity(CoordinatorEntity):
    """OpenMeteoPastDaysEntity class."""

    _attr_attribution = ATTRIBUTION

    def __init__(self, coordinator: OpenMeteoPastDaysDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            name=coordinator.config_entry.data[CONF_NAME],
            model=VERSION,
            manufacturer=NAME,
            entry_type=DeviceEntryType.SERVICE,
        )
