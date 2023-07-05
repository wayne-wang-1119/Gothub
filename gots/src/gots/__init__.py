from .typing import WriteRepoInp, WriteRepoOut


def git_of_thoughts(inp: WriteRepoInp) -> WriteRepoOut:
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
