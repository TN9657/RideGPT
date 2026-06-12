# RideGPT — Quick Project Overview

### What is RideGPT?

RideGPT is a **Multi-Agent AI Ride Orchestration Platform** that simulates how an intelligent assistant would search, compare, book, monitor, and recover rides automatically.

Instead of directly using Uber/Ola APIs, the system uses **mock ride providers** (Uber Simulator, Ola Simulator, Rapido Simulator) so you can focus on learning:

* Agentic AI
* LangGraph
* Backend Development
* System Design
* Database Design
* Full-Stack Development
* Recovery Workflows

---

# User Journey

### Step 1: User Opens Dashboard

User sees:

```text
Ride Booking Page
```

Fields:

* Pickup Location
* Destination
* Budget
* Vehicle Type
* Priority

Example:

```text
Pickup: Thane

Destination: Mumbai Airport

Budget: ₹500

Vehicle: Sedan
```

User clicks:

```text
[ Find Best Ride ]
```

---

# Step 2: Request Reaches Backend

Frontend:

```text
React
```

sends request to:

```text
FastAPI
```

Example:

```json
{
  "pickup":"Thane",
  "destination":"Mumbai Airport",
  "budget":500
}
```

---

# Step 3: LangGraph Starts Workflow

LangGraph creates a new trip state.

Example:

```text
Trip ID: T001

Status: Processing
```

Stored inside:

```text
Global State
```

---

# Step 4: Search Agent Starts

Agent:

```text
SearchAgent
```

Task:

```text
Find available rides
```

Queries:

```text
Uber Simulator

Ola Simulator

Rapido Simulator
```

Returns:

```text
Uber   ₹450  ETA 10m

Ola    ₹420  ETA 12m

Rapido ₹390  ETA 15m
```

---

# Step 5: Search Results Stored

System stores:

```text
ride_options
```

inside:

```text
LangGraph State

MySQL
```

---

# Step 6: Comparison Agent Starts

Agent:

```text
ComparisonAgent
```

Task:

```text
Compare all rides
```

Evaluation:

```text
Price

ETA

Rating

Reliability
```

Scoring Example:

```text
Rapido  92

Ola     88

Uber    85
```

---

# Step 7: Best Ride Selected

Selected:

```text
Rapido
```

Reason:

```text
Lowest price
Best overall score
```

---

# Step 8: Booking Agent Starts

Agent:

```text
BookingAgent
```

Task:

```text
Create booking
```

Creates:

```text
Ride ID: R1001
```

Status:

```text
BOOKED
```

Stores:

```text
Booking Table
```

---

# Step 9: Dashboard Updates

User sees:

```text
✓ Search Complete

✓ Comparison Complete

✓ Booking Complete

Current Ride:

Rapido

₹390

ETA: 15m
```

---

# Step 10: Monitoring Agent Starts

Agent:

```text
MonitoringAgent
```

Task:

```text
Monitor ride
```

Checks:

* Ride Status
* Driver Status
* Cancellation Status
* ETA

Every:

```text
30 seconds
```

---

# Step 11A: Normal Scenario

If ride remains active:

```text
Ride Started

Ride In Progress

Ride Completed
```

Status:

```text
SUCCESS
```

Trip saved to history.

---

# Step 11B: Cancellation Scenario

Example:

```text
Driver Cancelled Ride
```

MonitoringAgent detects:

```text
Cancellation
```

Triggers:

```text
RecoveryAgent
```

---

# Step 12: Recovery Agent Starts

Task:

```text
Recover ride
```

Actions:

```text
Search again

Compare again

Select next best ride
```

---

# Step 13: Rebooking

New result:

```text
Ola ₹420
```

Agent:

```text
BookingAgent
```

runs again.

New ride:

```text
BOOKED
```

---

# Step 14: User Notification

Dashboard shows:

```text
⚠ Ride Cancelled

Recovery Started

Alternative Ride Found

Ride Rebooked Successfully
```

---

# Step 15: Trip Completion

Status:

```text
COMPLETED
```

Stored in:

```text
Trips Table

History Table

Analytics Table
```

---

# Analytics Generation

AnalyticsAgent calculates:

```text
Average Fare

Average ETA

Provider Usage

Cancellation Rate

Recovery Rate

Trip Success Rate
```

Displays charts on dashboard.

---

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
MonitoringAgent                                                      |
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
RecoveryAgent ───────────────────────────────────────────────────────|
 
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

# What the Recruiter Sees

```text
✓ User books ride

✓ AI searches providers

✓ AI compares options

✓ AI books ride

✓ AI monitors ride

✓ AI detects cancellation

✓ AI automatically recovers

✓ AI rebooks ride

✓ Dashboard visualizes everything
```

That's what makes RideGPT a strong project: it's not just a booking app; it's a **full-stack multi-agent AI system with autonomous decision-making, monitoring, and recovery workflows.**
