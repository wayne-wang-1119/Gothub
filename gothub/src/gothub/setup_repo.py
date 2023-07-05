import os
from pathlib import Path
from typing import Optional

from git import Repo
from github import Github
from pydantic.dataclasses import dataclass

SETUP_BASE_DIR = Path("./repos")


@dataclass
class SetupRepoInp:
    setup_dir: str
    https_url: str
    github_token: str
    branch_name: Optional[str]


def mkdir_if_available_else_error(path: Path):
    if path.exists():
        raise FileExistsError(f"Path {path} already exists.")
    else:
        path.mkdir()


def setup_repo(inp: SetupRepoInp) -> Repo:
    match inp:
        case SetupRepoInp(
            setup_dir=setup_dir,
            https_url=https_url,
            github_token=github_token,
            branch_name=branch_name,
        ):
            pass

    dir = SETUP_BASE_DIR / setup_dir

    # Make dir in setup_dir
    mkdir_if_available_else_error(dir)

    # Clone repo in dir
    # TODO: How to use github_token?
    repo = Repo.clone_from(https_url, dir)

    # Checkout branch
    if branch_name is not None:
        repo.git.checkout(branch_name)

    return repo
