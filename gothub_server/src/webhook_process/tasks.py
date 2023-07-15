import json
import os
import subprocess

import requests

from gothub.order import (
    GithubOrderInp,
    GithubOrderOut,
    take_order,
)


def process_webhook(data, github_token):
    data = json.loads(data)

    username = data["sender"]["login"]
    https_url = data["repository"]["clone_url"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
    branch_name = data["repository"]["default_branch"]
    GITHUB_TOKEN = github_token
    if (
        "issue" in data
        and "action" in data
        and data["action"]
        in [
            "created",
            "opened",
        ]
    ):
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
            extra_prompt=issue,
        )

        take_order(hub)
    else:
        return "need an issue created"


def get_access_token(installation_id):
    headers = {
        "Authorization": f'Bearer {os.getenv("GITHUB_APP_PRIVATE_KEY")}',
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.post(
        f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers=headers,
    )
