#!/bin/bash
# takes URL sends rrequest 
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2