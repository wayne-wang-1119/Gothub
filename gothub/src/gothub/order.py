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
    https_url: str
    github_token: str
    openai_api_key: str
    branch_name: Optional[str]
    extra_prompt: Optional[str]


@dataclass
class GithubOrderOut:
    pull_requests: list[PullRequest]


def take_order(inp: GithubOrderInp) -> GithubOrderOut:
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    dir = SETUP_ORDERS_BASE_DIR + ... + time

    inp = SetupRepoControllerInp(
        setup_dir=dir,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        branch_name=OTHER_BRANCH,
    )

    with setup_repo(inp) as repo:
        pass
