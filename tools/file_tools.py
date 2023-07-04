from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents import Tool

from .file_tools_funcs import RecursiveDirectoryTool


read_one_file_tool = Tool(
    name="read_one_file",
    func=ReadFileTool().run,
    description="""
        Useful when you want to get the contents inside a file in a specified file path. 
        You should enter the file path recognized by the file. If you can not find the file,
        you should probably look deeper under the few existing directories.
        """,
)

read_directory_tree_tool = Tool(
    name="read_directory_tree",
    func=ListDirectoryTool().run,
    description="""
        Useful when you need to know what files are contained in this project.
        You should run this to record the file directory tree when you need to.
        If you are having trouble locating some files, you should go into each directory.
        """,
)

write_file_tool = Tool(
    name="write_file",
    func=WriteFileTool().run,
    description="""
        Useful when you want to write files.
        You should run this to write the file where you need to.
        If you are having trouble locating some files, you should go into each directory.
        """,
)

recursive_directory_tool = Tool(
    name="read_recursive_directory",
    func=RecursiveDirectoryTool().run,
    description="""
        Useful when you need to know what files are contained in this project and its subdirectories.
        You should run this to record the entire file directory tree when you need to.
        """,
)
