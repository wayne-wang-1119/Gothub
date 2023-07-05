from typing import Callable, Optional

from git import Head, Repo
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class WriteRepoInp(BaseModel):
    repo: Repo
    openai_api_key: str
    extra_prompt: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class WriteRepoOut(BaseModel):
    new_branches: list[Head]

    class Config:
        arbitrary_types_allowed = True


RepoAgent = Callable[[WriteRepoInp], WriteRepoOut]
