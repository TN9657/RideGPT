from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict
from datetime import datetime, timezone


class RideOption(TypedDict, total=False):
    provider: str
    price: float
    eta: int
    rating: float
    vehicle: str
    availability: bool
    reliability: float
    cancellation_probability: float
    surge_multiplier: float
    driver_name: Optional[str]
    driver_phone: Optional[str]


class GraphState(TypedDict, total=False):
    trip_id: Optional[str]
    user_id: Optional[str]
    pickup: Optional[str]
    destination: Optional[str]
    vehicle_preference: Optional[str]
    budget: Optional[float]
    priority: Optional[str]

    ride_options: List[RideOption]
    selected_ride: Optional[RideOption]
    booking_status: Optional[str]
    ride_status: Optional[str]

    cancellation_history: List[Dict[str, Any]]
    events: List[Dict[str, Any]]
    logs: List[str]
    timestamps: Dict[str, str]
    agent_outputs: Dict[str, Any]
    recovery_attempts: int
    user_preferences: Dict[str, Any]
    notifications: List[Dict[str, Any]]
    error: Optional[str]
    should_recover: bool
    trip_complete: bool


def add_log(state: dict, agent: str, message: str) -> dict:
    ts = datetime.now(timezone.utc).isoformat()
    logs = list(state.get("logs", []))
    events = list(state.get("events", []))
    logs.append(f"[{ts}] [{agent}] {message}")
    events.append({"timestamp": ts, "agent": agent, "message": message})
    return {**state, "logs": logs, "events": events}


def set_timestamp(state: dict, key: str) -> dict:
    timestamps = dict(state.get("timestamps", {}))
    timestamps[key] = datetime.now(timezone.utc).isoformat()
    return {**state, "timestamps": timestamps}


def default_state(overrides: dict = None) -> dict:
    base = {
        "trip_id": None,
        "user_id": None,
        "pickup": None,
        "destination": None,
        "vehicle_preference": None,
        "budget": None,
        "priority": "balanced",
        "ride_options": [],
        "selected_ride": None,
        "booking_status": None,
        "ride_status": None,
        "cancellation_history": [],
        "events": [],
        "logs": [],
        "timestamps": {},
        "agent_outputs": {},
        "recovery_attempts": 0,
        "user_preferences": {},
        "notifications": [],
        "error": None,
        "should_recover": False,
        "trip_complete": False,
    }
    if overrides:
        base.update(overrides)
    return base
