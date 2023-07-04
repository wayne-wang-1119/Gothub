from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from tools.file_tools import (
    read_directory_tree_tool,
    read_one_file_tool,
    write_file_tool,
    recursive_directory_tool,
)

# Initialize the OpenAI language model
# Replace <your_api_key> in openai_api_key="<your_api_key>" with your actual OpenAI key.
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

tools = [
    read_directory_tree_tool,
    read_one_file_tool,
    write_file_tool,
    recursive_directory_tool,
]


mrkl = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
)


import langchain

langchain.debug = True


mrkl.run(
    "what is the current directory looking like? and what does the file called file_tools_funcs.py containing?"
)
