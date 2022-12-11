#!/usr/bin/python3
"""Takes in a url, sends a request to the url
    lnd displays the val of X-Request-Id"""
if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-ID")
        print(html)
