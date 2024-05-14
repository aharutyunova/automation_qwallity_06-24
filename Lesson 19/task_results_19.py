# In one python file wtite functions which will get any 10 of advanced courses id and title
# Add schema validation for check returned data
# Open file and add json data there if validation pass
# Create second .py file and organize code run there
# create bat file to call second .py
#  create task scheduler (if have time)

import requests
from requests.auth import HTTPBasicAuth
import config_file
from endpoints_file import get_advanced_api
from login_file import get_auth_token

def get_10_advanced_courses(token):
    headers = {"Authorization": f'Bearer {token}'}
    get_advanced_course_response = requests.get(get_advanced_api, headers=headers)
    get_advanced_course_response = get_advanced_course_response.json()['result']
    advanced_courses = get_advanced_course_response[:10]
    return advanced_courses

