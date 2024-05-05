import requests
from requests.auth import HTTPBasicAuth
import endpoints
import config

def login(username = config.username, password = config.password, url = endpoints.login_url):
    response = requests.post(url=url, auth = HTTPBasicAuth(username, password))
    try:
        token= response.json()['token']
        print('User Successfully has logged in')
        return token
    except KeyError:
        print('LoginErr: Login failed')
    