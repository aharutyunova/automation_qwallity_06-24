import requests

from api_endpoints import FUNDAMENTAL_COURSE_API_ENDPOINT
from config_file import user_credentials
from login import token

user_credentials_for_login = user_credentials


def get_fundamental_course():
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            FUNDAMENTAL_COURSE_API_ENDPOINT,
            headers=headers)
        response.raise_for_status()
        fundamental_course_body = response.json()
        if fundamental_course_body:
            return fundamental_course_body
        else:
            return f"{fundamental_course_body} is empty"
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        if response.status_code == 401:
            print("Unauthorized: Check your credentials.")
        return None


print(get_fundamental_course())
