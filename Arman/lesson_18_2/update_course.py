import requests

from add_course import course_id
from login import token

UPDATE_COURSE_API_ENDPOINT = f'https://qwallity-prod.onrender.com/course/{course_id}/update/'

# Check which course is going to be updated to the console
print(UPDATE_COURSE_API_ENDPOINT)

update_course_dict = {
    "title": "Update Python course title",
    "body": 'Update Python course body',
}


def update_course_data(input_data, input_token):
    try:
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.patch(UPDATE_COURSE_API_ENDPOINT, json=input_data, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


# except requests.exceptions.RequestException as error:
#     print(f"Error occurred: {error}")
#     return None


# Update course
updated_course = update_course_data(update_course_dict, token)

if updated_course is not None:
    print(updated_course)
else:
    print("Failed to update course.")
