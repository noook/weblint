import requests, logging, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s %(message)s"
coloredlogs.install(logger=logger)


def cors_checker(url, param=None):
    response = requests.get(url)
    if response.headers.get("Access-Control-Allow-Origin") == None:
        logger.error(f"[{url}] Cors is not enabled")
    else:
        if response.headers.get("Access-Control-Allow-Origin") != "*":
            logger.error(f"[{url}] Cors is not compatible")

