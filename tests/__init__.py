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
