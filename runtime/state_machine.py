from agent.states import AgentState


class InvalidStateTransition(Exception):
    pass


class AgentStateMachine:
    """
    Controls legal transitions between agent states
    """

    TRANSITIONS = {
        AgentState.INIT: {AgentState.PLANNING},
        AgentState.PLANNING: {AgentState.ACTING, AgentState.FAILED},
        AgentState.ACTING: {AgentState.OBSERVING, AgentState.FAILED},
        AgentState.OBSERVING: {AgentState.REFLECTING, AgentState.FINISHED},
        AgentState.REFLECTING: {AgentState.PLANNING, AgentState.FAILED},
        AgentState.FINISHED: set(),
        AgentState.FAILED: set(),
    }

    def __init__(self):
        self.current_state = AgentState.INIT

    def transition(self, next_state: AgentState):
        allowed = self.TRANSITIONS[self.current_state]
        if next_state not in allowed:
            raise InvalidStateTransition(
                f"Invalid transition: {self.current_state} → {next_state}"
            )
        self.current_state = next_state

    def is_terminal(self) -> bool:
        return self.current_state in {AgentState.FINISHED, AgentState.FAILED}
