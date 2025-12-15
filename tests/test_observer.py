from agent.observer import Observer


def test_observer_interprets_logs():
    observer = Observer()

    execution = {
        "action": "search_logs",
        "output": {"matches": [1, 2, 3]},
    }

    observation = observer.observe(execution)
    assert "Found" in observation["insight"]
