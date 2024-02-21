
# GitHubRepoDownloader

A simple Python script to download all public repositories from a specified GitHub user. This tool uses the GitHub API to fetch repository details and then clones them into a local directory.

## Features

- Downloads all public repositories of a specified GitHub user.
- Optionally uses a GitHub API token to avoid rate limits.
- Organizes cloned repositories into a specified directory.

## Prerequisites

Before you use `GitHubRepoDownloader`, ensure you have the following:

- Python 3.x installed on your system.
- `git` installed and accessible from your command line or terminal.
- `requests` library installed in Python. You can install it using `pip install requests`.

## Usage

1. Clone this repository or download `github_repo_downloader.py` to your local machine.
2. Open `github_repo_downloader.py` in a text editor.
3. Replace `'username'` in the `GITHUB_USER` variable with the GitHub username of the user whose repositories you want to download.
4. If you have a GitHub API token and want to use it (recommended to avoid hitting rate limits), replace `None` in the `GITHUB_TOKEN` variable with your token as a string.
5. Run the script:

```bash
python github_repo_downloader.py
```

The script will create a directory named `github_repos` in the current working directory and clone all the public repositories of the specified user into this directory.

## Customization

You can modify the script to change the target directory for cloned repositories by editing the `TARGET_DIR` variable.

## Disclaimer

This tool is intended for educational and backup purposes. Please ensure you have the right to clone and store the repositories you download, especially if they are private or contain sensitive information.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
