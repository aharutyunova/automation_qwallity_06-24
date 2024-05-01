import requests
from endpoints import endpoint_update_course


def update_course(token, new_course_id, updated_body):
    body = {
        "title": "Test_Lus",
        "body": updated_body
    }

    endpoint_url = endpoint_update_course.format(new_course_id)
    print(f"Course update endpoint URL: {endpoint_url}")

    headers = {"Authorization": f"Bearer {token}"}
    update_course_response = requests.patch(endpoint_url, json=body, headers=headers)

    if update_course_response.status_code != 200:
        print(f"Failed to update course {new_course_id}. Status code: {update_course_response.status_code}")
        return None
    else:
        print(update_course_response.content)
        return None
