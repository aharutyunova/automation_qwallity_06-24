# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)
import os
import json
   
def getWeather(file):
    os.chdir("Lesson_17")
    kelvin = 273.15
    with open(file, 'r+') as f:
        result = json.load(f)
        city = result['name']
        temp =  int(result['main']['temp'] - kelvin)
        return f"The temperature in {city} is {temp}°C."
print(getWeather('weather.json'))

# Anna - Everything is correct