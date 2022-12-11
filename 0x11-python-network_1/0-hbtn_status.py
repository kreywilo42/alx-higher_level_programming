#!/usr/bin/python3
"""A python script that fetches alx intranet status"""
import urllib.request

url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content:".format(html.decode("utf-8", "replace")))
