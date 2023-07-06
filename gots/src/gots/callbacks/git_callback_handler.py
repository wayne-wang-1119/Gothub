import sys
from typing import Any, Dict, List, Union

from git import Repo
from langchain.callbacks.base import BaseCallbackHandler


# First, define custom callback handler implementations
class GitCallbackHandler(BaseCallbackHandler):
    def __init__(self, repo: Repo):
        self.repo = repo

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        **kwargs: Any,
    ) -> Any:
        """Run when tool starts running."""

    def on_tool_end(
        self,
        output: str,
        **kwargs: Any,
    ) -> Any:
        """Run when tool ends running."""

        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.git.commit("--allow-empty", "-m", output)
