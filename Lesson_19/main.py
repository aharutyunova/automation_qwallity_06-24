from login import login
from get_advanced_courses_id import get_advanced_courses_id
from validate_response import validate_response
from validate_response import write_to_file
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
valid_data_file_path = os.path.join(current_dir, "valid_data.json")

token = login()
print("Token:", token)

random_10_courses = get_advanced_courses_id(token)

if random_10_courses:
    print("Random courses:", random_10_courses)
    response = validate_response(random_10_courses)
    if response:
        write_to_file(random_10_courses, valid_data_file_path)
else:
    print("No random courses found")
