import requests


def check_ssl(url, param=None):
    response = requests.get(url)
    return ""  # response.headers
