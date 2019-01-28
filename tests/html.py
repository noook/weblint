from bs4 import BeautifulSoup
import requests
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s %(message)s"
coloredlogs.install(logger=logger)


def check_img_alt(url, param=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for img in soup.find_all("img"):
        if not img.has_attr("alt"):
            logger.error(f'[{url}] Missing "alt" attribute in {img}')
        elif len(img["alt"]) is 0:
            logger.error(f'[{url}] "alt" cannot be empty {img}')


def check_if_link_working(url, param=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        if link.get("href") != "/":
            response = requests.get(url + link.get("href"))
            data = response.status_code
            if data == 404:
                logger.error(
                    f'[{link.get("href")}] Link is redirecting to a 404 error code')
