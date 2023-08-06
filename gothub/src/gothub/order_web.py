import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from github import Github
from github.Auth import Token

from gothub.models import Agent, Order, OrderOut
from gothub.order import SETUP_ORDERS_BASE_DIR
from gothub.setup_repo import SetupRepoInp, setup_repo
from gothub.write_github import create_pull_request
from gots.repo_agent import RepoAgent, WriteRepoInp, gots_repo_agent

from .setup_venv import setup_venv
from .tokens import generate_installation_access_token

TARGET_REPO_DIR = "target_repo"


def take_order_web(inp: Order) -> OrderOut:
    match inp:
        case Order(
            id=id,
            name=name,  # This means title
            target_repo_url=target_repo_url,
            prompt=prompt,
            agent=agent,
        ):
            match agent:
                case Agent(
                    id=agent_id,
                    name=agent_name,
                    description=agent_description,
                    oracles=oracles,
                    abilities=abilities,
                ):
                    # ! FIXME make configurable
                    branch_name = None
                    github_token = os.environ["GITHUB_TOKEN"]
                    openai_api_key = os.environ["OPENAI_API_KEY"]
                    repo_agent = gots_repo_agent

                    # ! For Order-nextjs, Order-portfolio-starter-kit...
                    installation_id = 40121718
                    access_token_data = generate_installation_access_token(
                        installation_id
                    )
                    access_token = access_token_data["token"]
                    github_token = access_token

    setup_dir = SETUP_ORDERS_BASE_DIR + "/" + id

    # Oracles
    for oracle in oracles:
        setup_repo_inp = SetupRepoInp(
            setup_dir=setup_dir + "/" + oracle.id,
            https_url=oracle.url,
            github_token=github_token,
        )
        with setup_repo(setup_repo_inp) as repo:
            pass

    # TODO Abilities

    setup_repo_inp = SetupRepoInp(
        setup_dir=setup_dir + "/" + TARGET_REPO_DIR,
        https_url=target_repo_url,
        github_token=github_token,
        branch_name=branch_name,
    )

    with setup_repo(setup_repo_inp) as repo:
        # Setup virtual env
        setup_venv(Path(repo.working_dir).parent)

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

    # !!! Use Sweep
    sweep_issue = github_repo.create_issue(
        title=f"Sweep: {name}",
        body=prompt,
    )

    order_out = OrderOut(
        order=inp,
        pull_requests=new_pull_requests,
    )

    return order_out
