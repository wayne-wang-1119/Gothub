import subprocess
from pathlib import Path


def setup_venv(root_path: Path):
    conda_env_name = str(root_path.absolute()).replace("/", "_")

    cmd = "&& ".join(
        [
            f"cd {root_path.absolute()}",
            "ls -al",
            # "source ~/.bashrc",
            "echo $USER",
            "echo $PATH",
            "echo $SHELL",
            "python -c \"print('hello world!')\"",
            "source ../../start/install_tools.sh",
        ]
    )

    result = subprocess.run(
        cmd,
        shell=True,
        executable="/bin/bash",
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        text=True,
    )

    # Print the return code (0 is success)
    print("Return code:", result.returncode)

    # Print the output of the command
    print("Output:", result.stdout)

    # Print the stderr if any error happened
    print("Error:", result.stderr)
