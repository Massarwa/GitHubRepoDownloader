
import requests
import subprocess
import os

# GitHub username of the target user
GITHUB_USER = 'username'  # Replace 'username' with the GitHub username
# Optional: GitHub API token for higher rate limit, replace None with your token as a string
GITHUB_TOKEN = None
# Directory to clone the repositories into
TARGET_DIR = './github_repos'
# Base URL of GitHub API
API_URL = f'https://api.github.com/users/{GITHUB_USER}/repos'

def get_repos(url, headers):
    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos if isinstance(repos, list) else []

def clone_repo(git_url, target_dir):
    cmd = ['git', 'clone', git_url, target_dir]
    subprocess.run(cmd)

def main():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    repos = get_repos(API_URL, headers)

    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    for repo in repos:
        repo_name = repo['name']
        git_url = repo['clone_url']
        repo_dir = os.path.join(TARGET_DIR, repo_name)
        print(f'Cloning {repo_name}...')
        clone_repo(git_url, repo_dir)

if __name__ == '__main__':
    main()
