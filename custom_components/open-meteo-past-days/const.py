"""Constants for open-meteo-past-days."""
from logging import Logger, getLogger

from homeassistant.components.sensor.const import (
    SensorDeviceClass,
    UnitOfTemperature,
    UnitOfPrecipitationDepth,
    SensorStateClass,
)

LOGGER: Logger = getLogger(__package__)

NAME = "Open-Meteo Past days"
DOMAIN = "open-meteo-past-days"
VERSION = "0.0.0"
ATTRIBUTION = "Data provided by https://open-meteo.com/"
CONF_MAX_DAYS = "max_days"
CONF_VARIABLES = "variables"

VAR_NAMES = {
    "temperature_2m_max": {
        "label": "Maximum Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "native_unit_of_measurement": UnitOfTemperature.CELSIUS,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "temperature_2m_min": {
        "label": "Minimum Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "native_unit_of_measurement": UnitOfTemperature.CELSIUS,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "precipitation_sum": {
        "label": "Precipitation Sum",
        "device_class": SensorDeviceClass.PRECIPITATION,
        "native_unit_of_measurement": UnitOfPrecipitationDepth.MILLIMETERS,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "rain_sum": {
        "label": "Rain Sum",
        "device_class": SensorDeviceClass.PRECIPITATION,
        "native_unit_of_measurement": UnitOfPrecipitationDepth.MILLIMETERS,
        "state_class": SensorStateClass.MEASUREMENT,
    },
}
