import requests
from login import token
from endpoints_file import update_course_api
from add_course import added_id


headers = {"Authorization": f"Bearer {token}"}
# Update Course by course_id 
update_body = {
  "title": "Ann_Avt",
  "body": "python_body"
}
response = requests.patch(update_course_api % added_id, json=update_body, headers=headers)
update_fund_course = response.text
print(update_fund_course)