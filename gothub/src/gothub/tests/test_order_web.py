from datetime import datetime

from gothub.models import Agent, Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import TEST_HTTPS_URL


def test_order_web_mock_repo_agent():
    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")

    inp = Order(
        id=time,
        name="Test Order",
        description="Test Order description",
        target_repo_url=TEST_HTTPS_URL,
        prompt="",
        agent=Agent(
            id="test_agent",
            name="Test Agent",
            description="Test Agent description",
            oracles=[],
            abilities=[],
        ),
    )

    out = take_order_web(inp)

    assert isinstance(out, OrderOut)
    assert out.order is inp
