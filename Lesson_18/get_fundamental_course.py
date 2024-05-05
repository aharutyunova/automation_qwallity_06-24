import requests
from login import login
from endpoints_file import get_course_api
from add_course import Adding_new_course


def get_fundamental_course():
    token = login()
    added_id = Adding_new_course()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(get_course_api, headers=headers)
    courses = response.json()["result"]
    for course in courses:
        if str(course["id"]) == str(added_id):
            # print("Course is added")
            return courses


if __name__ == '__main__':
    get_fundamental_course()