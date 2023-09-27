import argparse
import os
from datetime import datetime

## this imports the load_dotenv function from the dotenv package
from dotenv import load_dotenv
from git import Repo

## this imports the gots_repo_agent function from the repo_agent.py file
from .repo_agent import (
    WriteRepoInp,
    WriteRepoOut,
    gots_repo_agent,
)

load_dotenv()  # Load environment variables from .env file


OPENAI_API_KEY = os.environ[
    "OPENAI_API_KEY"
]  # Get OpenAI API key from environment variable


def main():
    parser = argparse.ArgumentParser(
        description="Git of Thoughts",
    )  # Create argument parser
    parser.add_argument(
        "--dir",
        help="Git repo directory",
        required=True,
    )  # Add --dir argument

    args = parser.parse_args()  # Parse arguments

    # Checks that the directory is a git repo
    with Repo(args.dir) as repo:
        write_repo_out = gots_repo_agent(
            WriteRepoInp(
                repo=repo,
                openai_api_key=OPENAI_API_KEY,
                extra_prompt=None,
            )
        )  # Run repo agent

        new_branches = write_repo_out.new_branches  # Get new branches

        for branch in new_branches:
            print("New branch:", end=" ")  # Print new branch
            print(branch)  # Print new branch
