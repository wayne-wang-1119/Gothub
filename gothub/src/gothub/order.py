from pydantic.dataclasses import dataclass


@dataclass
class GithubPubOrderInp:
    https_url: str
    github_token: str
    openai_api_key: str


@dataclass
class GithubPubOrderOut:
    pull_requests: list[str]
