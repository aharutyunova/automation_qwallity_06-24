import requests
from add_course import course_id
from login import token
 
 
def delete_course(input_token):
    try:
        DELETE_COURSE_ENDPOINT = f'https://qwallity-prod.onrender.com/courses/course/{course_id}'
        headers = {"Authorization": f"Bearer {input_token}"}
        response = requests.delete(DELETE_COURSE_ENDPOINT, headers=headers)
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
 
 