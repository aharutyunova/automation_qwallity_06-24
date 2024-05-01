import requests
from requests.auth import HTTPBasicAuth
from endpoints import login


def user_login(username, password):
    response = requests.post(login, auth=HTTPBasicAuth(username, password))
    access_token = response.json()["token"]
    return access_token
