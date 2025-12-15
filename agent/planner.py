# agent/planner.py
from llm.client import LLMClient
from llm.schemas import AgentPlan


class Planner:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def create_plan(self, goal: str) -> AgentPlan:
        prompt = f"""
GOAL:
{goal}
"""
        plan = self.llm.generate(
            prompt=prompt,
            output_schema=AgentPlan
        )
        return plan
