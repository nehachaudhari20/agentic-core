class BaseTool:
    name: str

    def run(self, input: dict) -> dict:
        raise NotImplementedError
