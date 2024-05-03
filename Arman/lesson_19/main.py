# 1) In one python file write functions which will get any 10 of advanced courses id and title ✓
# 2) Add schema validation for check returned data ✓
# 3) Open file and add json data there if validation passes ✓
# 4) Create second .py file and organize code run there ✓
# 5) create bat file to call second .py
# 6) create task scheduler (if we have time)

from get_advanced_courses import get_advanced_courses
from login import get_access_token
from login import user_credentials
from write_json import write_in_json


def main():
    get_access_token(user_credentials)
    get_advanced_courses()
    write_in_json()


if __name__ == '__main__':
    main()
