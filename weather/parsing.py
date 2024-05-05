import os
import json

def parse_weather(folder_name, json_file, new_json_file):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Path to the JSON file
    json_path = os.path.join(folder_name, json_file)
    
    # Check if the JSON file exists
    if not os.path.exists(json_path):
        print("Weather file not found.")
        return
    
    # Load the JSON data from the file
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Extract temperature and city name from the first entry
    city_name = data[0].get('name', 'Armenia')
    temp = data[0].get('temp', 20) - 273.15
    
    # Print the result
    print(f"{city_name} temp is {temp:.2f}°C")

    # Write the data to a new JSON file
    new_json_path = os.path.join(folder_name, new_json_file)
    with open(new_json_path, 'w') as f:
        json.dump(data, f)

# Example usage:
folder_name = "weather"
json_file = "weather.json"
new_json_file = "new_weather.json"
parse_weather(folder_name, json_file, new_json_file)
