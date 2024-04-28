# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab - https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)

import json
import os

os.chdir("c:/automation_qwallity_06-24/Lesson_17")
def my_func():
    with open("weather.json", 'r+') as f:
        result = f.read()
        parsedJson = json.loads(result)
        temp = round(parsedJson["main"]["temp"] - 273.15)
        print(f'In {parsedJson["name"]} temp is {temp}C' )

my_func()

