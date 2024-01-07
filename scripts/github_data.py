import requests
import os
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from dotenv import load_dotenv

os.environ.clear()
load_dotenv()

github_token = os.getenv("GIT_TOKEN")

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

username = 'Ruy-GC'

url = f'https://api.github.com/users/{username}'

if github_token:
    headers = {'Authorization': f'token {github_token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 

        account_details = response.json()
        
        with open(f'account_details_{username}.txt', 'w', encoding='utf-8') as file:
            json.dump(account_details, file, ensure_ascii=False, indent=4)
        print(f"Account details saved to 'account_details_{username}.txt'")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch user details. Error: {e}")
else:
    print("GitHub token not found. Make sure the environment variable GIT_TOKEN is set.")
