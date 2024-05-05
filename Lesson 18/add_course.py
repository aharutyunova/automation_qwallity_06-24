import requests
from requests.auth import HTTPBasicAuth
from endpoints_file import login_api, add_course
import config_file 
from login import token

username = config_file.username
password = config_file.password

body = {
  "title": "New_course",
  "body": "Nobody",
  "coursetype": "1",
  "author": "Shushan",
  "price": 55
}

headers = {"Authorization": f'Bearer {token}'}
add_course_response = requests.post(add_course, json=body, headers=headers)

if add_course_response.status_code == 200:
    print("Course added successfully!")
    print(add_course_response.json())
else:
    print("Failed to added course. Status code:", add_course_response.status_code)
