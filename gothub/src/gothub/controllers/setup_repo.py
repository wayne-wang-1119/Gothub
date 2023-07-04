from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class SetupRepoControllerInp:
    setup_dir: str
    https_url: str
    github_token: str
    branch_name: Optional[str]
