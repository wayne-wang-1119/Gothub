# stdlib imports
import os
import argparse

# third-party imports
from dotenv import load_dotenv
from git import Repo

# local imports
from .typing import WriteRepoInp, WriteRepoOut


load_dotenv()


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


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

    # Checks that the directory is a git repo
    with Repo(args.dir) as repo:
        write_repo_out = git_of_thoughts(
            WriteRepoInp(
                repo=repo,
                openai_api_key=OPENAI_API_KEY,
                extra_prompt=None,
            )
        )
