#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the variable
X-Request-Id in the response header"""
import sys
import requests

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
