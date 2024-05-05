
# from faker import Faker

# fake_date = Faker()
# fake_name = fake_date.name 
# # fake_name = fake_data.address
# # fake_name = fake_data.email

# import random 

# test_phone_number = ["+37499999999", "555555 - 55555", "5489-123-456"]
# test_email_address = ["test@mailinator.com", "test", "invalidemailaddres"]

# add_any_data = {
#     "title": f"{fake_name}"
#     "phone_number": f"{test_phone_number}"
# }


import os
from dotenv import load_dotenv
set API_KEY1=your_api_key_value

a = os.environ['API_KEY1']
print(a)

a = os.getenv['API_KEY1', "default_value"]






