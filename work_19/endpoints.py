from data.env import user_name, secret_api_key
from config import prod_env
 
LOGIN_ENDPOINT = f'{prod_env["production"]}/login/api'
FUNDAMENTAL_COURSE_ENDPOINT = f'{prod_env["production"]}/courses/fundamental/api'
ADD_NEW_COURSE_ENDPOINT = f'{prod_env["production"]}/add_course/api'