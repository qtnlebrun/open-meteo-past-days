"""Adds config flow for Blueprint."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector as sel
from homeassistant.helpers import config_validation as cv
from homeassistant.const import (
    CONF_LOCATION,
    CONF_NAME,
)

from .const import CONF_MAX_DAYS, CONF_VARIABLES, DOMAIN, VAR_NAMES


DEFAULT_NAME = "Home"


class OpenMeteoPastDaysFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for OpenMeteoPastDays."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )
        if user_input is None:
            default_input = {}
        else:
            default_input = user_input

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default=default_input.get(CONF_NAME, DEFAULT_NAME)
                    ): cv.string,
                    vol.Required(
                        CONF_LOCATION,
                        default=default_input.get(
                            CONF_LOCATION,
                            {
                                "latitude": self.hass.config.latitude,
                                "longitude": self.hass.config.longitude,
                            },
                        ),
                    ): sel.LocationSelector(),
                    vol.Required(
                        CONF_MAX_DAYS, default=default_input.get(CONF_MAX_DAYS, 5)
                    ): sel.NumberSelector({"min": 1, "max": 99, "mode": "box"}),
                    vol.Required(CONF_VARIABLES): sel.SelectSelector(
                        {
                            "multiple": "true",
                            "mode": "list",
                            "options": [
                                ({"label": VAR_NAMES[key]["label"], "value": key})
                                for key in VAR_NAMES
                            ],
                        }
                    ),
                }
            ),
            errors=_errors,
        )
