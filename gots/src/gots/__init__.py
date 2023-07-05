import argparse
from datetime import datetime
import os

from dotenv import load_dotenv
from git import Repo

from .repo_agent import (
    WriteRepoInp,
    WriteRepoOut,
    gots_repo_agent,
)

load_dotenv()


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


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
        write_repo_out = gots_repo_agent(
            WriteRepoInp(
                repo=repo,
                openai_api_key=OPENAI_API_KEY,
                extra_prompt=None,
            )
        )

        new_branches = write_repo_out.new_branches

        for branch in new_branches:
            print("New branch:", end=" ")
            print(branch)
