#!/usr/bin/python3
"""
Python script that takes github account
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)

    response = requests.get("https://api.github.com/user", auth=basic)

    if response.status_code == 200:
        user_id = response.json().get("id")

        print(user_id)
    else:
        print(None)
