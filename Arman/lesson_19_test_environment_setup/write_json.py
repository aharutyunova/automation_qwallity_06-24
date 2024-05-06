import json
import os

from get_advanced_courses import ten_courses

# Store already 10 advanced courses from get_advanced_courses in advanced_courses
advanced_courses = ten_courses


def write_in_json():
    """Function writes advanced courses json data in the advanced_courses.json file"""
    current_directory = os.getcwd()
    advanced_courses_json_file = r'/Arman/lesson_19_test_environment_setup\advanced_courses.json'
    file_full_path = os.path.join(current_directory, advanced_courses_json_file)

    if file_full_path:
        with open(file_full_path, 'w') as json_file:
            json.dump(advanced_courses, json_file, indent=4)
    else:
        raise Exception("File not found in lesson_19 directory")
    return "JSON data successfully written in advanced_courses.json file"
