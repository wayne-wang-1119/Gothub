import os
import langchain
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from .callbacks.git_callback_handler import GitCallbackHandler
from .tools.file_tools import (
    read_directory_tree_tool,
    read_one_file_tool,
    write_file_tool,
)


def one_branch_agent(openai_api_key: str):
    git_callback_handler = GitCallbackHandler()

    tools = [
        read_directory_tree_tool,
        read_one_file_tool,
        write_file_tool,
    ]

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
