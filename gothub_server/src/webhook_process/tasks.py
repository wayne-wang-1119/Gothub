import os

import dotenv
from github import Github

from gothub.models import Agent, Oracle, Order, OrderOut
from gothub.order import (
    GithubOrderInp,
    GithubOrderOut,
    take_order,
)
from gothub.order_web import take_order_web

from . import firestore_client


def process_order_web(
    order_id: str,
    user_id: str,
    username: str,
    https_url: str,
    preprompt: str,
    prompt: str,
    # TODO Need to get oracles, abilities, etc.
):
    # TODO Preprompt should be system message to agent
    extra_prompt = preprompt + "\n\n" + prompt

    hub = Order(
        id=f"{user_id}_{order_id}",
        name=f"PR for {username} #{order_id}",
        description=NotImplemented,
        target_repo_url=https_url,
        agent=Agent(
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            oracles=[],
            abilities=[],
        ),
        prompt=extra_prompt,
    )

    order_output: OrderOut = take_order_web(hub)

    first_pr = order_output.pull_requests[0]

    set_doc_result = (
        firestore_client.collection("users")
        .document(user_id)
        .collection("orders")
        .document(order_id)
        .set(
            {
                "status": "completed",
                "result": first_pr.pr.html_url + "/files",
            }
        )
    )


def process_issue_opened(
    issue: dict,
    repository: dict,
    sender: dict,
    access_token: str,
):
    username = sender["login"]
    https_url = repository["clone_url"]

    openai_api_key = os.environ["OPENAI_API_KEY"]

    # Reply a comment
    # TODO Make more elaborate
    repository_full_name = repository["full_name"]
    github = Github(access_token)
    github_repo = github.get_repo(repository_full_name)
    github_issue = github_repo.get_issue(issue["number"])
    github_issue.create_comment("Thanks for opening this issue!")

    # Extract the issue title and body.
    issue_title = issue.get("title", "")
    issue_body = issue.get("body", "")

    # TODO Make more elaborate
    extra_prompt = "title: " + issue_title + "\nbody: " + issue_body

    hub = GithubOrderInp(
        username=username,
        https_url=https_url,
        github_token=access_token,
        openai_api_key=openai_api_key,
        extra_prompt=extra_prompt,
    )

    take_order(hub)
