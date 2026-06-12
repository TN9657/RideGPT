from state.graph_state import add_log, set_timestamp
from tools.provider_simulators import get_all_providers


def search_agent(state: dict) -> dict:
    state = set_timestamp(state, "search_start")
    state = add_log(state, "SearchAgent", f"Searching rides from '{state.get('pickup')}' to '{state.get('destination')}'")

    raw_rides = get_all_providers(state.get("pickup"), state.get("destination"), state.get("vehicle_preference"))
    ride_options = [r for r in raw_rides if r.get("availability")]

    if not ride_options:
        state = add_log(state, "SearchAgent", "No available rides found")
        state = {**state, "error": "No rides available"}
    else:
        agent_outputs = dict(state.get("agent_outputs", {}))
        agent_outputs["search"] = ride_options
        state = {**state, "ride_options": ride_options, "agent_outputs": agent_outputs}
        state = add_log(state, "SearchAgent", f"Found {len(ride_options)} available rides: {[r['provider'] for r in ride_options]}")

    state = set_timestamp(state, "search_end")
    return state
