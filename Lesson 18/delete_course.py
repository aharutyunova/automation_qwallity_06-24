import requests


def delete_course(course_id, token):
    url = f"https://qwallity-prod.onrender.com/courses/course/{course_id}"
    headers = {'Authorization': f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    return response.json()
