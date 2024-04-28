import json
import os


def print_weather(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        city_name = data['name']
        temperature = data['main']['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
    print(f'In {city_name} temp is {temperature:.2f}°C')


json_file = "weather.json"
current_directory = os.getcwd()
full_file_path = os.path.join(current_directory, json_file)
print_weather(full_file_path)

# Anna jan please also review my solution to lesson 16, pease ^_^
