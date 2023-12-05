#!/usr/bin/python3
"""
Python script that takes url, request to the url
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)

    except error.HTTPError as e:
        print("Error code:", e.code)
