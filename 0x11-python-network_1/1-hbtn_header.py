# 1/usr/bin/python3
"""
Script tthat takes URL and sends value
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        content = response.read()
        request_id = response.headers.get("X-Request-Id", None)

        print(request_id)
