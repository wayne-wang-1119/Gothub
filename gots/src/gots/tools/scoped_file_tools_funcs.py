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

current_dir = os.getcwd()
# /Users/wayne/Desktop/Gothub


class MyCreateToolInput(BaseModel):
    """Input for FileTool."""

    file_path: str = Field(..., description="Path of the file, include file name")


class MyCreateFileTool(BaseFileToolMixin, BaseTool):
    name: str = "create_file_tool"
    args_schema: Type[BaseModel] = MyCreateToolInput  # Accepts a single string argument
    description: str = "Create a new file"
    FILE_PATH_STORE = (
        current_dir + "/db/file_helper.txt"
    )  # /Users/wayne/Desktop/Gothub/db/file_helper.txt

    def _run(self, file_path: str) -> str:
        append = False
        write_path = self.get_relative_path(file_path)  # root_dir + "/file_path"
        if os.path.exists(write_path):
            # if file exists, just add its path to the db path
            with open(self.FILE_PATH_STORE, "w") as f:
                f.write(str(write_path))
            return f"Writing existing file: {file_path}"
        # creating a new file, path doesn't exist
        try:
            mode = "a" if append else "w"
            with open(write_path, mode) as f:
                f.write("created successfully")
            with open(self.FILE_PATH_STORE, "w") as f:
                f.write(str(write_path))
            return f"created {file_path}."
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
    FILE_PATH_STORE = (
        current_dir + "/db/file_helper.txt"
    )  # /Users/wayne/Desktop/Gothub/db/file_helper.txt

    def _run(self, text: str) -> str:
        if not os.path.exists(self.FILE_PATH_STORE):
            return "Error: No file has been created yet. Return to create a file."

        with open(self.FILE_PATH_STORE, "r") as f:
            file_path = f.read()

        try:
            write_path = file_path
            with open(write_path, "w") as file:
                file.write(text)

            with open(self.FILE_PATH_STORE, "w") as f:
                f.write("")
            return f"Written {file_path}."

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
