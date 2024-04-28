# Login to https://qwallity-prod.onrender.com/
#  Go to Weather Tab -  https://qwallity-prod.onrender.com/weather
# In Get Weather write any city name and click  Fet Weather
# From Network copy Json response and add it in weather.json file
# Write function which will open that file, parse it and as a result print In [CITY_NAME] temp is [XX]C (temp=273.15)

import json
import os

  
curr_dir = os.getcwd()
new_file = os.path.join(curr_dir, 'Lesson_17_Armine')
sec_file = os.path.join(new_file, 'wheather.json')


def Moscow_wheather():
  with open(r"C:\Users\Արմինա\automation_qwallity_06-24\Lesson_17_Armine\wheather.json") as wheather:
    js_file = json.load(wheather)
    temperature = (js_file["main"]["temp"])
    Kelvin = temperature - 273.15
    celsius = (int(Kelvin))
    city = (js_file["name"])
    result = (f"{city} temperature is {celsius} C")
    print(result)
   

Moscow_wheather()

#Anna jan, whould you please check also Lesson_15, thank you)    
