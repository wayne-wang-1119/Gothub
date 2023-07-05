from .typing import WriteRepoInp, WriteRepoOut


def write_repo(inp: WriteRepoInp) -> WriteRepoOut:
    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    raise NotImplementedError
