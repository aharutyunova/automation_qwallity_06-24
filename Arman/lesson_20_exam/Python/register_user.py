import json

import requests

config_data_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\config.json'
user_data_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\Python\data.json'

# !!! I store API endpoint here in file because not works in this version
# Get the value of the 'api_endpoint' key
# api_endpoint = config_data.get('api_endpoint')
api_endpoint = 'https://jsonplaceholder.typicode.com/posts'

# Open config file to read and store configuration data
with open(config_data_file_path, "r") as file:
    config_data = json.load(file)

# Open data.json file where stored user data
with open(user_data_file_path, "r") as file:
    user_data = json.load(file)


def user_registration(input_body):
    try:
        response = requests.post(api_endpoint, json=input_body)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


registered_user_data = user_registration(user_data)
print(registered_user_data)
