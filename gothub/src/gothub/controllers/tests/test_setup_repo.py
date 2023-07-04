# stdlib imports
import os
from pathlib import Path

# local imports
from ..setup_repo import (
    setup_repo,
    SetupRepoControllerInp,
    mkdir_if_available_else_error,
    SETUP_BASE_DIR,
)


SETUP_TESTS_BASE_DIR = "tests"


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
