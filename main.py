#!/usr/bin/env python3

import argparse
import requests
import json


def parse_args():
    parser = argparse.ArgumentParser(
        description="""
            Runs a list of test on a given url. Run this
            script with the help flag (-h or --help) to to see the
            list of flags
        """
    )
    parser.add_argument("url", help="URL on which the tests will be made.")
    return parser.parse_args()


def main():
    args = parse_args()
    print(args.url)


if __name__ == "__main__":
    main()
