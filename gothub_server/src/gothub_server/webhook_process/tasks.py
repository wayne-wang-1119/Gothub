import json
import os
import subprocess
import sys

# from gothub.order import (
#     GithubOrderInp,
#     GithubOrderOut,
#     take_order,
# )

# from gots.repo_agent import (
#     RepoAgent,
#     WriteRepoInp,
# )

# GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]


def process_webhook(data):
    data = json.loads(data)

    # username = data["sender"]["login"]
    # https_url = data["repository"]["clone_url"]
    # openai_api_key = os.environ["OPENAI_API_KEY"]
    # branch_name = data["repository"]["default_branch"]

    # if "issue" in data:
    #     # Extract the issue title and body.
    #     issue_title = data["issue"]["title"]
    #     issue_body = data["issue"]["body"]
    #     issue = "title: " + issue_title + "\nbody: " + issue_body
    #     git = WriteRepoInp(
    #         repo=https_url, openai_api_key=openai_api_key, extra_prompt=issue
    #     )
    #     agent = None
    #     hub = GithubOrderInp(
    #         username=username,
    #         https_url=https_url,
    #         github_token=GITHUB_TOKEN,
    #         openai_api_key=openai_api_key,
    #         branch_name=branch_name,
    #         extra_prompt=None,
    #         repo_agent=agent,
    #     )

    #     take_order(hub)
    # else:
    #     return "need an issue created"
