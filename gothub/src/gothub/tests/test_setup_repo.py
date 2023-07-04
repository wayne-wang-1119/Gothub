# stdlib imports
import os
import shutil
from datetime import datetime
from pathlib import Path

# third-party imports
import dotenv
from git import Repo

# local imports
from ..setup_repo import (
    setup_repo,
    SetupRepoControllerInp,
    mkdir_if_available_else_error,
    SETUP_BASE_DIR,
)


dotenv.load_dotenv()


SETUP_TESTS_BASE_DIR = "tests/"
TEST_HTTPS_URL = "https://github.com/Git-of-Thoughts/GoT-test.git"
OTHER_BRANCH = "modify-snake.py"
GITHUB_TOKEN = os.getenv("GITHUB_GOT_TEST_TOKEN")


def test_mkdir_if_available_else_error():
    dir = "test_mkdir_if_available_else_error"
    path = Path(SETUP_BASE_DIR / SETUP_TESTS_BASE_DIR / dir)
    mkdir_if_available_else_error(path)

    assert path.exists()

    path.rmdir()


def test_setup_repo_default_branch():
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    dir = SETUP_TESTS_BASE_DIR + "test_setup_repo_default_branch" + time

    inp = SetupRepoControllerInp(
        setup_dir=dir,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        branch_name=None,
    )

    with setup_repo(inp) as repo:
        assert repo.is_dirty() is False


def test_setup_repo_other_branch():
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    dir = SETUP_TESTS_BASE_DIR + "test_setup_repo_other_branch" + time

    inp = SetupRepoControllerInp(
        setup_dir=dir,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        branch_name=OTHER_BRANCH,
    )

    with setup_repo(inp) as repo:
        assert repo.is_dirty() is False
        assert repo.active_branch.name == OTHER_BRANCH
