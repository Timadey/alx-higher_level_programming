#!/usr/bin/python3
"""Display my Github ID
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # headers = {'Accept': 'application/vnd.github+json',
    #            'Authorization': f'Bearer {token}'}
    response = requests.get('https://api.github.com/user',
                            auth=requests.auth.HTTPBasicAuth(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print('None')
