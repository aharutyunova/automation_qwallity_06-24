import requests
from requests.auth import HTTPBasicAuth
import APIs_endpoints
import Login


def Get_fund_course():
    head = {'Authorization': f'Bearer {Login.token}'}
    request3 = requests.get(APIs_endpoints.get_fundamental_course, headers = head)
    print(request3.json())
    return request3.json()


print(Get_fund_course())