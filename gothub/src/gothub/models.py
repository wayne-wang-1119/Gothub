from attrs import define


@define
class Oracle:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    url: str


@define
class Ability:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    url: str


@define
class Agent:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    oracles: list[Oracle]
    abilities: list[Ability]


@define
class Order:
    """
    TODO author
    """

    id: str
    name: str
    description: str
    agent: Agent
    prompt: str
