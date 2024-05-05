import requests
from api_endpoints import get_advanced_courses_api
from login import generate_token


def get_advanced_courses():
    token = generate_token()
    global response
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            get_advanced_courses_api,
            headers=headers)
        advanced_courses = response.json()
        if advanced_courses:
            return advanced_courses
        else:
            return f"{advanced_courses} is empty"
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        

courses = get_advanced_courses()["result"]

courses_list = []

if courses:
    c = 0
    for data in courses:
        if c == 10:
            break
        else:
            courses_list.append(data)
        c += 1

print(courses_list)