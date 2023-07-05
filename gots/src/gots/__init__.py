from .typing import WriteRepoInp, WriteRepoOut


def git_of_thoughts(inp: WriteRepoInp) -> WriteRepoOut:
    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    return WriteRepoOut(
        new_branches=[],
    )
