import requests

from add_course import course_id
from login import token

DELETE_COURSE_API_ENDPOINT = f'https://qwallity-prod.onrender.com/courses/course/{course_id}'


def delete_course(input_token):
    try:
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.delete(DELETE_COURSE_API_ENDPOINT, headers=headers)
        response.raise_for_status()

        # Check if the response contains valid JSON data
        if response.text:
            return response.json()
        else:
            print("Empty response received.")
            return None
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


# Delete course
deleted_course = delete_course(token)

if deleted_course is not None:
    print(f"Deleted course with id {course_id}: {deleted_course}")
else:
    print("Failed to delete course.")
