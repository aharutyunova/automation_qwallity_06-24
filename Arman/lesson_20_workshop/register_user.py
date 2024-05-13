import json

import requests
from faker import Faker

from api_endpoints import REGISTER_USER_API

fake_data = Faker()

random_user = {
    "first_name": f"{fake_data.first_name()}",
    "email": f"{fake_data.email()}",
    "username": f"{fake_data.user_name()}",
    "password": f"{fake_data.password()}",
    "role_id": 2,
    "account": 100
}


def register_user(user_input_body):
    try:
        response = requests.post(REGISTER_USER_API, json=user_input_body)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


new_user = register_user(random_user)

new_user_json = json.dumps(new_user, indent=4)

# print(course_id)
print(f"User successfully registered: {new_user_json}")
