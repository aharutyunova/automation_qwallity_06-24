from add_course import add_new_course
from delete_course import delete_course
from get_fundamental_course import get_fundamental_course
from login import get_access_token
from login import user_credentials
from update_course import update_course_data


def main():
    get_access_token()
    add_new_course()
    update_course_data()
    get_fundamental_course()
    delete_course()


if __name__ == "__main__":
    main()
