import os
import re
from datetime import datetime

from github import Github
from github.Auth import Token

from gothub.models import Order, OrderOut
from gothub.order import SETUP_ORDERS_BASE_DIR
from gothub.setup_repo import SetupRepoInp, setup_repo
from gothub.write_github import create_pull_request
from gots.repo_agent import RepoAgent, WriteRepoInp, gots_repo_agent


def take_order_web(inp: Order) -> OrderOut:
    match inp:
        case Order(
            id=id,
            target_repo_url=target_repo_url,
            prompt=prompt,
        ):
            # ! FIXME make configurable
            branch_name = None
            github_token = os.environ["GITHUB_TOKEN"]
            openai_api_key = os.environ["OPENAI_API_KEY"]
            repo_agent = gots_repo_agent

    setup_dir = SETUP_ORDERS_BASE_DIR + "/" + id

    setup_repo_inp = SetupRepoInp(
        setup_dir=setup_dir,
        https_url=target_repo_url,
        github_token=github_token,
        branch_name=branch_name,
    )

    with setup_repo(setup_repo_inp) as repo:
        write_repo_out = repo_agent(
            WriteRepoInp(
                repo=repo,
                openai_api_key=openai_api_key,
                extra_prompt=prompt,
            )
        )

        new_branches = write_repo_out.new_branches

        # TODO abstract this away
        for branch in new_branches:
            repo.remote().push(branch)

    # TODO abstract this away
    github = Github(auth=Token(github_token))
    pattern = r"github\.com/([^/]+)/([^/]+)\.git"
    match = re.search(pattern, target_repo_url)
    full_name = match.group(1) + "/" + match.group(2) if match else ""
    github_repo = github.get_repo(full_name)

    new_pull_requests = [
        create_pull_request(
            github_repo,
            branch,
        )
        for branch in new_branches
    ]

    return OrderOut(
        order=inp,
        pull_requests=new_pull_requests,
    )