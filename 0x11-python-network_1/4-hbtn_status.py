#!/usr/bin/python3
'''fetches status of https://alx-intranet.hbtn.io/status'''
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
