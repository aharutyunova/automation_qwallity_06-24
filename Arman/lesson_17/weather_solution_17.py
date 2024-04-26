# Login to https://qwallity-prod.onrender.com/
# Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)

import json
import os

# Get current working directory path
current_file = os.getcwd()

# Join current working directory path with weather.json
weather_json = os.path.join(current_file, "weather.json")


def fahrenheit_to_celsius(input_temp):
    FAHRENHEIT_VALUE = 273.15
    """function returns converted temperature value from Fahrenheit to Celsius"""
    return round(input_temp - FAHRENHEIT_VALUE)


def get_city_and_temperature(input_json):
    """Get city and temperature from weather json and return result"""
    city = ""
    fahrenheit = 0

    # Open and read weather.json file data
    with open(weather_json, "r+") as f:
        json_file = f.read()

    # Convert json to dictionary
    json_to_dict = json.loads(json_file)

    # Loop get city name and temperature from weather dictionary
    for dict in json_to_dict:
        if dict == "main":
            for key, value in json_to_dict[dict].items():
                if key == "temp":
                    fahrenheit = value
        elif dict == "name":
            city = json_to_dict[dict]

    return f"{city} temp is {fahrenheit_to_celsius(fahrenheit)}°C (temp={fahrenheit})"


print(get_city_and_temperature(weather_json))
