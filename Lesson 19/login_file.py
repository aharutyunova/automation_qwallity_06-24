import requests
from requests.auth import HTTPBasicAuth
import config_file
from endpoints_file import login_api

def get_auth_token(username = config_file.username, password = config_file.password, url = login_api):
    response = requests.post(login_api, auth=HTTPBasicAuth(username, password))
    try:
        token = response.json()['token']
        return token
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
