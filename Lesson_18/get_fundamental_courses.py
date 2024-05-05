import requests
import endpoints 

def get_fundamental_courses(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url = endpoints.get_fundamental_courses_url, headers = headers)
    try:
        fund_courses = response.json()['result']
        fund_course_ids = []
        for course in fund_courses:
            fund_course_ids.append(course['id'])
        print("Fundamental courses successfully have got")
        return fund_courses
    except KeyError:
        print("fundCourseERR: getting of fund courses failed")

def check_course_existence(course_id, fund_course_ids):
    try:
        for id in fund_course_ids:
            if course_id == id:
                print("Course successfully added")
                return True
            break
    except AssertionError:
        print("courseNotFoundERR: added course not found in given course ids")