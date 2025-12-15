import json
from .base_tool import BaseTool

class LogSearchTool(BaseTool):
    name = "search_logs"

    def run(self, input: dict):
        with open("data/logs.json") as f:
            logs = json.load(f)

        return {
            "action": self.name,
            "status": "success",
            "output": logs[:3]
        }
