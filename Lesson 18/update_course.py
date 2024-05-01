import requests


def update_course(course_id, updated_course_details, token):
    url = f"https://qwallity-prod.onrender.com/course/{course_id}/update/"
    headers = {'Authorization': f"Bearer {token}"}
    response = requests.put(url, headers=headers, json=updated_course_details)
    return response.json()
