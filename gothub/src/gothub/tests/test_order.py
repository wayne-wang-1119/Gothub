from datetime import datetime

from gots.repo_agent import (
    RepoAgent,
    WriteRepoInp,
    WriteRepoOut,
)

from ..order import (
    GithubOrderInp,
    GithubOrderOut,
    take_order,
)
from . import (
    GITHUB_TOKEN,
    OPENAI_API_KEY,
    OTHER_BRANCH,
    TEST_HTTPS_URL,
)

TESTS_USERNAME = "../tests/"
TESTS_BRANCH_DIR = "gothub_mock/"


def mock_repo_agent(inp: WriteRepoInp) -> WriteRepoOut:
    repo = inp.repo

    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")
    original_branch = repo.active_branch

    new_branch_name_1 = TESTS_BRANCH_DIR + time + "(1)"
    new_branch_name_2 = TESTS_BRANCH_DIR + time + "(2)"

    new_branches = []
    for new_branch_name in [
        new_branch_name_1,
        new_branch_name_2,
    ]:
        new_branch = repo.create_head(new_branch_name)
        new_branch.checkout()

        repo.git.commit("--allow-empty", "-m", "empty commit")
        new_branches.append(new_branch)

        original_branch.checkout()

    return WriteRepoOut(
        new_branches=new_branches,
    )


def _test_order_mock_repo_agent():
    inp = GithubOrderInp(
        username=TESTS_USERNAME,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        openai_api_key=OPENAI_API_KEY,
        branch_name=None,
        extra_prompt=None,
        repo_agent=mock_repo_agent,
    )

    out = take_order(inp)

    assert isinstance(out, GithubOrderOut)
    assert out.order_id is not None


def test_order_gots_repo_agent():
    inp = GithubOrderInp(
        username=TESTS_USERNAME,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        openai_api_key=OPENAI_API_KEY,
        branch_name=None,
        extra_prompt=None,
        repo_agent=None,
    )

    out = take_order(inp)

    assert isinstance(out, GithubOrderOut)
    assert out.order_id is not None
