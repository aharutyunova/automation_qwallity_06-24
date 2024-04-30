from config_file import environments

LOGIN_API_ENDPOINT = f'{environments["production"]}/login/api'
FUNDAMENTAL_COURSE_API_ENDPOINT = f'{environments["production"]}/courses/fundamental/api'
ADD_NEW_COURSE_API_ENDPOINT = f'{environments["production"]}/add_course/api'
