from datetime import datetime
from sqlalchemy import (
    Column, String, Float, Integer, Boolean, DateTime, ForeignKey, JSON, Text, Index
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    trips = relationship("Trip", back_populates="user")
    preferences = relationship("UserPreference", back_populates="user", uselist=False)


class Trip(Base):
    __tablename__ = "trips"
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    pickup = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    vehicle_preference = Column(String(50))
    budget = Column(Float)
    priority = Column(String(20), default="balanced")
    status = Column(String(30), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="trips")
    bookings = relationship("Booking", back_populates="trip")
    history = relationship("RideHistory", back_populates="trip")
    __table_args__ = (Index("ix_trips_user_status", "user_id", "status"),)


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(String(36), primary_key=True)
    trip_id = Column(String(36), ForeignKey("trips.id"), nullable=False, index=True)
    provider = Column(String(50), nullable=False)
    price = Column(Float)
    eta = Column(Integer)
    vehicle = Column(String(50))
    driver_name = Column(String(100))
    driver_phone = Column(String(20))
    status = Column(String(30), default="pending")
    attempt_number = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    trip = relationship("Trip", back_populates="bookings")


class RideProvider(Base):
    __tablename__ = "ride_providers"
    id = Column(String(36), primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    base_price = Column(Float)
    reliability_score = Column(Float)
    cancellation_rate = Column(Float)
    is_active = Column(Boolean, default=True)


class RideHistory(Base):
    __tablename__ = "ride_history"
    id = Column(String(36), primary_key=True)
    trip_id = Column(String(36), ForeignKey("trips.id"), nullable=False, index=True)
    provider = Column(String(50))
    final_price = Column(Float)
    final_eta = Column(Integer)
    ride_status = Column(String(30))
    cancellation_count = Column(Integer, default=0)
    recovery_attempts = Column(Integer, default=0)
    agent_outputs = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    trip = relationship("Trip", back_populates="history")


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), index=True)
    trip_id = Column(String(36))
    type = Column(String(50))
    message = Column(Text)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class AgentLog(Base):
    __tablename__ = "agent_logs"
    id = Column(String(36), primary_key=True)
    trip_id = Column(String(36), index=True)
    agent_name = Column(String(50))
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


class RecoveryEvent(Base):
    __tablename__ = "recovery_events"
    id = Column(String(36), primary_key=True)
    trip_id = Column(String(36), ForeignKey("trips.id"), index=True)
    failed_provider = Column(String(50))
    attempt_number = Column(Integer)
    new_provider = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)


class UserPreference(Base):
    __tablename__ = "user_preferences"
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), unique=True, index=True)
    preferred_provider = Column(String(50))
    preferred_vehicle = Column(String(50))
    budget_preference = Column(Float)
    priority = Column(String(20), default="balanced")
    raw_data = Column(JSON)
    user = relationship("User", back_populates="preferences")


class Analytics(Base):
    __tablename__ = "analytics"
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), index=True)
    period = Column(String(20))
    total_trips = Column(Integer, default=0)
    total_cancellations = Column(Integer, default=0)
    avg_fare = Column(Float)
    avg_eta = Column(Float)
    most_used_provider = Column(String(50))
    trip_completion_rate = Column(Float)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
