import os
import langchain
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from .callbacks.CallbackHandler import MyCustomHandlerOne
from .callbacks.utils.git_methods import git_methods
from .tools.file_tools import (
    read_directory_tree_tool,
    read_one_file_tool,
    write_file_tool,
)

# keep this true if you want to see the outputs
langchain.debug = True

cwd = os.getcwd()

github_token = os.environ.get("GITHUB_TOKEN")
openai_api_key = os.environ.get("OPENAI_API_KEY")

repo_url = "https://github.com/Git-of-Thoughts/Gothub.git"
local_dir = cwd
access_token = github_token

git = git_methods(repo_url, local_dir, access_token)
handler = MyCustomHandlerOne(git)

llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo-0613",
    callbacks=[handler],
    openai_api_key=openai_api_key,
)

tools = [
    read_directory_tree_tool,
    read_one_file_tool,
    write_file_tool,
]


mrkl = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_MULTI_FUNCTIONS,
    verbose=True,
)


mrkl.run("write me a fun python script file")
