import requests
from login import token
from add_course import added_id
from endpoints_file import delete_course_api


headers = {"Authorization": f"Bearer {token}"}

del_fund_courses = requests.delete(url=(delete_course_api % added_id), headers=headers)
courses = del_fund_courses.text
print(courses)