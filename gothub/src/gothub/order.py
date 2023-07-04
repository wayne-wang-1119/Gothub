from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class GithubPubOrderInp:
    https_url: str
    github_token: str
    openai_api_key: str
    branch_name: Optional[str]
    extra_prompt: Optional[str]


@dataclass
class GithubPubOrderOut:
    pull_requests: list[str]


def take_order(inp: GithubPubOrderInp) -> GithubPubOrderOut:
    pass
