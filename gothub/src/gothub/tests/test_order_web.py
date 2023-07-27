from datetime import datetime

from gothub.models import Agent, Oracle, Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import TEST_HTTPS_URL

TEST_ORACLE_URL = "https://github.com/Git-of-Thoughts/Oracle-EmptyOracle.git"


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
            oracles=[
                Oracle(
                    id="test_oracle",
                    name="Test Oracle",
                    description="Test Oracle description",
                    url=TEST_ORACLE_URL,
                ),
                Oracle(
                    id="test_oracle_2",
                    name="Test Oracle 2",
                    description="Test Oracle 2 description",
                    url=TEST_ORACLE_URL,
                ),
            ],
            abilities=[],
        ),
    )

    out = take_order_web(inp)

    assert isinstance(out, OrderOut)
    assert out.order is inp
