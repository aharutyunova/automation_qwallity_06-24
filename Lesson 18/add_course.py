import requests


def add_course(course_details, token):
    url = "https://qwallity-prod.onrender.com/add_course/api"
    headers = {'Authorization': token}
    response = requests.post(url, json=course_details, headers=headers)
    if response.status_code == 200:
        try:
            course_response = response.json()
            course_id = course_response.get("id", "")
            return course_id
        except KeyError:
            print("KeyError: 'id' not found in response JSON:",
                  response.json())
            return None
    else:
        print("Failed to add course:", response.text)
        return None
