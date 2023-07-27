import subprocess


def setup_venv(root_path):
    cmd = "python -c \"print('hello world')\""

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
