import requests
from requests.auth import HTTPBasicAuth
# from config import username, password
import os


endpoint_login = "https://qwallity-prod.onrender.com/login/api"
username = os.getenv("qwallity_admin_user", "default_value")
password = os.getenv("qwallity_password", "default_value")
print(username, password)


def login():
    response = requests.post(endpoint_login,
                             auth=HTTPBasicAuth(username, password))
    token = response.json()["token"]
    return token
