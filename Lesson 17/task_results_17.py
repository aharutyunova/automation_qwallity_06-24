# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)

import json
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log.log', 
                    filemode='w+', 
                    encoding='utf-8')

def city_temperature(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            city_name = data['name']
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            print(f"In {city_name} temp is {temp_celsius:.2f}°C (temp={temp_kelvin:.2f})")
        
    except FileNotFoundError:
        logging.error(f"The specified file '{filename}' does not exist.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

filename = "city_weather.json"
city_temperature(filename)

# Anna - Everything is correct, only what about exception, in case you use general exception you could not additionally use FileNotFoundError exception,
# as this exception will be catched in line 27 


def city_weather(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

        country_name = data['sys']['country']
        weather_description = data['weather'][0]['description']
        country_name = 'Armenia'
        weather_description = "the sky looks like a colorful painting with soft colors today:"

        print(f'Country is {country_name} and {weather_description}')

file = "city_weather.json"
city_weather(file)


# Anna - in this function, I didn't understand, why you hardcoded  country_name and weather_description values, in case you also get it fron json in line 41 and 42

