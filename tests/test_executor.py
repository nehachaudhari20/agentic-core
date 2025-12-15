from agent.executor import Executor
from tools.tool_registry import ToolRegistry
from llm.schemas import PlanStep


def test_executor_runs_tool():
    registry = ToolRegistry()
    executor = Executor(registry)

    step = PlanStep(
        action="search_logs",
        input={"service": "payments"},
        reasoning="Test log search",
    )

    result = executor.execute(step)
    assert "output" in result
