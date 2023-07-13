import json
import os
import subprocess
import sys

from gothub.order import (
    GithubOrderInp,
    GithubOrderOut,
    take_order,
)


def process_webhook(data):
    data = json.loads(data)

    username = data["sender"]["login"]
    https_url = data["repository"]["clone_url"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
    branch_name = data["repository"]["default_branch"]
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
    if "issue" in data:
        # Extract the issue title and body.
        issue_title = data["issue"]["title"] if "title" in data["issue"] else ""
        issue_body = data["issue"]["body"] if "body" in data["issue"] else ""
        issue = "title: " + issue_title + "\nbody: " + issue_body
        hub = GithubOrderInp(
            username=username,
            https_url=https_url,
            github_token=GITHUB_TOKEN,
            openai_api_key=openai_api_key,
            branch_name=branch_name,
            extra_prompt=None,
        )

        take_order(hub)
    else:
        return "need an issue created"
