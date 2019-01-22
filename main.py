#!/usr/bin/env python3

import argparse, coloredlogs, logging

from tests.response_time import response_time

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s %(message)s"
coloredlogs.install(logger=logger)


def parse_args():
    parser = argparse.ArgumentParser(
        description="""
            Runs a list of test on a given url. Run this
            script with the help flag (-h or --help) to to see the
            list of flags
        """
    )
    parser.add_argument("urls", nargs="+", help="URLs on which the tests will be made.")

    return parser.parse_args()


def main():
    args = parse_args()

    for url in args.urls:
        # Put tests functions here
        logger.info(response_time(url))


if __name__ == "__main__":
    main()
