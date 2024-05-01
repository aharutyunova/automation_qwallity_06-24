import config_file
env = config_file.environment

login_api = f"https://qwallity-{env}.onrender.com/login/api"
add_new_corse_api = f"https://qwallity-{env}.onrender.com/add_course/api"
get_course_api = f"https://qwallity-{env}.onrender.com/courses/fundamental/api"
update_course_api = f"https://qwallity-{env}.onrender.com/course/%s/update/"
delete_course_api = f"https://qwallity-{env}.onrender.com/courses/course/%s"
