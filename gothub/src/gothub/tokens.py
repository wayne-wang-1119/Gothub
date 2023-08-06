import os
import time
from pathlib import Path

import dotenv
import jwt
import requests

dotenv.load_dotenv()


# Ugly
GITHUB_PEM_PATH = (
    Path(__file__).absolute().parent.parent.parent.parent / "gothub-ai.private-key.pem"
)
GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")


with open(GITHUB_PEM_PATH, "rb") as pem_file:
    SIGNING_KEY = jwt.jwk_from_pem(pem_file.read())


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


def generate_installation_access_token(installation_id) -> dict:
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

    if response.status_code != 201:
        raise Exception("Failed to generate installation access token")

    token_data = response.json()
    return token_data
