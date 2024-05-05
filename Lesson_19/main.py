# import os
import json
from login import login
from get_advanced_courses import get_advanced_courses
from schema_validation import AdvCourseSchema
from schema_validation import validate_adv_courses

# path = os.getcwd()
# full_path = os.path.join(path,'Lesson_19')
# os.chdir(full_path)

token = login()
courses = get_advanced_courses(token)
if validate_adv_courses(courses):
    with open("AdvCourses.json", 'w+') as f:
        f.write(json.dumps(courses,indent=4))

# Ann jan please also check Lesson_16 and Lesson_18, sorry(