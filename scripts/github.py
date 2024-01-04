import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GIT_TOKEN')
username = 'Ruy-GC'
repos_url = f'https://api.github.com/users/{username}/repos'
headers = {'Authorization': f'token {token}'}

try:
    response = requests.get(url=repos_url, headers=headers)

    response.raise_for_status()
    repositories = response.json()

    for repo in repositories:
        print(repo['name'])

except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
