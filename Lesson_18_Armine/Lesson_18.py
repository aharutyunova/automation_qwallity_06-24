import requests
from requests.auth import HTTPBasicAuth 

username = 'admin_user'
password = '11111111'


response = requests.post('https://qwallity-prod.onrender.com/login/api', auth=HTTPBasicAuth(username, password))

token = response.json()['token']




#add_new_course


info= {
  "title": "Armine",
  "body": "This course is about python",
  "coursetype": "1",
  "author": "Barseghyan",
  "price": 3333
}

head = {'Authorization': f'Bearer {token}'}

request_body = requests.post('https://qwallity-prod.onrender.com/add_course/api', json=info, headers=head)
print(request_body.json())
