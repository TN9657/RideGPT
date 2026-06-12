from typing import Any, Dict, List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class RideRequestSchema(BaseModel):
    user_id: str
    pickup: str
    destination: str
    vehicle_preference: Optional[str] = None
    budget: Optional[float] = None
    priority: Optional[str] = "balanced"


class RideOptionSchema(BaseModel):
    provider: str
    price: float
    eta: int
    rating: float
    vehicle: str
    availability: bool
    reliability: float
    surge_multiplier: float


class TripResponseSchema(BaseModel):
    trip_id: str
    user_id: str
    pickup: str
    destination: str
    booking_status: Optional[str]
    ride_status: Optional[str]
    selected_ride: Optional[RideOptionSchema]
    ride_options: List[RideOptionSchema]
    logs: List[str]
    events: List[Dict[str, Any]]
    agent_outputs: Dict[str, Any]
    notifications: List[Dict[str, Any]]
    recovery_attempts: int
    trip_complete: bool
    error: Optional[str]


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class UserSchema(UserCreateSchema):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


class AnalyticsSchema(BaseModel):
    total_trips: int
    total_cancellations: int
    avg_fare: Optional[float]
    avg_eta: Optional[float]
    most_used_provider: Optional[str]
    trip_completion_rate: Optional[float]
    providers_breakdown: Optional[Dict[str, int]]
