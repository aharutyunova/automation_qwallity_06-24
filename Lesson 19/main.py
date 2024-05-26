from login import login
from get_advanced_courses import get_advanced_courses
from my_json import append_to_json

if __name__ == "__main__":
    token = login()
    if token:
        print("Login successful. Token:", token)
        random_ten_courses = get_advanced_courses(token)
        if random_ten_courses:
            print(random_ten_courses)
            for course in random_ten_courses:
                append_to_json(course)
            print("Data appended to data.json.")
        else:
            print("Failed to retrieve advanced courses.")
    else:
        print("Login failed.")
