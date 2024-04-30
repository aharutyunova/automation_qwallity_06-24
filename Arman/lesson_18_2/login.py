import requests
from requests.auth import HTTPBasicAuth

from api_endpoints import LOGIN_API_ENDPOINT
from config_file import user_credentials


def get_access_token():
    try:
        get_token = requests.post(LOGIN_API_ENDPOINT,
                                  auth=HTTPBasicAuth(user_credentials["username"], user_credentials["password"]))
        access_token = get_token.json()['token']
        return access_token
    except Exception as error:
        print(error)


token = get_access_token()
print(token)
