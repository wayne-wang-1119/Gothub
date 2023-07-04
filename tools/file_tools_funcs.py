from langchain.tools.file_management import ListDirectoryTool
from pathlib import Path


class RecursiveDirectoryTool(ListDirectoryTool):
    name = "read_recursive_directory"
    description = "Lists all files in a directory and its subdirectories recursively"

    def run(self, args):
        dir_path = Path(args["directory"])

        files = list(dir_path.rglob("*"))

        return [str(file) for file in files]
