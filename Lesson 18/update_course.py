import requests
import config_file 
from endpoints_file import login_api, add_course, get_fundamental_course, update_course
from add_course import headers
from add_course import add_course_response

if add_course_response.status_code == 200:
    response_json = add_course_response.json()
    course_id = response_json['id']
    
    
    change = {
        "title": "New_course_update",
        "body": "Again_no_body"
    }

    update_course_response = requests.patch(update_course, json=change, headers=headers)

    if update_course_response.status_code == 200:
        print("Course updated successfully!")
    else:
        print("Failed to update course. Status code:", update_course_response.status_code)

