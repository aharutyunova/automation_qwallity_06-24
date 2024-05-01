import requests
from requests.auth import HTTPBasicAuth
import config

# Login
username = "admin_user"
password = "11111111"


response = requests.post('https://qwallity-dev.onrender.com/login/api', auth=HTTPBasicAuth(username, password))

print(response)

response.status_code

token = response.json()['token']

body = {
  "title": "Anush_course",
  "body": "string",
  "coursetype": "2",
  "author": "string",
  "price": 0
}

h = {"Authorization": f'Beraer {token}'}
add_course = requests.post('https://qwallity-prod.onrender.com/add_course/api', json=body, headers=h)
print(add_course.json())


headers1 = {"Authorization": f"Bearer {token}"}

del_courses = requests.delete('https://qwallity-prod.onrender.com/courses/course/{course_id}', headers=headers1)
print(del_courses.json())
