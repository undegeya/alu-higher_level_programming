#!/usr/bin/python3
"""Sends a POST request with an email parameter."""

from urllib import request, parse
import sys

if __name__ == "__main__":
    values = parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    with request.urlopen(sys.argv[1], values) as response:
        print(response.read().decode("utf-8"))
