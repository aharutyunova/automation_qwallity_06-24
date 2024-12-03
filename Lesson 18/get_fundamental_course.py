import requests
import config_file 
from endpoints_file import login_api, add_course, get_fundamental_course
from add_course import headers
from add_course import add_course_response

if add_course_response.status_code == 200:
    response_json = add_course_response.json()
    course_id = response_json['id']
    
    course_to_check = course_id
    get_fundamental_course_response = requests.get(get_fundamental_course, headers=headers)

    if get_fundamental_course_response.status_code == 200:
        fundamental_courses = get_fundamental_course_response.json()


        if any(isinstance(course, dict) and course_to_check == course.get('id') for course in fundamental_courses):
            print(f"The course '{course_to_check}' exists in the Fundamental course list.")
        else:
            print(f"The course '{course_to_check}' does not exist in the Fundamental course list.")
else:
    print("Failed to add course. Status code:", add_course_response.status_code)
