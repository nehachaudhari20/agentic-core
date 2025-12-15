# llm/client.py
import json
from typing import Type
from pydantic import BaseModel


class LLMClient:
    def __init__(self, model_name: str = "gpt-4"):
        self.model_name = model_name

    def generate(
        self,
        prompt: str,
        output_schema: Type[BaseModel],
    ) -> BaseModel:
        """
        Calls LLM and enforces JSON-only output.
        """
        # MOCKED FOR NOW (important)
        raw_response = self._mock_response()

        try:
            parsed = json.loads(raw_response)
            return output_schema(**parsed)
        except Exception as e:
            raise ValueError(f"Invalid LLM output: {e}")

    def _mock_response(self) -> str:
        return """
        {
          "goal": "Investigate high API latency incident",
          "steps": [
            {
              "action": "search_logs",
              "input": {"service": "payments"},
              "reasoning": "Check recent errors or slow queries"
            },
            {
              "action": "fetch_metrics",
              "input": {"metric": "latency_p99"},
              "reasoning": "Confirm latency spike"
            },
            {
              "action": "respond",
              "input": {"message": "Latency caused by DB connection saturation"},
              "reasoning": "Enough evidence collected"
            }
          ]
        }
        """
