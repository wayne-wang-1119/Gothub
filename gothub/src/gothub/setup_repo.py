import os
import re
from pathlib import Path
from typing import Optional

from git import Repo
from github import Github
from pydantic.dataclasses import dataclass

# TODO This is not elegant
SETUP_BASE_DIR = Path(__file__).absolute().parent.parent.parent.parent / "repos/"


@dataclass
class SetupRepoInp:
    setup_dir: str
    https_url: str
    github_token: str
    branch_name: Optional[str] = None


def mkdir_if_available_else_error(path: Path):
    if path.exists():
        raise FileExistsError(f"Path {path} already exists.")
    else:
        # TODO Maybe use mkdir() instead?
        os.makedirs(path)


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

    # Insert github_token into https_url
    # TODO This is not elegant
    pattern = r"https://"
    https_url = re.sub(pattern, f"https://oauth2:{github_token}@", https_url)

    # Clone repo in dir
    repo = Repo.clone_from(https_url, dir)

    # Checkout branch
    if branch_name is not None:
        repo.git.checkout(branch_name)

    return repo


def setup_logs(inp: Path):
    file_path = SETUP_BASE_DIR / f"{inp}/log.txt"

    if not file_path.exists():
        with open(file_path, "w") as f:
            pass
    else:
        print(f"File {file_path} already exists!")
