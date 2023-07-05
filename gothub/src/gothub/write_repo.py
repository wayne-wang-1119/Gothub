# stdlib imports
import os
from pathlib import Path
from typing import Optional

# third-party imports
from pydantic.dataclasses import dataclass
from pydantic import BaseModel
from github import Github
from git import Repo, Head


class WriteRepoInp(BaseModel):
    repo: Repo
    openai_api_key: str
    extra_prompt: Optional[str]

    class Config:
        arbitrary_types_allowed = True


@dataclass
class WriteRepoOut:
    new_branches: list[Head]
