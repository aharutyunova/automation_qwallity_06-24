import requests
from endpoints import endpoint_get_fund_courses


def get_added_fundamental_course(token, new_course_id):
    headers = {"Authorization": f"Bearer {token}"}
    get_added_f_course = requests.get(endpoint_get_fund_courses,
                                      headers=headers)

    if get_added_f_course.status_code != 200:
        print("Error:", get_added_f_course.text)
        return None

    try:
        courses = get_added_f_course.json()["result"]
        print("New Course ID:", new_course_id)

        for course in courses:
            if str(course["id"]) == str(new_course_id):
                print(f"Newly Added Course ID: {course['id']}")
                return course["id"]

    except Exception as e:
        print("Error parsing JSON:", e)
        return None
