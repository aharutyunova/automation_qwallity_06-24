import requests
from login import login
from add_course import Adding_new_course
from endpoints_file import delete_course_api


def delete_course():
    token = login()
    added_id = Adding_new_course()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url=(delete_course_api % added_id), headers=headers)
    del_fund_course = response.text
    print(del_fund_course)
    return del_fund_course


if __name__ == '__main__':
    delete_course()
