# stdlib imports
import os
from pathlib import Path
from typing import Optional

# third-party imports
from pydantic.dataclasses import dataclass


SETUP_BASE_DIR = Path("./repos")


@dataclass
class SetupRepoControllerInp:
    setup_dir: str
    https_url: str
    github_token: str
    branch_name: Optional[str]


def mkdir_if_available_else_error(path: Path):
    if path.exists():
        raise FileExistsError(f"Path {path} already exists.")
    else:
        path.mkdir()


def setup_repo(inp: SetupRepoControllerInp):
    # Make dir in setup_dir
    mkdir_if_available_else_error(SETUP_BASE_DIR / inp.setup_dir)

    # Clone repo in dir
    # Checkout branch
