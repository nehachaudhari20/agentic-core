class Executor:
    def __init__(self, registry):
        self.registry = registry

    def execute(self, step):
        if not self.registry.has(step.action):
            return {
                "action": step.action,
                "status": "error",
                "output": f"No tool registered for {step.action}"
            }

        tool = self.registry.get(step.action)
        return tool.run(step.input)
