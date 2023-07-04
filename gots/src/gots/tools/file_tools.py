from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents import Tool


read_one_file_tool = Tool(
    name="read_one_file",
    func=ReadFileTool().run,
    description="""
        Useful when you want to get the contents inside a file in a specified file path. 
        You should enter the file path recognized by the file. If you can not find the file,
        """,
)

read_directory_tree_tool = Tool(
    name="read_directory_tree",
    func=ListDirectoryTool().run,
    description="""
        Useful when you need to know what files are contained in this project.
        You should run this to record the file directory tree when you need to.
        """,
)

write_file_tool = Tool(
    name="write_file",
    func=WriteFileTool().run,
    description="""
        Useful when you want to write files.
        You should run this to write the file where you need to.
        """,
)
