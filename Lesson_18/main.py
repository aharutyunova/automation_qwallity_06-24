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
import os
from login import login
from add_course import add_course
from get_fundamental_courses import get_fundamental_courses
from get_fundamental_courses import check_course_existence
from update_course import update_course
from delete_course import delete_course

path = os.getcwd()
full_path = os.path.join(path,'Lesson_18')
# os.chdir(full_path)

token = login()
course_id = add_course(token)
fund_course_ids = get_fundamental_courses(token)
check_course_existence(course_id,fund_course_ids)
update_course(course_id, token)
delete_course(course_id, token)


# Anna - good, everything works and readable
# In the future it is better to use logging for track data, instead of print data