from typing import Optional

from git import Head
from github.PullRequest import PullRequest
from github.Repository import Repository
from pydantic import BaseModel


class GothubPullRequest(BaseModel):
    pr: PullRequest

    class Config:
        arbitrary_types_allowed = True


def create_pull_request(
    github_repo: Repository,
    branch: Head,
    title: Optional[str] = None,
    body: Optional[str] = None,
) -> GothubPullRequest:
    branch_name = branch.name
    base_branch = github_repo.default_branch

    title = title or f"PR for: {branch_name}"
    body = body or f"This is a pull request for changes in the branch: {branch_name}"

    pr = github_repo.create_pull(
        title=title,
        body=body,
        head=branch_name,  # name of the branch you want to merge
        base=base_branch,
    )

    return GothubPullRequest(
        pr=pr,
    )
