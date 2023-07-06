from langchain.agents import Tool
from langchain.tools.file_management import (
    CopyFileTool,
    DeleteFileTool,
    ListDirectoryTool,
    MoveFileTool,
    ReadFileTool,
)

from .scoped_file_tools_funcs import (
    MyCreateFileTool,
    MyFillFileTool,
)


def build_scoped_file_tools(root_dir: str) -> list[Tool]:
    read_one_file_tool = Tool(
        name="read_one_file",
        func=ReadFileTool(
            root_dir=root_dir,
        ).run,
        description="""
Useful when you want to get the contents inside a file in a specified file path.
You should enter the file path recognized by the file. If you can not find the file,
""",
    )

    read_directory_tree_tool = Tool(
        name="read_directory_tree",
        func=ListDirectoryTool(
            root_dir=root_dir,
        ).run,
        description="""
Useful when you need to know what files are contained in this project.
You should run this to record the file directory tree when you need to.
""",
    )

    create_file_tool = Tool(
        name="create_file",
        func=MyCreateFileTool(
            root_dir=root_dir,
        ).run,
        description="""
Useful when you want to create files.
You should run this to create the file right before writing to the file.
A use of the "write_file" tool should immediately follow this tool.
""",
    )

    fill_file_tool = Tool(
        name="write_file",
        func=MyFillFileTool(
            root_dir=root_dir,
        ).run,
        description="""
Useful when you want to fill in the contents in a file.
This tool should immediately follow a use of the "create_file" tool.
You should run this to write in a file, the file must be created first.

The tool takes the file path and the text content as two strings separated by a /
An example of this input: example.py/print("Hello World.")\nprint("Hello World again!")
Follow this example strictly.
""",
    )

    return [
        read_one_file_tool,
        read_directory_tree_tool,
        create_file_tool,
        fill_file_tool,
    ]
