You are a Senior AI Architect, Principal Software Engineer, System Designer, Product Architect, and LangGraph Expert.

Your task is to design and build a production-quality portfolio project called:

RideGPT - Autonomous Multi-Agent Ride Orchestration Platform

This project must be designed as a real-world Agentic AI application suitable for:

- Software Engineering Interviews
- AI Engineering Interviews
- Full Stack Developer Roles
- Backend Engineering Roles
- Portfolio Demonstrations
- Final Year Computer Science Projects

The system must demonstrate:

- Agentic AI
- Multi-Agent Systems
- Workflow Orchestration
- State Management
- Event Driven Architecture
- Failure Recovery
- Autonomous Decision Making
- LLM Integration
- Tool Calling
- Frontend + Backend Architecture

The project should be completely free to build and run.

No paid APIs.

No paid infrastructure.

No proprietary services.

Use only free and open-source technologies.

====================================================

PROJECT OVERVIEW

Build an autonomous ride orchestration platform that simulates ride providers such as:

- Uber
- Ola
- Rapido

The system should Automate and allow users to:

1. Automatically Request a ride
2. Automatically Compare available rides
3. Automatically Select optimal rides 
4. Automatically Book rides
5. Monitor rides
6. Automatically Handle cancellations
7. Automatically rebook rides
8. Maintain ride history

The system should use multiple AI agents coordinated through LangGraph.

====================================================

TECH STACK

Frontend:

- React
- Vite
- Tailwind CSS
- React Query
- Axios

Backend:

- FastAPI
- Pydantic
- SQLAlchemy

Database:

- MySQL

Caching:

- Redis

AI Layer:

- LangGraph
- LangChain

Free LLM Providers:

Primary:
Groq

Fallback:
Google Gemini Free Tier

Supported Models:

- DeepSeek
- Llama 3
- Qwen

Deployment Ready:

Frontend:
Vercel

Backend:
Render

Database:
Neon MySQL

====================================================

PROJECT STRUCTURE

Generate complete folder structure.

Example:

ride-gpt/

frontend/

backend/

agents/

tools/

services/

database/

schemas/

models/

routes/

langgraph/

state/

utils/

tests/

docs/

README.md

====================================================

SYSTEM DESIGN

Design the system using:

Microservice-Inspired Modular Architecture

Layers:

Presentation Layer

Business Logic Layer

Agent Layer

Tool Layer

Data Layer

Storage Layer

Monitoring Layer

Notification Layer

====================================================


# Complete Agent Flow

```text
User
 │
 ▼
Ride Request
 │
 ▼
SearchAgent ⟵───────────────────────────────────────────────────────|
 │                                                                   |
 ▼                                                                   |
ComparisonAgent                                                      |
 │                                                                   |
 ▼                                                                   |
BookingAgent                                                         |
 │                                                                   |
 ▼                                                                   |
MonitoringAgent                                                     🔼
 │                                                                   |
 ├──────────────► Ride Completed                                     |
 │                      │                                            |
 │                      ▼                                            |
 │                    END                                            |
 │                                                                   |
 ▼                                                                   |
Ride Cancelled                                                       |
 │                                                                   |
 ▼                                                                   |
RecoveryAgent ──────────────────────────────────────────────────────►|
 
```

---

# Technology Flow

```text
React Dashboard
        │
        ▼
FastAPI APIs
        │
        ▼
LangGraph Workflow
        │
 ┌──────┼──────┐
 │      │      │
 ▼      ▼      ▼

Uber   Ola   Rapido
Mock   Mock  Mock

        │
        ▼

      MySQL

        │
        ▼

Analytics & Logs
```


====================================================

LANGGRAPH ARCHITECTURE

Create the complete LangGraph workflow.

Agents:

SearchAgent

ComparisonAgent

BookingAgent

MonitoringAgent

RecoveryAgent

MemoryAgent

NotificationAgent

AnalyticsAgent

Graph Flow:

User Request

↓

SearchAgent

↓

ComparisonAgent

↓

BookingAgent

↓

MonitoringAgent

↓

IF CANCELLED

↓

RecoveryAgent

↓

SearchAgent

↓

ComparisonAgent

↓

BookingAgent

↓

MonitoringAgent

↓

Trip Complete

====================================================


STATE DESIGN

Create global graph state.

Store:

trip_id

user_id

pickup

destination

ride_options

selected_ride

booking_status

ride_status

cancellation_history

events

logs

timestamps

agent_outputs

recovery_attempts

user_preferences

====================================================

DATABASE DESIGN

Generate SQLAlchemy models.

Tables:

Users

Trips

Bookings

RideProviders

RideHistory

Notifications

AgentLogs

RecoveryEvents

UserPreferences

Analytics

Include:

Relationships

Indexes

Constraints

====================================================

MOCK PROVIDER SYSTEM

Create realistic provider simulators.

Provider Simulators:

UberSimulator

OlaSimulator

RapidoSimulator

Each simulator should generate:

Price

ETA

Driver Rating

Vehicle Type

Availability

Cancellation Probability

Reliability Score

Surge Multiplier

Response Example:

{
  "provider": "Uber",
  "price": 420,
  "eta": 8,
  "rating": 4.8,
  "vehicle": "Sedan",
  "availability": true,
  "reliability": 95
}

====================================================

SEARCH AGENT

Responsibilities:

Search all ride providers.

Gather:

Price

ETA

Vehicle

Rating

Availability

Reliability

Cancellation Risk

Output structured JSON.

====================================================

COMPARISON AGENT

Responsibilities:

Rank rides.

Scoring Formula:

40% Reliability

30% Price

20% ETA

10% Rating

Reject:

Rating < 4

ETA > 25

Reliability < 70

Output:

Selected Ride

Score

Reasoning

Alternatives

====================================================

BOOKING AGENT

Responsibilities:

Validate ride.

Create booking.

Generate booking ID.

Persist booking.

Update state.

Handle booking failures.

Retry:

3 times

Exponential Backoff

====================================================

MONITORING AGENT

Responsibilities:

Monitor active rides.

Run continuously.

Track:

Status

ETA

Driver Availability

Cancellation

Traffic Delay

Trigger RecoveryAgent when required.

====================================================

RECOVERY AGENT

Responsibilities:

Handle failures.

Scenarios:

Driver Cancelled

Provider Failure

Excessive Delay

Booking Failure

Recovery Process:

Analyze Failure

Search Alternatives

Re-rank Providers

Auto-Rebook

Update Logs

Notify User

====================================================

MEMORY AGENT

Responsibilities:

Learn user behavior.

Track:

Preferred Providers

Preferred Vehicle Types

Travel Times

Frequent Destinations

Cancellation Patterns

Budget Preferences

Store preferences.

Influence future recommendations.

====================================================

NOTIFICATION AGENT

Generate notifications for:

Booking Confirmed

Driver Assigned

Ride Started

Ride Cancelled

Ride Rebooked

Ride Completed

Notification Channels:

In-App

Email Simulation

SMS Simulation

====================================================

ANALYTICS AGENT

Generate metrics:

Average Fare

Average ETA

Cancellation Rate

Provider Success Rate

Most Used Provider

Monthly Trips

Trip Completion Rate

====================================================

FRONTEND REQUIREMENTS

Dashboard Layout

Pages:

Dashboard

Book Ride

Ride History

Agent Logs

Analytics

Settings

====================================================

BOOK RIDE PAGE

Inputs:

Pickup

Destination

Vehicle Type

Budget

Priority

Button:

Find Ride

====================================================

LIVE AGENT EXECUTION PANEL

Display:

SearchAgent Running

ComparisonAgent Running

BookingAgent Running

MonitoringAgent Running

RecoveryAgent Running

Display timestamps.

Display execution logs.

====================================================

ACTIVE TRIP DASHBOARD

Display:

Current Provider

Price

ETA

Driver

Vehicle

Ride Status

Booking Status

====================================================

RECOVERY VISUALIZATION

Display:

Cancellation Event

Recovery Triggered

Alternative Search

Rebooking Success

====================================================

ANALYTICS PAGE

Charts:

Trip Count

Provider Usage

Fare Trends

Cancellation Trends

Success Rates

Use:

Recharts

====================================================

API DESIGN

Generate FastAPI endpoints.

Examples:

POST /rides/search

POST /rides/book

GET /rides/{id}

POST /rides/recover

GET /analytics

GET /logs

GET /history

====================================================

TESTING

Generate:

Unit Tests

Integration Tests

Agent Tests

API Tests

Workflow Tests

====================================================

LOGGING

Implement:

Structured Logging

Agent Execution Logs

System Logs

Recovery Logs

Error Logs

====================================================

SECURITY

Implement:

Input Validation

Request Validation

Rate Limiting

Error Handling

Secure Configuration

Environment Variables

====================================================

DOCUMENTATION

Generate:

README

Architecture Diagram

Setup Guide

API Documentation

Database Diagram

LangGraph Diagram

====================================================

CODE QUALITY

Requirements:

Type Hints

Docstrings

Clean Architecture

SOLID Principles

Modular Code

Reusable Components

Production-Level Structure

====================================================

OUTPUT REQUIREMENT

Generate:

1. Complete folder structure.

2. System architecture diagram.

3. Database schema.

4. LangGraph workflow.

5. Backend implementation.

6. Frontend implementation.

7. Agent implementation.

8. API implementation.

9. Deployment instructions.

10. README.

11. Step-by-step development roadmap.

Do not provide pseudo-code.

Generate real executable code.

Generate project incrementally in logical phases.

Explain all design decisions before writing code.