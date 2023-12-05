#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST
request
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    try:
        response = requests.post(url, data=data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
