import random
from state.graph_state import add_log, set_timestamp
from tools.provider_simulators import PROVIDER_MAP


def monitoring_agent(state: dict) -> dict:
    state = set_timestamp(state, "monitoring_start")
    selected = state.get("selected_ride", {})
    state = add_log(state, "MonitoringAgent", f"Monitoring ride with {selected.get('provider')}")

    provider_sim = PROVIDER_MAP.get(selected.get("provider"))
    status = provider_sim.simulate_ride_status() if provider_sim else random.choice(["active", "active", "completed", "cancelled"])

    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["monitoring"] = {"ride_status": status, "provider": selected.get("provider")}
    state = {**state, "ride_status": status, "agent_outputs": agent_outputs}

    if status == "cancelled":
        state = add_log(state, "MonitoringAgent", "Ride cancelled — triggering recovery")
        cancellation_history = list(state.get("cancellation_history", []))
        cancellation_history.append({
            "provider": selected.get("provider"),
            "trip_id": state.get("trip_id"),
            "timestamp": state.get("timestamps", {}).get("monitoring_start"),
        })
        state = {**state, "cancellation_history": cancellation_history, "should_recover": True}
    elif status == "completed":
        state = add_log(state, "MonitoringAgent", "Ride completed successfully")
        state = {**state, "trip_complete": True, "should_recover": False}
    else:
        state = add_log(state, "MonitoringAgent", "Ride is active and on track")
        state = {**state, "should_recover": False}

    state = set_timestamp(state, "monitoring_end")
    return state
