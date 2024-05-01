from add_course import add_new_course, new_course
from delete_course import delete_course
from get_fundamental_course import get_fundamental_course
from login import get_access_token, token
from login import user_credentials
from update_course import update_course_data, update_course_dict


def main():
    get_access_token(user_credentials)
    add_new_course(new_course, token)
    update_course_data(update_course_dict, token)
    get_fundamental_course()
    delete_course(token)


if __name__ == "__main__":
    main()


# The concept is good , the structure also
# I commented functions calls in separate files, because when you import this files, all functions called 
# Also some APIs failed durinf the run (with update/delete APIs we have system issue, they are failed from time to time )
# And hwo I understand you get fundamental courses but missed part of checking, that your course is added
