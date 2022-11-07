#!/usr/bin/python3
"""Search a user"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    response = requests.post(url, data)
    if response.status_code == 200:
        try:
            res = response.json()
            print(f"[{res.get('id')}] {res.get('name')}")
        except requests.exceptions.JSONDecodeError:
            print('Invalid Json')
    elif response.status_code == 204:
        print('No Content')
