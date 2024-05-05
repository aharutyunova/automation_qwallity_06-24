import requests
from endpoints import get_advanced_courses_api
import random


def get_advanced_courses(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(get_advanced_courses_api, headers=headers)
    courses = response.json().get("result", [])
    random_ten_courses = random.sample(courses, min(len(courses), 10))
    return random_ten_courses
