import requests

from api_endpoints import ADD_NEW_COURSE_API_ENDPOINT
from login import token

new_course = {
    "title": "Python title",
    "body": "Python body",
    "coursetype": "1",
    "author": "Admin",
    "price": 50000
}


def add_new_course(input_body, input_token):
    try:
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.post(ADD_NEW_COURSE_API_ENDPOINT, json=input_body, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


# Create new course
new_course = add_new_course(new_course, token)

# Created course id
course_id = new_course["id"]

# print(course_id)
print(f"Created course with id: {course_id}")
