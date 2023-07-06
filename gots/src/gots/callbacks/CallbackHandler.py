from typing import Any, Dict, List, Union

from git import Head, Repo
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import tracing_enabled
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction


# First, define custom callback handler implementations
class MyCustomHandlerOne(BaseCallbackHandler):
    def __init__(self, repo: Repo):
        self.repo = repo

    def on_tool_start(
        self, serialized: Dict[str, Any], inputs: str, **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""
        self.repo.git.add(A=True)
        self.repo.index.commit("A")

    def on_tool_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        self.repo.git.add(A=True)
        self.repo.index.commit("A")
