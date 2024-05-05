import requests
import endpoints

def delete_course(course_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(url = endpoints.delete_course_url.format(course_id), headers = headers)
    try:
        if response.status_code == 200:
            print('Course successfully has deleted')
            return response.status_code
    except AssertionError:
        print("updateERR: Course deletion has failed")