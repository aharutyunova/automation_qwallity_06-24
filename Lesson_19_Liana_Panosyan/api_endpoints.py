from config_file import environments
# Log in API
login_api = f"{environments['prod']+'/login/api'}"

# Advanced courses API
get_advanced_courses_api = f"{environments['prod']+'/courses/advanced/api'}"

# print(login_api)
# print(get_advanced_courses_api)
