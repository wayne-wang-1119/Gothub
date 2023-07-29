from datetime import datetime

from gothub.models import Agent, Oracle, Order, OrderOut
from gothub.order_web import take_order_web
from gothub.tests import TEST_HTTPS_URL

TEST_HTTPS_URL_NEXTJS = "https://github.com/kingh0730/Order-nextjs.git"
TEST_HTTPS_URL_PORTFOLIO_STARTER_KIT = (
    "https://github.com/kingh0730/Order-portfolio-starter-kit.git"
)


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


def _test_order_nextjs():
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
    - Add `<style>` tags to the `page.js` file to center and justify the text.
    - And add a vibrant background color that's gradient from top to bottom.
    - You must incorporate EVERYTHING from `index`, `experience`, and `coursework`.
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


def test_order_sweep_portfolio_starter_kit():
    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")

    inp = Order(
        id=time,
        name="Replace the content with my own information",
        description="Test Order description",
        target_repo_url=TEST_HTTPS_URL_PORTFOLIO_STARTER_KIT,
        prompt="""
My information in YAML format:

- Name: Shangdian (King) Han
- Email: kingh0730@berkeley.edu
- LinkedIn: https://www.linkedin.com/in/kingh0730/
- GitHub: https://www.github.com/kingh0730/
- Introduction: >
    Hi there! 👋

    I'm Shangdian (King) Han.

    At Microsoft Research, I prototyped the new Office AI for Excel.

    I believe high-quality code generation AI will be
    the most important development for human civilization in the near future,
    for the simple reason that code shapes our world today.

    That's why I'm building an LLM agent customization platform to
    enhance the SOTA in code generation AI.
""",
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
