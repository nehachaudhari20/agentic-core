from agent.planner import Planner
from agent.executor import Executor
from agent.observer import Observer
from tools.tool_registry import ToolRegistry

from runtime.retry_policy import RetryPolicy
from agent.self_reflection import SelfReflection

from memory.short_term import ShortTermMemory
class BaseAgent:
    def __init__(self, llm_client, executor):
        self.planner = Planner(llm_client)
        self.executor = executor
        self.observer = Observer()
        self.reflector = SelfReflection()
        self.memory = ShortTermMemory()

    def run(self, goal: str):
        plan = self.planner.create_plan(goal)

        for step in plan.steps:
            if step.action == "respond":
                return {
                    "status": "success",
                    "final_answer": step.input.get("message")
                }

            execution = self.executor.execute(step)
            observation = self.observer.observe(execution)

            self.memory.add({
                "step": step.action,
                "observation": observation
            })

            if self.reflector.should_retry(observation):
                plan = self.reflector.fix_plan(plan, observation)
                return {
                    "status": "retry",
                    "reason": observation
                }

            if step.action == "respond":
                return {
                    "status": "success",
                    "final_answer": execution.get("result")
                }

        return {
            "status": "incomplete",
            "memory": self.memory.dump()
        }