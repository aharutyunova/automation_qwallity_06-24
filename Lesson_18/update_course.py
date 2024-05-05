import requests
import endpoints

def update_course(course_id,token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.patch(url = endpoints.update_course_url.format(course_id), json = endpoints.update_add_course_body, headers = headers)
    try:
        if response.status_code == 200:
            print('Course successfully has updated')
            return response.status_code
    except AssertionError:
        print("updateERR: Course update has failed")
