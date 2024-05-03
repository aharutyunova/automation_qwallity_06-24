import requests
from requests.auth import HTTPBasicAuth
import APIs_endpoints
import Config_file


def Login_API():
    request1 = requests.post(APIs_endpoints.login_post, auth=HTTPBasicAuth(Config_file.username, Config_file.password))
    global token
    token = (request1.json()['token'])
    print(token)
    return token


Login_API()
    
    



