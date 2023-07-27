import subprocess
from pathlib import Path


def setup_venv(root_path: Path):
    conda_env_name = str(root_path.absolute()).replace("/", "_")

    cmd = "&& ".join(
        [
            f"cd {root_path.absolute()}",
            "ls -al",
            "python -c \"print('hello world!')\"",
            f"conda create -n {conda_env_name} python=3.11 -y",
            f"conda activate {conda_env_name}",
            f"conda env remove -n {conda_env_name} -y",
        ]
    )

    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Print the return code (0 is success)
    print("Return code:", result.returncode)

    # Print the output of the command
    print("Output:", result.stdout)

    # Print the stderr if any error happened
    print("Error:", result.stderr)
