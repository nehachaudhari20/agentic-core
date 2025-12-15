from enum import Enum, auto


class AgentState(Enum):
    INIT = auto()          # Agent just started
    PLANNING = auto()      # Asking LLM what to do
    ACTING = auto()        # Executing tools
    OBSERVING = auto()     # Reading tool results
    REFLECTING = auto()    # Self-correction / retry logic
    FINISHED = auto()      # Task completed
    FAILED = auto()        # Gave up safely
