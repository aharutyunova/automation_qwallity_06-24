import requests
from requests.auth import HTTPBasicAuth
import config
from endpoints import login_api


def login():
    login_cred = config
    response = requests.post(login_api, auth=HTTPBasicAuth(login_cred.username, login_cred.password))
    token = response.json()["token"]
    print(token)
    return token


if __name__ == '__main__':
    login()