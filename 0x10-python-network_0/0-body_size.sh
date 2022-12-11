#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size of the body of the response
curl -sI $1 | grep 'Content-Length' | cut -f2 -d ':'
