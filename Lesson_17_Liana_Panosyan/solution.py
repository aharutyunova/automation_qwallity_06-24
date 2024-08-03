# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a
# result print In [CITY_NAME] temp is [XX]C (temp=273.15)

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, "weather.json")


def my_function(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            city_name = data["name"]
            city_temp = data["main"]["temp"] - 273.15
            city_temp = round(city_temp)
            print(f"In {city_name} temp is {city_temp}°C.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


my_function(json_file_path)

# Anna - very good job!!!