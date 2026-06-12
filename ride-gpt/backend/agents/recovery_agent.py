from state.graph_state import add_log, set_timestamp

MAX_RECOVERY = 3


def recovery_agent(state: dict) -> dict:
    state = set_timestamp(state, "recovery_start")
    recovery_attempts = state.get("recovery_attempts", 0) + 1
    state = {**state, "recovery_attempts": recovery_attempts}
    state = add_log(state, "RecoveryAgent", f"Recovery attempt {recovery_attempts}/{MAX_RECOVERY}")

    selected = state.get("selected_ride") or {}
    failed_provider = selected.get("provider", "unknown")

    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["recovery"] = {
        "attempt": recovery_attempts,
        "failed_provider": failed_provider,
        "action": "searching_alternatives",
    }

    remaining = [r for r in state.get("ride_options", []) if r.get("provider") != failed_provider]
    state = {**state, "agent_outputs": agent_outputs, "ride_options": remaining,
             "selected_ride": None, "booking_status": None, "ride_status": None, "should_recover": False}

    if recovery_attempts >= MAX_RECOVERY:
        state = {**state, "error": "Max recovery attempts reached", "trip_complete": True}
        state = add_log(state, "RecoveryAgent", "Max recovery attempts reached — aborting")
    else:
        state = add_log(state, "RecoveryAgent", f"Excluded {failed_provider}, will re-search remaining providers")

    state = set_timestamp(state, "recovery_end")
    return state
