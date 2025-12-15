# llm/schemas.py
from typing import List, Literal
from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    action: Literal["search_logs", "fetch_metrics", "respond", "think"]
    input: dict = Field(default_factory=dict)
    reasoning: str


class AgentPlan(BaseModel):
    goal: str
    steps: List[PlanStep]
