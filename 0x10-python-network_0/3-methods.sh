#!/bin/bash
# takes url displays HTTP methods
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'