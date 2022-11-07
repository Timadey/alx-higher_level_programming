#!/usr/bin/python3
"""Display X-Request-Id variable found in the header of the response."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = str(response.headers)
        x = headers.find("X-Request-Id")
        if x != -1:
            print (headers[x+14: x+14+37])
