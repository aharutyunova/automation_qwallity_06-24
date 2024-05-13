import requests
from requests.auth import HTTPBasicAuth
import config_file
from endpoints_file import login_api


def login():
    login_cred = config_file
    response = requests.post(login_api, auth=HTTPBasicAuth(login_cred.username, login_cred.password))
    token = response.json()["token"]
    print(token)
    return token


if __name__ == '__main__':
    login()
