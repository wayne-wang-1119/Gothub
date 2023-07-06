from typing import Any, Dict, List, Union

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import tracing_enabled
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction

from .utils.git_methods import git_methods


# First, define custom callback handler implementations
class MyCustomHandlerOne(BaseCallbackHandler):
    def __init__(self, git_methods_instance: git_methods):
        self.git = git_methods_instance

    def on_tool_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""

    def on_tool_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        self.git.commit_changes(outputs)
