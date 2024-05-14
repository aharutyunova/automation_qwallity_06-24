import requests
import login
from endpoints import register_user_API
from test_data import register_body
from faker import Faker

fake = Faker()
fake_email = fake.email()
fake_username = fake.user_name()

print("Fake Username:", fake_username)

print("Fake Username:", fake_username)



def register_user():
    headers = {"Authorization": f"Bearer {login}"}
    register_user = requests.post(register_user_API)
    print(add_new_course.json())
    added_id = add_new_course.json()["id"]
    print(added_id)
    return added_id


if __name__ == '__main__':
    Adding_new_course()