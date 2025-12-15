class SelfReflection:
    def should_retry(self, observation: dict) -> bool:
        """
        Decide whether agent should retry based on observation
        """
        if observation.get("status") == "error":
            return True
        return False

    def fix_plan(self, plan, observation):
        """
        Modify the plan when something fails
        """
        # Simple policy for now
        for step in plan.steps:
            if step.action == "respond":
                step.reasoning += " (adjusted after failure)"
        return plan
