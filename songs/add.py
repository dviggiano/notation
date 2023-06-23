"""
A script for adding several songs at a time.
Depends on the API running, and this directory being populated with MP3 files.
"""

import os
import requests

URL = 'http://localhost:5000/add'
cwd = os.getcwd()

for filename in os.listdir(cwd):
    path = os.path.join(cwd, filename)

    if filename.endswith('.mp3'):
        with open(path, 'rb') as f:
            files = {'file': f}
            response = requests.post(URL, files=files)

        if response.status_code != 200:
            print(f'Failed to upload song (response status {response.status_code}).')
