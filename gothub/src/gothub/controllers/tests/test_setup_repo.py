# stdlib imports
import os
from pathlib import Path

# third-party imports
import dotenv

# local imports
from ..setup_repo import (
    setup_repo,
    SetupRepoControllerInp,
    mkdir_if_available_else_error,
    SETUP_BASE_DIR,
)


SETUP_TESTS_BASE_DIR = "tests/"
TEST_HTTPS_URL = "https://github.com/Git-of-Thoughts/GoT-test.git"
GITHUB_TOKEN = os.getenv("GITHUB_GOT_TEST_TOKEN")


def test_mkdir_if_available_else_error():
    dir = "test_mkdir_if_available_else_error"
    path = Path(SETUP_BASE_DIR / SETUP_TESTS_BASE_DIR / dir)
    mkdir_if_available_else_error(path)

    assert path.exists()

    path.rmdir()


def test_setup_repo():
    inp = SetupRepoControllerInp(
        setup_dir="test_setup_repo",
        https_url="",
        github_token="",
        branch_name="",
    )
