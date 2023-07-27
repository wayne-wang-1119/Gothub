from datetime import datetime

from gothub.models import Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import GITHUB_TOKEN, OPENAI_API_KEY, TEST_HTTPS_URL
from gothub.tests.test_order import mock_repo_agent


def test_order_web_mock_repo_agent():
    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")

    inp = Order(
        id=time,
        name="Test Order",
        https_url=TEST_HTTPS_URL,
        github_token=GITHUB_TOKEN,
        openai_api_key=OPENAI_API_KEY,
        branch_name=None,
        extra_prompt=None,
        repo_agent=mock_repo_agent,
    )

    out = take_order_web(inp)

    assert isinstance(out, OrderOut)
    assert out.order_id is not None
