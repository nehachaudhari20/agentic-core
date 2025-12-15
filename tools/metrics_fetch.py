import json
from .base_tool import BaseTool

class MetricsFetchTool(BaseTool):
    name = "fetch_metrics"

    def run(self, input: dict):
        with open("data/metrics.json") as f:
            metrics = json.load(f)

        return {
            "action": self.name,
            "status": "success",
            "output": metrics
        }
