from collections import Counter
from state.graph_state import add_log, set_timestamp


def memory_agent(state: dict) -> dict:
    state = set_timestamp(state, "memory_start")
    prefs = dict(state.get("user_preferences", {}))
    selected = state.get("selected_ride")

    if selected:
        providers = prefs.get("providers", []) + [selected["provider"]]
        prefs["preferred_provider"] = Counter(providers).most_common(1)[0][0]
        prefs["providers"] = providers[-20:]

        vehicles = prefs.get("vehicles", []) + [selected["vehicle"]]
        prefs["preferred_vehicle"] = Counter(vehicles).most_common(1)[0][0]
        prefs["vehicles"] = vehicles[-20:]

    if state.get("destination"):
        destinations = prefs.get("destinations", []) + [state["destination"]]
        prefs["frequent_destination"] = Counter(destinations).most_common(1)[0][0]
        prefs["destinations"] = destinations[-20:]

    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["memory"] = prefs
    state = {**state, "user_preferences": prefs, "agent_outputs": agent_outputs}
    state = add_log(state, "MemoryAgent", f"Updated preferences: preferred={prefs.get('preferred_provider')}")
    state = set_timestamp(state, "memory_end")
    return state


def notification_agent(state: dict) -> dict:
    state = set_timestamp(state, "notification_start")
    selected = state.get("selected_ride") or {}
    notifications = []

    if state.get("booking_status") == "confirmed":
        notifications.append({"type": "BOOKING_CONFIRMED", "message": f"Ride booked with {selected.get('provider')}! Driver: {selected.get('driver_name')}"})
    if state.get("ride_status") == "active":
        notifications.append({"type": "DRIVER_ASSIGNED", "message": f"Driver {selected.get('driver_name')} is on the way. ETA {selected.get('eta')} min."})
    if state.get("ride_status") == "cancelled":
        notifications.append({"type": "RIDE_CANCELLED", "message": f"Ride with {selected.get('provider', 'provider')} was cancelled. Searching alternatives..."})
    if state.get("trip_complete") and not state.get("error"):
        notifications.append({"type": "RIDE_COMPLETED", "message": "Your ride is complete. Have a great day!"})
    if state.get("should_recover"):
        notifications.append({"type": "RIDE_REBOOKED", "message": "We are rebooking your ride automatically."})

    all_notifications = list(state.get("notifications", [])) + notifications
    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["notifications"] = notifications
    state = {**state, "notifications": all_notifications, "agent_outputs": agent_outputs}
    state = add_log(state, "NotificationAgent", f"Sent {len(notifications)} notification(s)")
    state = set_timestamp(state, "notification_end")
    return state


def analytics_agent(state: dict) -> dict:
    state = set_timestamp(state, "analytics_start")
    selected = state.get("selected_ride")
    analytics = {
        "total_cancellations": len(state.get("cancellation_history", [])),
        "recovery_attempts": state.get("recovery_attempts", 0),
        "selected_provider": selected["provider"] if selected else None,
        "final_price": selected["price"] if selected else None,
        "final_eta": selected["eta"] if selected else None,
        "trip_complete": state.get("trip_complete"),
        "providers_searched": list({r["provider"] for r in state.get("ride_options", [])}),
    }
    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["analytics"] = analytics
    state = {**state, "agent_outputs": agent_outputs}
    state = add_log(state, "AnalyticsAgent", f"Analytics recorded — provider: {analytics['selected_provider']}, price: ₹{analytics['final_price']}")
    state = set_timestamp(state, "analytics_end")
    return state
