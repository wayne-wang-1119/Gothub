from datetime import datetime
from typing import Callable, Optional

import langchain
from git import Head, Repo
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


# keep this true if you want to see the outputs
langchain.debug = True


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


def gots_repo_agent(inp: WriteRepoInp) -> WriteRepoOut:
    """
    ! Should only modify what's permitted by inp
    """
    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")
    original_branch = repo.active_branch

    # TODO Create more than one branch
    new_branch_name = "gothub_gots" + time
    new_branch = repo.create_head(new_branch_name)
    new_branch.checkout()

    # FIXME Replace this with the actual code
    repo.git.commit("--allow-empty", "-m", "empty commit")

    original_branch.checkout()

    return WriteRepoOut(
        new_branches=[new_branch],
    )
