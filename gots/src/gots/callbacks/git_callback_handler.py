import sys
from typing import Any, Dict, List, Union

from git import Repo
from langchain.callbacks.base import BaseCallbackHandler


# First, define custom callback handler implementations
class GitCallbackHandler(BaseCallbackHandler):
    """
    FIXME Tool callbacks seem to have bugs.
    """

    def __init__(self, repo: Repo):
        self.repo = repo
        logfile = repo.working_dir + "/log.txt"
        self.logfilepath = logfile
        with open(self.logfilepath, "a") as f:  # Open the file in append mode
            f.write("init\n")

    def write_to_log(self, message: str):
        with open(self.logfilepath, "a") as f:
            f.write(message)

    def on_tool_start(self, *args, **kwargs: Any) -> Any:
        """Run when tool starts running."""

    def on_llm_start(self, *args, **kwargs: Any) -> Any:
        self.write_to_log("on_llm_start\n" + str(args) + "\n" + str(kwargs) + "\n")
        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.git.commit("-m", "on llm start", "--allow-empty")

    def on_llm_end(self, *args, **kwargs: Any) -> Any:
        self.write_to_log("on_llm_end\n" + str(args) + "\n" + str(kwargs) + "\n")
        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.git.commit("-m", "on llm end", "--allow-empty")

    def on_chain_end(self, *args, **kwargs: Any) -> Any:
        """Run when chain ends running."""
        self.write_to_log("on_chain_end\n" + str(args) + "\n" + str(kwargs) + "\n")
        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.git.commit("-m", "on chain end", "--allow-empty")

    def on_agent_finish(self, *args, **kwargs: Any) -> Any:
        """Run on agent end."""
        self.write_to_log("on_agent_finish\n" + str(args) + "\n" + str(kwargs) + "\n")
        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.git.commit("-m", "on agent finish", "--allow-empty")
