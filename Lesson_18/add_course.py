import requests
import login
from endpoints_file import add_new_corse_api
from test_data import adding_course_body


def Adding_new_course():
    headers = {"Authorization": f"Bearer {login}"}
    add_new_course = requests.post(add_new_corse_api, json=adding_course_body, headers=headers)
    print(add_new_course.json())
    added_id = add_new_course.json()["id"]
    print(added_id)
    return added_id


if __name__ == '__main__':
    Adding_new_course()