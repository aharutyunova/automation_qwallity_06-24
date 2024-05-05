from login import login
from add_course import Adding_new_course
from get_fundamental_course import get_fundamental_course
from update_course import update_course
from delete_course import delete_course


def main():
    if __name__ == '__main__':
        login()
        Adding_new_course()
        get_fundamental_course()
        update_course()
        delete_course()


main()

# An jan you write logic in each separate file correct, but you don't write functions for each action, so your actions are done when you import files,
# but when you write login(), add_new_course() ..etc as function in main() it is incorrect, as you don't have such functions

# You should write each action as function for example 
"""

def login():
    ---
    return token

def add_new_course()
    ...
    return added_id
...etc

"""
# After it you could call all this functions in main()

# Endpoint file, readme files are good enough. config file aslo, only body mostly part of test data than configuration part


"""Using python code and APIs

Login to the system with admin_user account                  /login/api
Add Fundamental Course                                        /add_course/api
Get Fundamental Course and check your course is added           /courses/fundamental/api
Update Course by course_id                                      /course/{course_id}/update/
Delete Course                                                   /courses/course/{course_id}



At the end you should have following Files

Readme
login.py
add_course.py
get_fundamental_course.py
update_course.py
delete_course.py
config file  
endpoints file
main.py """