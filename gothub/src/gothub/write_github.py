from typing import Optional

from pydantic import BaseModel
from github.Repository import Repository
from github.PullRequest import PullRequest
from git import Head


class GothubPullRequest(BaseModel):
    pr: PullRequest

    class Config:
        arbitrary_types_allowed = True


def create_pull_request(github_repo: Repository, branch: Head) -> GothubPullRequest:
    branch_name = branch.name
    base_branch = github_repo.default_branch

    pr = github_repo.create_pull(
        title=f"PR for: {branch_name}",
        body=f"This is a pull request for changes in the branch: {branch_name}",
        head=branch_name,  # name of the branch you want to merge
        base=base_branch,
    )

    return GothubPullRequest(
        pr=pr,
    )
