from login import login
from add_course import add_course
from get_fundamental_course import get_added_fundamental_course
from update_course import update_course
from delete_course import delete_course


token = login()
print("Token:", token)

new_course_id = add_course(token)

newly_added_id = get_added_fundamental_course(token, new_course_id)

updated_body = "updated_by_Lus"
update_course(token, new_course_id, updated_body)

delete_course(token, new_course_id)
