# stdlib imports
from datetime import datetime
from typing import Optional

# third-party imports
from github import Github
from github.PullRequest import PullRequest
from pydantic.dataclasses import dataclass
from pydantic import BaseModel

# local imports
from gots import git_of_thoughts
from gots.typing import RepoAgent, WriteRepoInp, WriteRepoOut
from .setup_repo import setup_repo, SetupRepoInp
from .write_github import create_pull_request


SETUP_ORDERS_BASE_DIR = "orders/"


class GothubPullRequest(BaseModel):
    pr: PullRequest

    class Config:
        arbitrary_types_allowed = True


@dataclass
class GithubOrderInp:
    username: str
    https_url: str
    github_token: str
    openai_api_key: str
    branch_name: Optional[str]
    extra_prompt: Optional[str]
    repo_agent: Optional[RepoAgent]


@dataclass
class GithubOrderOut:
    order_id: str
    pull_requests: list[GothubPullRequest]


def take_order(inp: GithubOrderInp) -> GithubOrderOut:
    match inp:
        case GithubOrderInp(
            username=username,
            https_url=https_url,
            github_token=github_token,
            openai_api_key=openai_api_key,
            branch_name=branch_name,
            extra_prompt=extra_prompt,
            repo_agent=repo_agent,
        ):
            pass

    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    setup_dir = SETUP_ORDERS_BASE_DIR + username + "/" + time

    setup_repo_inp = SetupRepoInp(
        setup_dir=setup_dir,
        https_url=https_url,
        github_token=github_token,
        branch_name=branch_name,
    )

    with setup_repo(setup_repo_inp) as repo:
        write_repo_out = repo_agent(
            WriteRepoInp(
                repo=repo,
                openai_api_key=openai_api_key,
                extra_prompt=extra_prompt,
            )
        )
        new_branches = write_repo_out.new_branches

    # TODO abstract this away
    github = Github(github_token)
    github_repo = github.get_repo(https_url)

    new_pull_requests = [
        create_pull_request(
            github_repo,
            branch,
        )
        for branch in new_branches
    ]

    return GithubOrderOut(
        order_id=time,
        pull_requests=new_pull_requests,
    )
