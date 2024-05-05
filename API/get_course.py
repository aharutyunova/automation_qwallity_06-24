import requests
 
from endpoints import FUNDAMENTAL_COURSE_ENDPOINT
from config_file import valid_user_credentials
from login import token
 
user_credentials_for_login = valid_user_credentials
 
 
def get_fundamental_course():
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            FUNDAMENTAL_COURSE_ENDPOINT,
            headers=headers)
        response.raise_for_status()
        fundamental_course_body = response.json()
        return fundamental_course_body
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        if response.status_code == 401:
            print("Unauthorized: Check your credentials.")
        return None