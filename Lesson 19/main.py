import json
import config_file
from endpoints_file import get_advanced_api
from login_file import get_auth_token
from task_results_19 import get_10_advanced_courses
from validation_scheme import Advanced_Course_Schema
from validation_scheme import validate_advanced_courses

token = get_auth_token()
courses = get_10_advanced_courses(token)
if validate_advanced_courses(courses):
    with open("advanced_courses.json", 'w+') as f:
        f.write(json.dumps(courses,indent=4))