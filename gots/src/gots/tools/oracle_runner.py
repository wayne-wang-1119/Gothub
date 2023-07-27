import subprocess
from pathlib import Path

from langchain.tools import BaseTool, StructuredTool


def oracle_runner_factory(root_path: str):
    def run_oracle(oracle_id: str) -> str:
        """
        Run the oracle with the given id.

        :param oracle_id: id of the oracle to run
        :return: result of the oracle
        """

        cmd = "&& ".join(
            [
                f"cd {root_path}",
                "ls -al",
                # "source ~/.bashrc",
                "echo $USER",
                "echo $PATH",
                "echo $SHELL",
                "python -c \"print('hello world!')\"",
            ]
        )

        result = subprocess.run(
            cmd,
            shell=True,
            executable="/bin/bash",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Print the return code (0 is success)
        print("Return code:", result.returncode)

        # Print the output of the command
        print("Output:", result.stdout)

        # Print the stderr if any error happened
        print("Error:", result.stderr if result.stderr else None)

        return str(630)

    oracle_runner = StructuredTool.from_function(run_oracle)

    return oracle_runner
