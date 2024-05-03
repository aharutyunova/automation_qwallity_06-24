import requests
from endpoints import get_advancecourses_api
import random


def get_advanced_courses(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(get_advancecourses_api, headers=headers)
    courses = response.json()["result"]
    random_ten_courses = random.sample(courses, 10)
    print(random_ten_courses)
    return random_ten_courses