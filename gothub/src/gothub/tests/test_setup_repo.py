import os
import shutil
from datetime import datetime
from pathlib import Path

from git import Repo

from ..setup_repo import (
    SETUP_BASE_DIR,
    SetupRepoInp,
    mkdir_if_available_else_error,
    setup_repo,
)
from . import GITHUB_TOKEN, OTHER_BRANCH, TEST_HTTPS_URL

SETUP_TESTS_BASE_DIR = "tests/"


def test_mkdir_if_available_else_error():
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    dir = "test_mkdir_if_available_else_error" + time

    path = Path(SETUP_BASE_DIR / SETUP_TESTS_BASE_DIR / dir)
    mkdir_if_available_else_error(path)

    assert path.exists()


def test_setup_repo_default_branch():
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    dir = SETUP_TESTS_BASE_DIR + "test_setup_repo_default_branch" + time

    inp = SetupRepoInp(
        setup_dir=dir,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        branch_name=None,
    )

    with setup_repo(inp) as repo:
        assert repo.is_dirty() is False


def test_setup_repo_other_branch():
    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    dir = SETUP_TESTS_BASE_DIR + "test_setup_repo_other_branch" + time

    inp = SetupRepoInp(
        setup_dir=dir,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        branch_name=OTHER_BRANCH,
    )

    with setup_repo(inp) as repo:
        assert repo.is_dirty() is False
        assert repo.active_branch.name == OTHER_BRANCH
