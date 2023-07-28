from datetime import datetime

from gothub.models import Agent, Oracle, Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import TEST_HTTPS_URL

TEST_HTTPS_URL_NEXTJS = "https://github.com/kingh0730/Order-nextjs.git"


TEST_ORACLE_URL = "https://github.com/Git-of-Thoughts/Oracle-EmptyOracle.git"


def _test_order_web_oracle():
    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")

    inp = Order(
        id=time,
        name="Test Order",
        description="Test Order description",
        target_repo_url=TEST_HTTPS_URL,
        prompt="Run `test_oracle` and give me back the secret number",
        agent=Agent(
            id="test_agent",
            name="Test Agent",
            description="Test Agent description",
            oracles=[
                Oracle(
                    id="test_oracle",
                    name="Test Oracle",
                    description="This oracle outputs a secret number",
                    url=TEST_ORACLE_URL,
                ),
                # Oracle(
                #     id="test_oracle_2",
                #     name="Test Oracle 2",
                #     description="This oracle outputs a secret number",
                #     url=TEST_ORACLE_URL,
                # ),
            ],
            abilities=[],
        ),
    )

    out = take_order_web(inp)

    assert isinstance(out, OrderOut)
    assert out.order is inp


def test_order_nextjs():
    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")

    inp = Order(
        id=time,
        name="Test Order",
        description="Test Order description",
        target_repo_url=TEST_HTTPS_URL_NEXTJS,
        prompt="""
1. Delete the `app/page.js` file.
2. Create a new file called `app/page.js`.
3. Fill in the `page.js` file with the following content:
    - a fun snake game
4. Run `test_oracle` and obtain the secret number
5. Display the secret number on the `page.js` file
""",
        agent=Agent(
            id="test_agent",
            name="Test Agent",
            description="Test Agent description",
            oracles=[
                Oracle(
                    id="test_oracle",
                    name="Test Oracle",
                    description="This oracle outputs a secret number",
                    url=TEST_ORACLE_URL,
                ),
                # Oracle(
                #     id="test_oracle_2",
                #     name="Test Oracle 2",
                #     description="This oracle outputs a secret number",
                #     url=TEST_ORACLE_URL,
                # ),
            ],
            abilities=[],
        ),
    )

    out = take_order_web(inp)

    assert isinstance(out, OrderOut)
    assert out.order is inp
