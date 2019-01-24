from time import process_time
import requests, math


def response_time(url, param=None):
    begin = process_time()
    requests.get(url)
    end = process_time()

    difference = (end - begin) / (1 * math.pow(10, -3))  #  Convert ns to ms
    return f"[{url}] Response time : {difference} ms"

