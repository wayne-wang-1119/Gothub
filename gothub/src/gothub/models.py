from dataclasses import dataclass

from gothub.write_github import GothubPullRequest


@dataclass
class Oracle:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    url: str


@dataclass
class Ability:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    url: str


@dataclass
class Agent:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    oracles: list[Oracle]
    abilities: list[Ability]


@dataclass
class Order:
    """
    TODO author
    """

    id: str
    name: str  # This means title
    description: str
    target_repo_url: str
    agent: Agent
    prompt: str


@dataclass
class OrderOut:
    order: Order
    pull_requests: list[GothubPullRequest]
