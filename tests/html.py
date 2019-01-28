from bs4 import BeautifulSoup
import requests, logging, coloredlogs

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


def check_duplicate_id(url, param=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    ids = {}
    for tag in soup.find_all(True):
        if tag.has_attr("id"):
            if len(tag.attrs["id"]) is 0:
                logger.error(f'[{url}] "id" attribute cannot be empty {tag}')
            else:
                if tag.attrs["id"] in ids:
                    ids[tag.attrs["id"]] += 1
                else:
                    ids[tag.attrs["id"]] = 1
    for (id, occurr) in [(id, occurr) for (id, occurr) in ids.items() if occurr > 1]:
        logger.error(f"[{url}] Duplicate ID '{id}' on the page")
