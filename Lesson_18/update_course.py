import requests
from login import login
from endpoints_file import update_course_api
from add_course import Adding_new_course
from test_data import updating_course_body


def update_course():
    token = login()  # Get the token 
    added_id = Adding_new_course()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.patch(update_course_api % added_id, json=updating_course_body, headers=headers)
    update_fund_course = response.text
    print(update_fund_course)
    return update_fund_course


if __name__ == '__main__':
    update_course()
