# In one python file write functions which will get any 10 of advanced courses id and title
# Add schema validation for check returned data
# Open file and add json data there if validation pass
# Create second .py file and organize code run there
# create bat file to call second .py
# create task scheduler (if have time)


from login import login
from get_adv_course import get_advanced_courses
from write_json import write_json


if __name__ == "__main__":

    token = login()
    if token:
        print("Login successful. Token:", token)
        random_ten_courses = get_advanced_courses(token)
        if random_ten_courses:
            write_json(random_ten_courses)
        else:
            print("Failed to retrieve advanced courses.")
    else:
        print("Login failed.")