"""
1. Create Virtual env +
2. Activate it and use as interpretator +
3. Write pyhton code to register user via API +
4. Keep endpoint in environment variable and get from there in python code +
5. Generate username and email randomly for registration
6. Create bat file to run the program
7. Add used packages to requirements.txt file
"""
from endpoints import register_url
import requests

from faker import Faker

def generate_random_email():
    fake = Faker()
    return fake.email()

random_email = generate_random_email()
print("Random email:", random_email)

def generate_random_username():
    fake = Faker()
    return fake.user_name()

random_username = generate_random_username()
print("Random username:", random_username)

def register(url = register_url, email = random_email, username = random_username):
    body = {
            "first_name": "testnnn",
            "email": email,
            "username": username,
            "password": "testgroup3",
            "role_id": 2,
            "account": 100
            }
    response = requests.post(url, json = body)
    return response
print(register().json())