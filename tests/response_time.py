from time import process_time
import requests, logging, coloredlogs, math

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s %(message)s"
coloredlogs.install(logger=logger)


def response_time(url, param=None):
    begin = process_time()
    requests.get(url)
    end = process_time()

    difference = round((end - begin) / (1 * math.pow(10, -3)), 2)  #  Convert ns to ms
    logger.info(f"[{url}] Response time : {difference} ms")

