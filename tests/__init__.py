import os
from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools.base import BaseTool
from langchain.tools.file_management.utils import (
    INVALID_PATH_TEMPLATE,
    BaseFileToolMixin,
    FileValidationError,
)
from pydantic import BaseModel, Field

current_dir = os.getcwd()


class MyCreateToolInput(BaseModel):
    """Input for FileTool."""

    file_path: str = Field(..., description="Path of the file, include file name")


class MyCreateFileTool(BaseFileToolMixin, BaseTool):
    name: str = "create_file_tool"
    args_schema: Type[BaseModel] = MyCreateToolInput  # Accepts a single string argument
    description: str = "Create a new file"
    FILE_PATH_STORE = current_dir + "/db/file_helper.txt"

    def _run(
        self,
        file_path: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        append = False
        write_path = self.get_relative_path(file_path)
        try:
            mode = "a" if append else "w"
            with open(write_path, mode) as f:
                f.write("created successfully")
            with open(self.FILE_PATH_STORE, "w") as f:
                f.write(str(write_path))
            return f"File created successfully to {file_path}."
        except Exception as e:
            return "Error: " + str(e)

    async def _arun(
        self,
        text: str,
        append: bool = False,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        # TODO: Add aiofiles method
        raise NotImplementedError
