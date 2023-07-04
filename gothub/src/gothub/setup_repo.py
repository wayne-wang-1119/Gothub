from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class SetupRepoInp:
    https_url: str
    github_token: str
    branch_name: Optional[str]


@dataclass
class SetupRepoOut:
    pull_requests: list[str]
