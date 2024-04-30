import requests

from add_course import course_id
from login import token

UPDATE_COURSE_API_ENDPOINT = f'https://qwallity-prod.onrender.com/course/{course_id}/update'


def update_course_data(input_data, input_token):
    try:
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.patch(UPDATE_COURSE_API_ENDPOINT, json=input_data, headers=headers)
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


# Update course
updated_course = update_course_data(course_data, token)

if updated_course is not None:
    print(f"Updated course with id {course_id}: {updated_course}")
else:
    print("Failed to update course.")
