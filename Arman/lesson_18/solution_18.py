import requests
from requests.auth import HTTPBasicAuth

from api_endpoints import *
from user_credentials import *

# Authorization with post method
get_token = requests.post(login_api, auth=HTTPBasicAuth(user_name, password))

# store token in the token variable
token = get_token.json()['token']

headers = {'Authorization': f'Bearer {token}'}

if get_token.status_code == 200:
    print(token)

add_course_api_endpoint = 'https://qwallity-prod.onrender.com/add_course/api'

course_body = {
    "title": "python_title",
    "body": 'python_body',
    "coursetype": "1",
    "author": "python_author",
    "price": 500
}

add_course = requests.post('add_course_api_endpoint', json=course_body, headers=headers)

get_courses = requests.get(advanced_courses_api_endpoint, headers={'Authorization': token})

courses = get_courses.json()['result']

for dict in courses:
    if dict["title"] == "python_title":
        print("found")
