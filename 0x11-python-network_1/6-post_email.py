#!/usr/bin/python3
"""Sends a post request to a url"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, email)
    print(response.text)

