import json
import requests
 
from endpoints import ADD_NEW_COURSE_ENDPOINT
from login import token
 
new_course = {
    "title": "Python title",
    "body": "Python body",
    "coursetype": "",
    "author": "Lianna",
    "price": 1618
}
 
 
def add_new_course(input_body, input_token):
    try:
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.post(ADD_NEW_COURSE_ENDPOINT, json=input_body, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None
 
 
# Create new course
new_course = add_new_course(new_course, token)
 
# Created course id
course_id = new_course["id"]
 
# Print created course JSON to the console
print(json.dumps(new_course, indent=4))
 
# print(course_id)
print(f"Created course with id: {course_id}")