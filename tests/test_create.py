import os
from pathlib import Path

import pytest

from . import (
    MyCreateFileTool,
    MyCreateToolInput,
)


def test_my_create_file_tool():
    tool = MyCreateFileTool()
    file_path = "tests/test_file.txt"
    input_model = MyCreateToolInput(file_path=file_path)
    # convert the input model to a dictionary
    input_dict = input_model.dict()
    output = tool.run(input_dict)
    assert output == f"File created successfully to {file_path}."
