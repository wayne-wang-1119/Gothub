# stdlib imports
import argparse

# local imports
from .typing import WriteRepoInp, WriteRepoOut


def main():
    parser = argparse.ArgumentParser(
        description="Git of Thoughts",
    )
    parser.add_argument(
        "--dir",
        help="Git repo directory",
        required=True,
    )

    args = parser.parse_args()


def git_of_thoughts(inp: WriteRepoInp) -> WriteRepoOut:
    """
    ! Should only modify what's permitted by inp
    """

    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    result = WriteRepoOut(
        new_branches=[],
    )

    raise NotImplementedError("git_of_thoughts")

    return result
