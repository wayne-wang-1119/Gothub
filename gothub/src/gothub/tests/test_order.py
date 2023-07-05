from datetime import datetime
from . import (
    TEST_HTTPS_URL,
    OTHER_BRANCH,
    GITHUB_TOKEN,
)
from ..order import (
    take_order,
    GithubOrderInp,
    GithubOrderOut,
)
from gots.typing import (
    RepoAgent,
    WriteRepoInp,
    WriteRepoOut,
)


TESTS_USERNAME = "../tests/"
TESTS_BRANCH_DIR = "gothub_mock/"


def mock_repo_agent(inp: WriteRepoInp) -> WriteRepoOut:
    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    time = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")

    new_branch_name_1 = TESTS_BRANCH_DIR + time + "(1)"
    new_branch_name_2 = TESTS_BRANCH_DIR + time + "(2)"

    new_branch_1 = repo.create_head(new_branch_name_1)
    new_branch_2 = repo.create_head(new_branch_name_2)

    return WriteRepoOut(
        new_branches=[
            new_branch_1,
            new_branch_2,
        ],
    )


def test_order():
    inp = GithubOrderInp(
        username=TESTS_USERNAME,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        openai_api_key="...",
        branch_name=None,
        extra_prompt=None,
        repo_agent=mock_repo_agent,
    )

    out = take_order(inp)

    assert isinstance(out, GithubOrderOut)
    assert out.order_id is not None
