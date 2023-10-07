"""DataUpdateCoordinator for open-meteo-past-days."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.exceptions import ConfigEntryAuthFailed

from .api import (
    OpenMeteoPastDaysApiClient,
    OpenMeteoPastDaysApiClientAuthenticationError,
    OpenMeteoPastDaysApiClientError,
)
from .const import DOMAIN, LOGGER


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class OpenMeteoPastDaysDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        client: OpenMeteoPastDaysApiClient,
    ) -> None:
        """Initialize."""
        self.client = client
        super().__init__(
            hass=hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=timedelta(hours=1),
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.client.async_get_data()
        except OpenMeteoPastDaysApiClientAuthenticationError as exception:
            raise ConfigEntryAuthFailed(exception) from exception
        except OpenMeteoPastDaysApiClientError as exception:
            raise UpdateFailed(exception) from exception