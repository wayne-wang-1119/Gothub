import os
from .repo_agent import WriteRepoInp
import langchain
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from .callbacks.git_callback_handler import GitCallbackHandler
from .tools.scoped_file_tools import build_scoped_file_tools


def one_branch_agent(inp: WriteRepoInp) -> None:
    match inp:
        case WriteRepoInp(
            repo=repo,
            openai_api_key=openai_api_key,
            extra_prompt=extra_prompt,
        ):
            pass

    tools = build_scoped_file_tools(repo.working_dir)
    git_callback_handler = GitCallbackHandler()

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
        callbacks=[
            git_callback_handler,
        ],
        openai_api_key=openai_api_key,
    )

    mrkl = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_MULTI_FUNCTIONS,
        verbose=True,
    )

    mrkl.run("write me a fun python script file")
