import os
from pathlib import Path

import pytest

from . import (
    MyFillFileTool,
    MyFillToolInput,
)


def test_my_fill_file_tool():
    tool = MyFillFileTool()
    text = "Test content"
    input_model = MyFillToolInput(text=text)
    # convert the input model to a dictionary
    input_dict = input_model.dict()
    output = tool.run(input_dict)
    assert output == "File content written successfully to ./file_path_store.txt."


def test_my_fill_file_tool_no_file_created():
    tool = MyFillFileTool()
    text = "Test content"
    input_model = MyFillToolInput(text=text)
    # convert the input model to a dictionary
    input_dict = input_model.dict()
    # delete the file if exists
    if os.path.exists(tool.FILE_PATH_STORE):
        os.remove(tool.FILE_PATH_STORE)
    output = tool.run(input_dict)
    assert output == "Error: No file has been created yet."


def test_my_fill_file_tool_error():
    tool = MyFillFileTool()
    text = "Test content"
    input_model = MyFillToolInput(text=text)
    # convert the input model to a dictionary
    input_dict = input_model.dict()
    # make the file read only
    if os.path.exists(tool.FILE_PATH_STORE):
        os.chmod(tool.FILE_PATH_STORE, 0o444)
    output = tool.run(input_dict)
    assert output.startswith("Error: ")
