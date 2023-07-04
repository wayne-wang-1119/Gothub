# stdlib imports
import os
from pathlib import Path
from typing import Optional

# third-party imports
from pydantic.dataclasses import dataclass


@dataclass
class SetupRepoControllerInp:
    setup_dir: Path
    https_url: str
    github_token: str
    branch_name: Optional[str]


def setup_repo(inp: SetupRepoControllerInp):
    # Make dir in setup_dir
    os.mkdir(inp.setup_dir)

    # Clone repo in dir
    # Checkout branch
