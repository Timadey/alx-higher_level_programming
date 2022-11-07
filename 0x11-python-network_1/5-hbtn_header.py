#!/usr/bin/python3
"""Displays the value of the variable
X-Request-Id in the response header"""

import requests
import sys

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))

