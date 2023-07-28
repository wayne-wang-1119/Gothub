from datetime import datetime

from gothub.models import Agent, Oracle, Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import TEST_HTTPS_URL

TEST_HTTPS_URL_NEXTJS = "https://github.com/kingh0730/Order-nextjs.git"


TEST_ORACLE_URL = "https://github.com/Git-of-Thoughts/Oracle-EmptyOracle.git"
KINGH0730_INFO_ORACLE_URL = (
    "https://github.com/Git-of-Thoughts/Oracle-private.kinghan.info.git"
)


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
3. Obtain kingh0730's personal info from the `kingh0730_info_oracle` oracle.
3. Fill in the `page.js` file with a personal portfolio page written in React
    - You must incorporate `index`, `experience`, and `coursework` from the oracle.
    - You must start your file with `"use client";`
    - You must not include any `img` tags in your file.
    - Otherwise Next.js will not be able to render your code on the client side.
""",
        agent=Agent(
            id="test_agent",
            name="Test Agent",
            description="Test Agent description",
            oracles=[
                Oracle(
                    id="kingh0730_info_oracle",
                    name="kingh0730's personal info",
                    description="This oracle outputs kingh0730's personal info",
                    url=KINGH0730_INFO_ORACLE_URL,
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
