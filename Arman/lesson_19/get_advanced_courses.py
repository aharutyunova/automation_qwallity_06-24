import requests

from api_endpoints import FUNDAMENTAL_COURSE_API_ENDPOINT
from login import token


def get_advanced_courses():
    """Function get advanced courses json data"""
    global response
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            FUNDAMENTAL_COURSE_API_ENDPOINT,
            headers=headers)
        response.raise_for_status()
        fundamental_course_body = response.json()
        if fundamental_course_body:
            return fundamental_course_body
        else:
            return f"{fundamental_course_body} is empty"
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        if response.status_code == 401:
            print("Unauthorized: Check your credentials.")
        return None


# Get result list from courses json
courses_json = get_advanced_courses()["result"]

# Empty courses list to append first 10 courses from advanced courses
ten_courses = []

# Append 10 advanced courses from courses_json to ten_courses
if courses_json:
    temp = 0
    for dict in courses_json:
        if temp == 10:
            break
        else:
            ten_courses.append(dict)
        temp += 1

# Print ten courses to console for debug
print(ten_courses)
