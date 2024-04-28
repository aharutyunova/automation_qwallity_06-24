import json
import os


def print_temperature(city_name, file_name):
    with open(file_name, 'r') as f:
        data_file = json.load(f)
    # Extract city_name, temperature information
    city_name = data_file['name']
    temp_kelvin = data_file['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    # We can also import math and rounded_temp_celsius = math.ceil(temp_celsius)
    rounded_temp_celsius = round(temp_celsius)
    print(f"In {city_name} temp is {rounded_temp_celsius}°C")


file_name = "weather.json"
current_directory = os.getcwd()
full_file_path = os.path.join(current_directory, file_name)
print_temperature(full_file_path, file_name)


# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)