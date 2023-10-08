# Open-Meteo Past days

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

This integration provides sensors for selected variables for past days and today Forecast

**Available variables :**

Variable | Sensor name | Description
-- | -- | --
`Maximum Temperature` <br> `Minimum Temperature`| sensor.today_maximum_temperature or sensor.d_X_maximum_temperature <br> sensor.today_minimum_temperature or sensor.d_X_minimum_temperature | Maximum and minimum daily air temperature at 2 meters above ground
`Precipitation Sum` | sensor.today_precipitation_sum or sensor.d_X_precipitation_sum | Sum of daily precipitation (including rain, showers and snowfall)
`Rain Sum` | sensor.today_maximum_temperature or sensor.d_X_maximum_temperature | Sum of daily rain
`Reference Evapotranspiration` | sensor.today_maximum_temperature or sensor.d_X_maximum_temperature | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `open-meteo-past-days`.
1. Download _all_ the files from the `custom_components/open-meteo-past-days/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Open-Meteo Past days"

## Configuration is done in the UI

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[open-meteo-past-days]: https://github.com/qtnlebrun/open-meteo-past-days
[commits-shield]: https://img.shields.io/github/commit-activity/y/qtnlebrun/open-meteo-past-days.svg?style=for-the-badge
[commits]: https://github.com/qtnlebrun/open-meteo-past-days/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/qtnlebrun/open-meteo-past-days.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%20%40qtnlebrun-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/qtnlebrun/open-meteo-past-days.svg?style=for-the-badge
[releases]: https://github.com/qtnlebrun/open-meteo-past-days/releases
