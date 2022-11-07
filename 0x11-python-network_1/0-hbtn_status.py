#!/usr/bin/python3
"""A python progam that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print(f"    - type: {type(content)}\n\
        - content: {content}\n\
        - utf8 content: {content.decode('utf-8')}")
