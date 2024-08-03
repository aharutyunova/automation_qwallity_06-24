import requests
from requests.auth import HTTPBasicAuth


from config_file import credentials
from api_endpoints import login_api


def generate_token():
    response = requests.post(login_api, auth=HTTPBasicAuth(credentials['username'], credentials['password']))
    token = response.json()["token"]
    return token
