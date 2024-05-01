import requests
from add_course import added_id
from endpoints_file import get_course_api
from login import token

# get_fundamental_course.py
headers = {"Authorization": f"Bearer {token}"}
get_fund_courses = requests.get(get_course_api, headers=headers)
courses = get_fund_courses.json()["result"]
# print(courses)

for dict in courses:
    if str(dict["id"]) == str(added_id):
        print("course is added")
