import requests
from requests.auth import HTTPBasicAuth
from config import username, password
from endpoints import endpoint_login


def login():
    response = requests.post(endpoint_login,
                             auth=HTTPBasicAuth(username, password))
    token = response.json()["token"]
    return token
