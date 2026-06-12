import uuid
from sqlalchemy.orm import Session
from workflow_graph.workflow import ride_graph
from state.graph_state import default_state
from models.db_models import Trip, Booking, RideHistory, AgentLog
from schemas.schemas import RideRequestSchema, TripResponseSchema


def _persist(trip_id: str, req: RideRequestSchema, fs: dict, db: Session) -> None:
    selected = fs.get("selected_ride")
    db.add(Trip(
        id=trip_id,
        user_id=req.user_id,
        pickup=req.pickup,
        destination=req.destination,
        vehicle_preference=req.vehicle_preference,
        budget=req.budget,
        priority=req.priority,
        status=fs.get("ride_status") or "unknown",
    ))
    if selected and fs.get("booking_status") == "confirmed":
        db.add(Booking(
            id=str(uuid.uuid4()),
            trip_id=trip_id,
            provider=selected["provider"],
            price=selected["price"],
            eta=selected["eta"],
            vehicle=selected["vehicle"],
            driver_name=selected.get("driver_name"),
            driver_phone=selected.get("driver_phone"),
            status=fs["booking_status"],
        ))
    db.add(RideHistory(
        id=str(uuid.uuid4()),
        trip_id=trip_id,
        provider=selected["provider"] if selected else None,
        final_price=selected["price"] if selected else None,
        final_eta=selected["eta"] if selected else None,
        ride_status=fs.get("ride_status"),
        cancellation_count=len(fs.get("cancellation_history", [])),
        recovery_attempts=fs.get("recovery_attempts", 0),
        agent_outputs=fs.get("agent_outputs", {}),
    ))
    for log in fs.get("logs", []):
        db.add(AgentLog(id=str(uuid.uuid4()), trip_id=trip_id, agent_name="workflow", message=log))
    db.commit()


def run_ride_workflow(req: RideRequestSchema, db: Session) -> TripResponseSchema:
    trip_id = str(uuid.uuid4())

    initial = default_state({
        "trip_id": trip_id,
        "user_id": req.user_id,
        "pickup": req.pickup,
        "destination": req.destination,
        "vehicle_preference": req.vehicle_preference,
        "budget": req.budget,
        "priority": req.priority or "balanced",
    })

    fs: dict = ride_graph.invoke(initial)

    try:
        if db is not None:
            _persist(trip_id, req, fs, db)
    except Exception as e:
        print(f"[WARNING] DB persist failed (DB may be offline): {e}")

    selected = fs.get("selected_ride")
    return TripResponseSchema(
        trip_id=fs["trip_id"],
        user_id=fs["user_id"],
        pickup=fs["pickup"],
        destination=fs["destination"],
        booking_status=fs.get("booking_status"),
        ride_status=fs.get("ride_status"),
        selected_ride=selected,
        ride_options=fs.get("ride_options", []),
        logs=fs.get("logs", []),
        events=fs.get("events", []),
        agent_outputs=fs.get("agent_outputs", {}),
        notifications=fs.get("notifications", []),
        recovery_attempts=fs.get("recovery_attempts", 0),
        trip_complete=fs.get("trip_complete", False),
        error=fs.get("error"),
    )
