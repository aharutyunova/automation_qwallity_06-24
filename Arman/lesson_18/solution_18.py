import requests
from requests.auth import HTTPBasicAuth

user_name = 'admin_user'
password = '11111111'
login_api = 'https://qwallity-prod.onrender.com/login/api'
get_token = requests.post(login_api, auth=HTTPBasicAuth(user_name, password))
token = get_token.json()['token']

if get_token.status_code == 200:
    print(token)