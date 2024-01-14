import requests
import os
import json

from dotenv import load_dotenv

os.environ.clear()

load_dotenv()

github_token = os.getenv("GIT_TOKEN")
username = 'Ruy-GC'

url = f'https://api.github.com/users/{username}/repos'
repos_list = []

if github_token:
    headers = {'Authorization': f'token {github_token}'}

    try:
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        account_details = response.json()
        repos_details = response.json()
        
        with open(f'repos_details_{username}.txt', 'w', encoding='utf-8') as file:
            json.dump(account_details, file, ensure_ascii=False, indent=4)

        print(f"Repositories details saved to 'repos_details_{username}.txt'")
        
        for repo in repos_details:
            name = repo['name']
            repos_list.append(name)

        with open(f'repos_names_{username}.txt', 'w', encoding='utf-8') as file:
            json.dump(repos_list, file, ensure_ascii=False, indent=4)

        print(f"Repositories names saved to 'repos_names_{username}.txt'")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch user details. Error: {e}")
else:
    print("GitHub token not found. Make sure the environment variable GIT_TOKEN is set.")
