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

del_courses = requests.delete(f'https://qwallity-prod.onrender.com/courses/course/{course_id}', headers=headers1)
print(del_courses.json())


# Anna - in readme file you should descrive structure of the code - which files you use for which goal and how run the code
# What about the code, you wrote everything in the same file, without write each api action in separate function
# In delete action course_id is not defined, you should get course_id from add_course and use it in del_courses 