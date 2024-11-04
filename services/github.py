import requests
import base64

BASE_URL = "https://api.github.com"
# TOKEN = "YOUR_GITHUB_TOKEN"

def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    # Check if the user exists and has repositories
    if response.status_code == 200:
        repos = response.json()
        if repos:
            return repos
        else:
            return {"detail": "No repositories available for this user"}
    elif response.status_code == 404:
        return {"detail": "User not found"}
    else:
        return {"detail": "Error fetching repositories"}


def get_readme(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/readme"
    response = requests.get(url)

    if response.status_code == 200:
        readme_data = response.json()
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
        return readme_content
    elif response.status_code == 404:
        return {"detail": "README not found for this repository"}
    else:
        return {"detail": "Error fetching README"}

