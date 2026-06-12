from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import Counter
from database.connection import get_db
from schemas.schemas import RideRequestSchema, TripResponseSchema, AnalyticsSchema
from services.ride_service import run_ride_workflow
from models.db_models import Trip, RideHistory, AgentLog

router = APIRouter(prefix="/api", tags=["rides"])


@router.post("/ride/request", response_model=TripResponseSchema)
def request_ride(req: RideRequestSchema, db: Session = Depends(get_db)):
    return run_ride_workflow(req, db)


@router.get("/trips/{user_id}")
def get_user_trips(user_id: str, db: Session = Depends(get_db)):
    if db is None:
        return []
    return db.query(Trip).filter(Trip.user_id == user_id).order_by(Trip.created_at.desc()).all()


@router.get("/trip/{trip_id}/logs")
def get_trip_logs(trip_id: str, db: Session = Depends(get_db)):
    if db is None:
        return []
    return db.query(AgentLog).filter(AgentLog.trip_id == trip_id).order_by(AgentLog.timestamp).all()


@router.get("/analytics/{user_id}", response_model=AnalyticsSchema)
def get_analytics(user_id: str, db: Session = Depends(get_db)):
    if db is None:
        return AnalyticsSchema(total_trips=0, total_cancellations=0, avg_fare=None, avg_eta=None,
                               most_used_provider=None, trip_completion_rate=None, providers_breakdown=None)
    histories = (
        db.query(RideHistory)
        .join(Trip, RideHistory.trip_id == Trip.id)
        .filter(Trip.user_id == user_id)
        .all()
    )
    if not histories:
        return AnalyticsSchema(total_trips=0, total_cancellations=0, avg_fare=None, avg_eta=None,
                               most_used_provider=None, trip_completion_rate=None, providers_breakdown=None)

    total = len(histories)
    completed = sum(1 for h in histories if h.ride_status == "completed")
    fares = [h.final_price for h in histories if h.final_price]
    etas = [h.final_eta for h in histories if h.final_eta]
    providers = [h.provider for h in histories if h.provider]

    return AnalyticsSchema(
        total_trips=total,
        total_cancellations=sum(1 for h in histories if h.ride_status == "cancelled"),
        avg_fare=round(sum(fares) / len(fares), 2) if fares else None,
        avg_eta=round(sum(etas) / len(etas), 2) if etas else None,
        most_used_provider=Counter(providers).most_common(1)[0][0] if providers else None,
        trip_completion_rate=round(completed / total * 100, 2) if total else None,
        providers_breakdown=dict(Counter(providers)),
    )
