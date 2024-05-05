import requests
import endpoints 

def get_advanced_courses(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url = endpoints.get_advanced_courses_url, headers = headers)
    try:
        response = response.json()['result']
        adv_courses = response[:10]
        return adv_courses
    except KeyError:
        print("advCourseERR: getting of adv courses failed")


