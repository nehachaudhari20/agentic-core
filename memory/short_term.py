class ShortTermMemory:
    def __init__(self):
        self.buffer = []

    def add(self, item: dict):
        self.buffer.append(item)

    def dump(self):
        return self.buffer

    def summarize(self):
        return {
            "steps_seen": len(self.buffer),
            "errors": [
                x for x in self.buffer
                if x["observation"].get("status") == "error"
            ]
        }
