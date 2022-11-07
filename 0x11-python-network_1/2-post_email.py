#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2].encode('utf-8')
req = urllib.request.Request(url, email)
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))
