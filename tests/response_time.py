from time import process_time_ns
import requests, math


def response_time(url, param=None):
    begin = process_time_ns()
    requests.get(url)
    end = process_time_ns()

    difference = (end - begin) / (1 * math.pow(10, 6))  #  Convert ns to ms
    return f"[{url}] Response time : {difference} ms"

