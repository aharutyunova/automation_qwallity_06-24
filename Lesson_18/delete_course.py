import requests
from endpoints import endpoint_delete_course


def delete_course(token, new_course_id):

    endpoint_url = endpoint_delete_course.format(new_course_id)
    print(f"Course delete endpoint URL: {endpoint_url}")

    headers = {"Authorization": f"Bearer {token}"}
    delete_course_response = requests.delete(endpoint_url, headers=headers)

    if delete_course_response.status_code != 200:
        print(f"Failed to delete course {new_course_id}. Status code: {delete_course_response.status_code}")
        return None
    else:
        print(delete_course_response.content)
        return None
