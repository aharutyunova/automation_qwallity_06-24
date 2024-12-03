import requests
import config_file
import add_course
import get_fundamental_course
import update_course
import delete_course



# Anna - generally you did correct steps, but
#   - This is not correct structure, when in main file you have imports of files and code run in that files
#  You should write functions in each file and from main file, after import call functions of each page, for example, delete_course.delete()

# Also you had variable sin api (update and delete) and use apis without replace variables in the value,
# so you send 'https://qwallity-prod.onrender.com/courses/course/{course_id}' instead of 'https://qwallity-prod.onrender.com/courses/course/XXXXXX'