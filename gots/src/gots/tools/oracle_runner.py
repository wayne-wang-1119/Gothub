from langchain.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field


class _OracleRunnerInput(BaseModel):
    oracle_id: str = Field(
        ...,
        description="id of the oracle to run",
    )


def run_oracle(oracle_id: str) -> str:
    """
    Run the oracle with the given id.

    :param oracle_id: id of the oracle to run
    :return: result of the oracle
    """
    return str(630)


oracle_runner = StructuredTool.from_function(run_oracle)
