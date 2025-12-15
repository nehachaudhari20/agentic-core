from runtime.state_machine import AgentStateMachine
from agent.states import AgentState


def test_valid_transitions():
    sm = AgentStateMachine()
    sm.transition(AgentState.PLANNING)
    sm.transition(AgentState.ACTING)
    sm.transition(AgentState.OBSERVING)
    sm.transition(AgentState.REFLECTING)
    sm.transition(AgentState.PLANNING)


def test_invalid_transition():
    sm = AgentStateMachine()
    try:
        sm.transition(AgentState.ACTING)
    except Exception:
        assert True
    else:
        assert False
