import json
import os
import subprocess
import sys
import time
from pathlib import Path

import dotenv
import jwt
import requests

from gothub.order import (
    GithubOrderInp,
    GithubOrderOut,
    take_order,
)

dotenv.load_dotenv()


# Ugly
GITHUB_PEM_PATH = (
    Path(__file__).absolute().parent.parent.parent.parent / "gothub-ai.private-key.pem"
)
GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")


with open(GITHUB_PEM_PATH, "rb") as pem_file:
    SIGNING_KEY = jwt.jwk_from_pem(pem_file.read())


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


def generate_jwt() -> str:
    payload = {
        # Issued at time
        "iat": int(time.time()),
        # JWT expiration time (10 minutes maximum)
        "exp": int(time.time()) + 600,
        # GitHub App's identifier
        "iss": GITHUB_APP_ID,
    }

    # Create JWT
    jwt_instance = jwt.JWT()
    encoded_jwt = jwt_instance.encode(
        payload,
        SIGNING_KEY,
        alg="RS256",
    )

    return encoded_jwt


def generate_installation_access_token(installation_id):
    jwt = generate_jwt()

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.post(
        f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers=headers,
    )

    if response.status_code == 201:
        token_data = response.json()
        return token_data["token"]
    else:
        raise Exception("Failed to generate installation access token")
