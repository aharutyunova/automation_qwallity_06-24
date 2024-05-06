from config_file import environments

# Authorization / Login API to get access token
LOGIN_API_ENDPOINT = f'{environments["production"]}/login/api'

# Advanced courses API
FUNDAMENTAL_COURSE_API_ENDPOINT = f'{environments["production"]}/courses/advanced/api'
