import requests


def get_fundamental_course(token):
    url = "https://qwallity-prod.onrender.com/courses/fundamental/api"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()
