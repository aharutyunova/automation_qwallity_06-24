import requests
from requests.auth import HTTPBasicAuth
import APIs_endpoints 
import Login  
import Config_file


def Adding_new_course():
    headers_info = {'Authorization': f'Bearer {Login.token}'}
    request2 = requests.post(APIs_endpoints.add_course_post, headers=headers_info, json=Config_file.info)
    print(request2.json())
    return request2.json()
 

print(Adding_new_course())