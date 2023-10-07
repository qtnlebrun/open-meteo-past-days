from __future__ import annotations

import asyncio
import socket

import aiohttp
import async_timeout

from .const import LOGGER


class OpenMeteoPastDaysApiClientError(Exception):
    """Exception to indicate a general API error."""


class OpenMeteoPastDaysApiClientCommunicationError(OpenMeteoPastDaysApiClientError):
    """Exception to indicate a communication error."""


class OpenMeteoPastDaysApiClientAuthenticationError(OpenMeteoPastDaysApiClientError):
    """Exception to indicate an authentication error."""


class OpenMeteoPastDaysApiClient:
    """Open-Meteo API Client"""

    def __init__(
        self,
        latitude: str,
        longitude: str,
        max_days: int,
        variables,
        session: aiohttp.ClientSession,
    ) -> None:
        self._session = session
        self._latitude = latitude
        self._longitude = longitude
        self._max_days = max_days
        self._variables = variables

    async def async_get_data(self) -> any:
        """Get Data"""
        return await self._api_wrapper(
            method="get",
            url="https://api.open-meteo.com/v1/forecast?"
            + f"latitude={self._latitude}"
            + f"&longitude={self._longitude}"
            + f"&daily={','.join(self._variables)}"
            + "&timezone=auto"
            + f"&past_days={self._max_days}"
            + "&forecast_days=1",
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                if response.status in (401, 403):
                    raise OpenMeteoPastDaysApiClientAuthenticationError(
                        "Invalid credentials",
                    )
                response.raise_for_status()
                return await response.json()

        except asyncio.TimeoutError as exception:
            raise OpenMeteoPastDaysApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            LOGGER.error(exception)
            raise OpenMeteoPastDaysApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            raise OpenMeteoPastDaysApiClientError(
                "Something really wrong happened!"
            ) from exception
