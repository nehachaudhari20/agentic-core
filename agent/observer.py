class Observer:
    def observe(self, execution_result: dict):
        if execution_result["status"] == "error":
            return {
                "type": "error",
                "details": execution_result["output"]
            }

        return {
            "type": "observation",
            "data": execution_result["output"]
        }
