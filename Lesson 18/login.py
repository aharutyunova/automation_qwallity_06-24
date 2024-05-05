import requests
from endpoints_file import login_api
from requests.auth import HTTPBasicAuth
import config_file 

username = config_file.username
password = config_file.password

response = requests.post(login_api, auth=HTTPBasicAuth(username, password))
token = response.json()['token']

print(token)