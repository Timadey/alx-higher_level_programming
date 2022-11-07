#!/usr/bin/python3
"""Search a user"""

import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) >= 2:
    q = sys.argv[1]
else:
    q = ""
response = requests.post(url, q)
if response.status_code == 200:
    try:
        res = response.json()
        print(f"[{res.get('id')}] {res.get('name')}")
    except requests.exceptions.JSONDecodeError:
        print('Invalid Json')
elif response.status_code == 204:
    print('No Content')
