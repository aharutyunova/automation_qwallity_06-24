import json
    
with open("json_Anush.json", 'r') as f:
    data = json.read(f)
    
    
name_of_city = data.get("name")
temp_kelvin = data["main"].get("temp", 273.15)
    
temp_celsius = temp_kelvin - 273.15
    
print(f"In {name_of_city}, temp is {temp_celsius:.2f}C")