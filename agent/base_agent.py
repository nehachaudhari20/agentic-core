from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from enum import Enum, auto


class AgentState(Enum):
    INIT = auto()
    PLANNING = auto()
    EXECUTING = auto()
    OBSERVING = auto()
    REFLECTING = auto()
    DONE = auto()
    FAILED = auto()


class BaseAgent(ABC):
    """
    BaseAgent defines the deterministic agent loop.
    All agents in this repo must inherit from this.
    """

    def __init__(self, agent_id: str, max_steps: int = 10):
        self.agent_id = agent_id
        self.max_steps = max_steps
        self.current_step = 0

        self.state: AgentState = AgentState.INIT

        self.plan: Optional[Dict[str, Any]] = None
        self.last_action: Optional[Dict[str, Any]] = None
        self.last_observation: Optional[Any] = None

        self.final_result: Optional[Any] = None
        self.error: Optional[str] = None

    # -------------------------
    # Abstract methods
    # -------------------------

    @abstractmethod
    def plan_step(self) -> Dict[str, Any]:
        """
        Decide what to do next.
        Must return a structured plan (dict).
        """
        pass

    @abstractmethod
    def execute_step(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the planned action.
        Returns raw tool/action output.
        """
        pass

    @abstractmethod
    def observe_step(self, execution_result: Dict[str, Any]) -> Any:
        """
        Interpret execution output.
        """
        pass

    @abstractmethod
    def reflect_step(self) -> bool:
        """
        Decide whether:
        - continue
        - retry
        - terminate
        Return True if agent should continue, False if done.
        """
        pass

    # -------------------------
    # Core Agent Loop
    # -------------------------

    def run(self) -> Any:
        """
        Main agent loop.
        """
        try:
            self.state = AgentState.PLANNING

            while self.current_step < self.max_steps:
                self.current_step += 1

                # ---- PLAN ----
                self.state = AgentState.PLANNING
                self.plan = self.plan_step()

                # ---- EXECUTE ----
                self.state = AgentState.EXECUTING
                self.last_action = self.execute_step(self.plan)

                # ---- OBSERVE ----
                self.state = AgentState.OBSERVING
                self.last_observation = self.observe_step(self.last_action)

                # ---- REFLECT ----
                self.state = AgentState.REFLECTING
                should_continue = self.reflect_step()

                if not should_continue:
                    self.state = AgentState.DONE
                    return self.final_result

            # Max steps exceeded
            self.state = AgentState.FAILED
            self.error = "Max steps exceeded"
            return None

        except Exception as e:
            self.state = AgentState.FAILED
            self.error = str(e)
            return None
