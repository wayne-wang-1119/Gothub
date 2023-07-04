# stdlib imports
from typing import Optional

# third-party imports
from github.PullRequest import PullRequest
from pydantic.dataclasses import dataclass


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
    pass
