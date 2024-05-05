import requests
import random

endpoint = "https://qwallity-prod.onrender.com/courses/advanced/api"


def get_advanced_courses_id(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    courses = response.json()["result"]

    valid_courses = [course['id'] for course in courses if course['id'] is not None]

    if valid_courses:
        random_courses = random.sample(courses, 10)
        return random_courses
    else:
        print("No valid courses found")
        return None
