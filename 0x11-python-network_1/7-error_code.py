#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and display response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code:", response.status_code)
