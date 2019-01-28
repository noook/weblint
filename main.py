#!/usr/bin/env python3

from tests.html import check_img_alt, check_duplicate_id, check_404
from tests.cors import cors_checker
import argparse
import inspect

from tests.response_time import response_time


def parse_args():
    parser = argparse.ArgumentParser(
        description="""
            Runs a list of test on a given url.
            Choose specific tests with the following flags
        """
    )
    tests = parser.add_argument_group("tests", "List of tests that will be realized")

    parser.add_argument("urls", nargs="+",
                        help="URLs on which the tests will be made.")

    tests.add_argument(
        "--response-time",
        nargs="?",
        const=True,
        dest="response_time",
        help="Checks response time for the given URLs",
    )

    tests.add_argument(
        "--img-alt",
        nargs="?",
        const=True,
        dest="check_img_alt",
        help="Checks if all images have the `alt` attribute",
    )

    tests.add_argument(
        "--check-404",
        nargs="?",
        const=True,
        dest="check_404",
        help="Checking if the links are working",
    )

    tests.add_argument(
        "--cors-check",
        nargs="?",
        const=True,
        dest="cors_checker",
        help="Checks if the site is cors compatible",
    )

    tests.add_argument(
        "--duplicate-ids",
        nargs="?",
        const=True,
        dest="check_duplicate_id",
        help="Checks the unicity of all html elements' ids",
    )

    # tests.add_argument(
    #     "--test-name", # Flag name
    #     nargs="?", # Allows passing a value (--arg="value")
    #     const=True, # Just store True if no argument
    #     dest="function_to_call", # Function associated to the test
    #     help="This is the description of the test", # Test description
    # )

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
default_tests = {
    "check_img_alt": check_img_alt,
    "response_time": response_time,
    "check_404": check_404,
    "cors_checker": cors_checker,
    "check_duplicate_id": check_duplicate_id,
}


def defaults(urls):
    for url in urls:
        for (name, test) in default_tests.items():
            test(url)


def main():
    urls, tests, params = parse_args()
    if len(tests.items()) == 0:
        defaults(urls)
    else:
        for url in urls:
            for (name, test) in tests.items():
                test(url, params[name])


if __name__ == "__main__":
    main()
