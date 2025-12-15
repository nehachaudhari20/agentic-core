from llm.client import LLMClient
from agent.planner import Planner

def main():
    task = "Investigate high API latency incident"

    llm = LLMClient()
    planner = Planner(llm)

    plan = planner.create_plan(task)

    print("\n=== AGENT PLAN ===")
    print(plan.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
