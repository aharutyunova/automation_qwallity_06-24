import requests
from requests.auth import HTTPBasicAuth
import config_file
from endpoints_file import login_api

# Login
login_cred = config_file
login = requests.post(login_api, auth=HTTPBasicAuth(login_cred.username, login_cred.password))
token = login.json()["token"]
print(token)