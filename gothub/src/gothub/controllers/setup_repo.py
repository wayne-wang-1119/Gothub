from pathlib import Path
from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class SetupRepoControllerInp:
    setup_dir: Path
    https_url: str
    github_token: str
    branch_name: Optional[str]
