import uuid, random
from state.graph_state import add_log, set_timestamp


def _attempt_booking() -> bool:
    return random.random() > 0.1  # 90% success


def booking_agent(state: dict) -> dict:
    state = set_timestamp(state, "booking_start")
    selected = state.get("selected_ride", {})
    state = add_log(state, "BookingAgent", f"Attempting to book {selected.get('provider')}")

    for attempt in range(1, 4):
        if _attempt_booking():
            trip_id = state.get("trip_id") or str(uuid.uuid4())
            agent_outputs = dict(state.get("agent_outputs", {}))
            agent_outputs["booking"] = {
                "booking_id": trip_id,
                "provider": selected.get("provider"),
                "status": "confirmed",
                "attempt": attempt,
            }
            state = {**state, "trip_id": trip_id, "booking_status": "confirmed",
                     "ride_status": "active", "agent_outputs": agent_outputs}
            state = add_log(state, "BookingAgent", f"Booking confirmed on attempt {attempt} — ID: {trip_id}")
            break
        state = add_log(state, "BookingAgent", f"Attempt {attempt} failed, retrying...")
    else:
        state = {**state, "booking_status": "failed", "error": "Booking failed after 3 attempts"}
        state = add_log(state, "BookingAgent", "All booking attempts failed")

    state = set_timestamp(state, "booking_end")
    return state
