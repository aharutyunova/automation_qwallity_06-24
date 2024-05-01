import requests
from login import token
from endpoints_file import add_new_corse_api
from config_file import body

# Add Fundamental Course 
headers = {"Authorization": f"Bearer {token}"}
add_new_course = requests.post(add_new_corse_api, json=body, headers=headers)
print(add_new_course.json())
added_id = add_new_course.json()["id"]
print(added_id)