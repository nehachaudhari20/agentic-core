# tests/test_planner.py
from llm.client import LLMClient
from agent.planner import Planner
from llm.schemas import AgentPlan


def test_planner_creates_plan():
    llm = LLMClient()
    planner = Planner(llm)

    plan = planner.create_plan("Investigate high API latency incident")

    assert isinstance(plan, AgentPlan)
    assert plan.goal is not None
    assert len(plan.steps) > 0
