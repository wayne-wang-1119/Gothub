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


TESTS_USERNAME = "tests"


def test_order():
    inp = GithubOrderInp(
        username=TESTS_USERNAME,
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        openai_api_key="...",
        branch_name=None,
        extra_prompt=None,
    )

    out = take_order(inp)

    assert isinstance(out, GithubOrderOut)
    assert out.order_id is not None
