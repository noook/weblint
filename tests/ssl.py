import requests


def check_ssl(url):
    response = requests.get(url)
    print(response)
