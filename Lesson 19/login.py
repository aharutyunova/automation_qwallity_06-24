import requests
from requests.auth import HTTPBasicAuth
import config_file
from endpoints import login_api


def login():
    login_1 = config_file
    response = requests.post(login_api, auth=HTTPBasicAuth(login_1.username, login_1.password))
    token = response.json()["token"]
    print(token)
    return token


if __name__ == '__main__':
    login()