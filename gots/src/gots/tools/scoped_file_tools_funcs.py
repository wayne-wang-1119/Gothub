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


class MyCreateToolInput(BaseModel):
    """Input for FileTool."""

    file_path: str = Field(..., description="Path of the file, include file name")


class MyCreateFileTool(BaseFileToolMixin, BaseTool):
    name: str = "create_file_tool"
    args_schema: Type[BaseModel] = MyCreateToolInput  # Accepts a single string argument
    description: str = "Create a new file"
    FILE_PATH_STORE = "./file_path_store.txt"

    def _run(
        self,
        file_path: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        append = False
        write_path = self.get_relative_path(file_path) / file_path
        try:
            write_path.parent.mkdir(exist_ok=True, parents=True)
            mode = "a" if append else "w"
            with write_path.open(mode, encoding="utf-8") as f:
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


class MyFillToolInput(BaseModel):
    """Input for FileTool."""

    text: str = Field(..., description="content to write to file")


class MyFillFileTool(BaseFileToolMixin, BaseTool):
    name: str = "write_file_tool"
    args_schema: Type[BaseModel] = MyFillToolInput
    description: str = "Write to a file"
    FILE_PATH_STORE = "./file_path_store.txt"

    def _run(
        self, text: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        if not os.path.exists(self.FILE_PATH_STORE):
            return "Error: No file has been created yet."

        with open(self.FILE_PATH_STORE, "r") as f:
            file_path = f.read()

        try:
            write_path = file_path
            with open(write_path, "w") as file:
                file.write(text)

            with open(self.FILE_PATH_STORE, "w") as f:
                f.write("")
            return f"File content written successfully to {file_path}."

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
