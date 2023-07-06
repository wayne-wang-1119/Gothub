import os
from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
)
from langchain.tools.base import BaseTool
from langchain.tools.file_management.utils import (
    BaseFileToolMixin,
)
from pydantic import BaseModel, Field


class MyCreateToolInput(BaseModel):
    """Input for FileTool."""

    file_path: str = Field(..., description="Path of the file, include file name")


class MyCreateFileTool(BaseFileToolMixin, BaseTool):
    name: str = "create_file_tool"
    args_schema: Type[BaseModel] = MyCreateToolInput  # Accepts a single string argument
    description: str = "Create a new file"

    def _run(self, file_path: str) -> str:
        append = False
        write_path = self.get_relative_path(file_path)  # root_dir + "/file_path"
        try:
            mode = "a" if append else "w"
            with open(write_path, mode) as f:
                f.write("created successfully")

            # TODO This is hacky

            return f"File created successfully to {file_path}."
        except Exception as e:
            return "Error: " + str(e)

    async def _arun(self) -> str:
        # TODO: Add aiofiles method
        raise NotImplementedError


class MyFillToolInput(BaseModel):
    """Input for FileTool."""

    content: str = Field(..., description="content to write to file")


class MyFillFileTool(BaseFileToolMixin, BaseTool):
    name: str = "write_file_tool"
    args_schema: Type[BaseModel] = MyFillToolInput
    description: str = "Write to a file"

    def _run(self, content: str) -> str:
        file_path = ""
        try:
            write_path = file_path
            with open(write_path, "w") as file:
                file.write(content)
            return f"File content written successfully to {file_path}."
        except Exception as e:
            return "Error: " + str(e)

    async def _arun(self) -> str:
        # TODO: Add aiofiles method
        raise NotImplementedError
