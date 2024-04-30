import requests
from requests.auth import HTTPBasicAuth

from api_endpoints import LOGIN_API_ENDPOINT
from config_file import user_credentials

user_credentials_for_login = user_credentials


def get_access_token(input_credentials):
    try:
        response = requests.post(LOGIN_API_ENDPOINT,
                                 auth=HTTPBasicAuth(input_credentials["username"], input_credentials["password"]))
        response.raise_for_status()
        access_token = response.json()['token']
        return access_token
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


def is_logged_in(input_token):
    is_logged = False
    if input_token:
        is_logged = True
    return is_logged


# Get access token
token = get_access_token(user_credentials_for_login)

print(f"Is logged in: {is_logged_in(token)}")

# Print access token to the console
print(token)
