import requests


def send_request(url, data):
    try:
        response = requests.post(url, json=data)
        return response
    except requests.exceptions.RequestException as e:
        return e
