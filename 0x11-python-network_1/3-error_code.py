#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response"""

import urllib.request
import urllib.error
import sys
url = sys.argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
