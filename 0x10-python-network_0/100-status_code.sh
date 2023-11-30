#!/bin/bash
# sends request
curl -so /dev/null --write-out "%{http_code}" "$1"
