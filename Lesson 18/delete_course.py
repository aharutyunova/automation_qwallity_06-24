import requests
import config_file 
from endpoints_file import login_api, add_course, get_fundamental_course, update_course, delete_course
from add_course import headers

try:
    delete_course_response = requests.delete(delete_course, headers=headers, allow_redirects=False)

    if delete_course_response.status_code == 200:
        print("Course deleted successfully!")
    else:
        print("Failed to delete course. Status code:", delete_course_response.status_code)
except ValueError as e:
    print("Error decoding JSON:", e)
