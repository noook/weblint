#!/usr/bin/env python3

import argparse, coloredlogs, logging, inspect

from tests.response_time import response_time
from tests.ssl import check_ssl

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s %(message)s"
coloredlogs.install(logger=logger)


def parse_args():
    parser = argparse.ArgumentParser(
        description="""
            Runs a list of test on a given url.
            Choose specific tests with the following flags
        """
    )
    tests = parser.add_argument_group("tests", "List of tests that will be realized")
    parser.add_argument("urls", nargs="+", help="URLs on which the tests will be made.")

    tests.add_argument(
        "--response-time",
        nargs="?",
        const=True,
        dest="response_time",
        help="Checks response time for the given URLs",
    )

    args = parser.parse_args()
    tests = {
        key: getattr(inspect.getmodule(main), key)
        for (key, value) in vars(args).items()
        if key is not "urls"
        and key in dir(inspect.getmodule(main))
        and value is not None
    }

    params = {}

    for (test, param) in tests.items():
        params[test] = vars(args)[test]

    return args.urls, tests, params


# Register tests here - Arguments "dest" must be the the same as the function name
default_tests = {"response_time": response_time, "check_ssl": check_ssl}


def defaults(urls):
    for url in urls:
        for (name, test) in default_tests.items():
            logger.info(test(url))


def main():
    urls, tests, params = parse_args()
    if len(tests.items()) == 0:
        defaults(urls)
    else:
        for url in urls:
            for (name, test) in tests.items():
                logger.info(test(url, params[name]))


if __name__ == "__main__":
    main()
