#!/usr/bin/python3
"""Display my Github ID
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
"""

import requests
import sys

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

headers = {'Accept': 'application/vnd.github+json',
           'Authorization': f'Bearer {token}'}
response = requests.get('https://api.github.com/user', headers=headers)

if response.status_code == 200:
    print(response.json().get('id'))
else:
    print('None')
