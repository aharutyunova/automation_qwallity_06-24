import requests
from endpoints import endpoint_add_course


def add_course(token):
    body = {
        "title": "Test_Lus",
        "body": "string2",
        "coursetype": "1",
        "author": "Lusine",
        "price": 457452
    }

    headers = {"Authorization": f"Bearer {token}"}
    add_course_response = requests.post(endpoint_add_course, json=body,
                                        headers=headers)
    if add_course_response.status_code == 200:
        try:
            new_course_id = add_course_response.json()["id"]
            return new_course_id
        except KeyError:
            print("KeyError: 'id' not found in response JSON:",
                  add_course_response.json())
            return None
    else:
        print("Failed to add course:", add_course_response.text)
        return None
