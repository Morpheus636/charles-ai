import json
import logging
import os

import requests

from ... import config


logger = logging.getLogger(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")

spec = {
    "plugin": "weather",
    "description": "Fetches information about the weather.",
    "args": {
        "zip": "Required argument, the zip code of the place to get weather information about.",
        "country": "Required argument, the country code of the place to get weather information about.",
    },
}


def run(**kwargs):
    # Error out if there is no API key.
    if not API_KEY:
        logger.error(
            "Missing Weather API key. Populate WEATHER_API_KEY env var with an API key for openweathermap.org"
        )
        return "The weather plugin could not get weather information because there is no API key."

    # Validate args
    zip = kwargs.get("zip")
    if not zip:
        logger.error("No zip code specified.")
        return "The weather plugin could not get weather information because the zip arg was not specified."
    country = kwargs.get("country")
    if not country:
        logger.error("No country code specified.")
        return "The weather plugin could not get weather information because the country arg was not specified."

    # Geocoding - https://openweathermap.org/api/geocoding-api
    response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},{country}&appid={API_KEY}"
    )
    status = response.status_code
    if status != 200:
        logger.error(f"Weather API returned status code {status}")
        return f"The weather plugin could not get weather information because the API returned HTTP status code {status}"
    response_json = response.json()
    lat = response_json["lat"]
    lon = response_json["lon"]

    # Send the request to the weather API
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={config.units}&appid={API_KEY}"
    )
    # Curate this JSON to include only the important information.
    weather_json = response.json()
    logger.debug(f"Received response: \n{weather_json}")
    curated = {}
    if config.units == "metric":
        curated["temperature units"] = "degrees celcius"
    elif config.units == "imperial":
        curated["temperature units"] = "degrees fahrenheit"
    curated["current conditions"] = weather_json["weather"][0]["description"]
    curated["current temputature"] = weather_json["main"]["temp"]
    curated["feels like temperature"] = weather_json["main"]["feels_like"]
    curated["low temperature"] = weather_json["main"]["temp_min"]
    curated["high temperature"] = weather_json["main"]["temp_max"]
    return f"{json.dumps(curated)}"
