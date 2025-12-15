from llm.client import LLMClient
from agent.base_agent import BaseAgent
from tools.tool_registry import ToolRegistry
from tools.log_search import LogSearchTool
from tools.metrics_fetch import MetricsFetchTool
from agent.executor import Executor


if __name__ == "__main__":
    registry = ToolRegistry()
    registry.register(LogSearchTool())
    registry.register(MetricsFetchTool())

    executor = Executor(registry)

    agent = BaseAgent(
        llm_client=LLMClient(),
        executor=executor
    )

    result = agent.run("Investigate high API latency incident")

    print("\n=== FINAL RESULT ===")
    print(result)
