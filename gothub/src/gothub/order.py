from typing import Optional
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
    pull_requests: list[str]


def take_order(inp: GithubOrderInp) -> GithubOrderOut:
    pass
