import os
import json
from temp_convertion import Temp_Convertor


current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "weather.json")

with open(data_file, "r") as f:
    weather_data = json.load(f)

kelvin_temp = weather_data[0]["temp"]
converted_temp = Temp_Convertor.kelvin_to_celsius(kelvin_temp)
print(converted_temp)
