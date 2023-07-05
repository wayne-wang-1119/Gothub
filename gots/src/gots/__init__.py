import argparse
from datetime import datetime
import os

from dotenv import load_dotenv
from git import Repo

from .repo_agent import WriteRepoInp, WriteRepoOut

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

    time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")
    original_branch = repo.active_branch

    new_branch_name_1 = "gothub_got" + time + "(1)"
    new_branch_name_2 = "gothub_got" + time + "(2)"

    new_branches = []
    for new_branch_name in [
        new_branch_name_1,
        new_branch_name_2,
    ]:
        new_branch = repo.create_head(new_branch_name)
        new_branch.checkout()

        repo.git.commit("--allow-empty", "-m", "empty commit")
        new_branches.append(new_branch)

        original_branch.checkout()

    return WriteRepoOut(
        new_branches=new_branches,
    )


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

        new_branches = write_repo_out.new_branches

        for branch in new_branches:
            print("New branch:", end=" ")
            print(branch)
