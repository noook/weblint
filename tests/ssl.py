import requests


def check_ssl(url, param):
    response = requests.get(url)
    return ""  # response.headers
