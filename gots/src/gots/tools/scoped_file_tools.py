from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents import Tool


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

    write_file_tool = Tool(
        name="write_file",
        func=WriteFileTool(
            root_dir=root_dir,
        ).run,
        description="""
Useful when you want to write files.
You should run this to write the file where you need to.
""",
    )

    return [
        read_one_file_tool,
        read_directory_tree_tool,
        write_file_tool,
    ]
