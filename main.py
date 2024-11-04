from fastapi import FastAPI, HTTPException
from services.github import get_repositories, get_readme

app = FastAPI()


@app.get("/repos/{username}") 
def list_repositories(username: str):
    repos = get_repositories(username)
    
    # Check for custom error messages
    if isinstance(repos, dict) and "detail" in repos:
        raise HTTPException(status_code=404, detail=repos["detail"])
    return repos

@app.get("/repos/{username}/{repo_name}/readme")
def readme(username: str, repo_name: str):
    content = get_readme(username, repo_name)
    if content:
        return {"content": content}
    raise HTTPException(status_code=404, detail="README not found for this repository")
