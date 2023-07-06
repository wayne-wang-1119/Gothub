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

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running."""
        print("I'm Here!!!!!!")

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[Any]],
        **kwargs: Any,
    ) -> Any:
        """Run when Chat Model starts running."""
        print("I'm Here!!!!!!")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        """Run on new LLM token. Only available when streaming is enabled."""
        print("I'm Here!!!!!!")

    def on_llm_end(self, response, **kwargs: Any) -> Any:
        """Run when LLM ends running."""
        print("I'm Here!!!!!!")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""
        print("I'm Here!!!!!!")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""
        print("I'm Here!!!!!!")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        print("I'm Here!!!!!!")

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when chain errors."""
        print("I'm Here!!!!!!")

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when tool errors."""
        print("I'm Here!!!!!!")

    def on_text(self, text: str, **kwargs: Any) -> Any:
        """Run on arbitrary text."""
        print("I'm Here!!!!!!")

    def on_agent_action(self, action, **kwargs: Any) -> Any:
        """Run on agent action."""
        print("I'm Here!!!!!!")

    def on_agent_finish(self, finish, **kwargs: Any) -> Any:
        """Run on agent end."""
        print("I'm Here!!!!!!")
