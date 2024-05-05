import requests
import endpoints 

def add_course(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(url = endpoints.add_course_url,json = endpoints.add_course_body, headers = headers)
    try:
        course_id = response.json()['id']
        print('Course has successfully added')
        return course_id
    except KeyError:
        print("addCourseERR: course adding failed")
