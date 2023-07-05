from typing import Dict, Union, Any, List

from langchain.callbacks.base import BaseCallbackHandler


# First, define custom callback handler implementations
class GitCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        pass

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        inputs: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        """Run when chain starts running."""

    def on_tool_end(
        self,
        outputs: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        """Run when chain ends running."""
