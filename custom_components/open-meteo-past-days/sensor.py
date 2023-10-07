"""Sensor platform for open-meteo-past-days."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import CONF_MAX_DAYS, CONF_VARIABLES, DOMAIN, VAR_NAMES
from .coordinator import OpenMeteoPastDaysDataUpdateCoordinator
from .entity import OpenMeteoPastDaysEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        OpenMeteoPastDaysSensor(
            coordinator=coordinator,
            entity_description=SensorEntityDescription(
                key=(f"today_{variable}" if i == 0 else f"d_minus{i}_{variable}"),
                name=(
                    f"Today {VAR_NAMES[variable]['label']}"
                    if i == 0
                    else f"D-{i} {VAR_NAMES[variable]['label']}"
                ),
                native_unit_of_measurement=VAR_NAMES[variable][
                    "native_unit_of_measurement"
                ],
                device_class=VAR_NAMES[variable]["device_class"],
                state_class=VAR_NAMES[variable]["state_class"],
            ),
            i=i,
            index=int(entry.data[CONF_MAX_DAYS]) - i,
            variable=variable,
        )
        for i in range(int(entry.data[CONF_MAX_DAYS]) + 1)
        for variable in entry.data[CONF_VARIABLES]
    )


class OpenMeteoPastDaysSensor(OpenMeteoPastDaysEntity, SensorEntity):
    """open-meteo-past-days Sensor class."""

    def __init__(
        self,
        coordinator: OpenMeteoPastDaysDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
        i: int,
        index: int,
        variable: str,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._variable = variable
        self._attr_unique_id = f"{coordinator.config_entry.entry_id}_{i}_{variable}"
        self._index = index

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("daily").get(self._variable)[self._index]
