# stdlib imports
from datetime import datetime
from typing import Optional

# third-party imports
from github.PullRequest import PullRequest
from pydantic.dataclasses import dataclass

# local imports
from .setup_repo import setup_repo, SetupRepoControllerInp


SETUP_ORDERS_BASE_DIR = "orders/"


@dataclass
class GithubOrderInp:
    username: str
    https_url: str
    github_token: str
    openai_api_key: str
    branch_name: Optional[str]
    extra_prompt: Optional[str]


@dataclass
class GithubOrderOut:
    order_id: str
    pull_requests: list[PullRequest]


def take_order(inp: GithubOrderInp) -> GithubOrderOut:
    match inp:
        case GithubOrderInp(
            username=username,
            https_url=https_url,
            github_token=github_token,
            openai_api_key=openai_api_key,
            branch_name=branch_name,
            extra_prompt=extra_prompt,
        ):
            pass

    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    dir = SETUP_ORDERS_BASE_DIR + username + "/" + time

    setup_repo_inp = SetupRepoControllerInp(
        setup_dir=dir,
        https_url=https_url,
        github_token=github_token,
        branch_name=branch_name,
    )

    with setup_repo(setup_repo_inp) as repo:
        pass
