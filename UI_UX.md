

FRONTEND REQUIREMENTS

The project MUST include a modern professional frontend dashboard.

The frontend is NOT optional.

The frontend should be designed as a real-world SaaS platform that allows users, recruiters, and interviewers to visually observe the behavior of all AI agents in real time.

The dashboard should prioritize:

- Visibility
- Transparency
- Real-Time Updates
- Agent Monitoring
- Analytics
- User Experience

====================================================

FRONTEND TECHNOLOGY STACK

Framework:

React

Build Tool:

Vite

Styling:

Tailwind CSS

HTTP Client:

Axios

State Management:

React Query

Charts:

Recharts

Icons:

Lucide React

Routing:

React Router DOM

====================================================

FRONTEND OBJECTIVES

The frontend must provide complete visibility into:

1. Ride Requests
2. Agent Execution
3. Agent Decisions
4. Booking Status
5. Ride Monitoring
6. Recovery Events
7. Ride History
8. Analytics

The frontend should function as an AI Control Center.

====================================================

FRONTEND DESIGN PHILOSOPHY

The dashboard should resemble:

- AI Operations Center
- Mission Control Dashboard
- Enterprise SaaS Product

The design should feel modern, clean, responsive, and professional.

Use:

- Cards
- Tables
- Status Indicators
- Progress Timelines
- Analytics Charts
- Activity Feeds

====================================================

REQUIRED PAGES

Generate all frontend pages.

Pages:

Dashboard

Ride Booking

Live Agent Execution

Agent Logs

Active Trips

Ride History

Recovery Center

Analytics

Settings

====================================================

DASHBOARD PAGE

Purpose:

Provide system overview.

Display:

Total Trips

Active Trips

Completed Trips

Cancellation Rate

Recovery Success Rate

Average ETA

Average Fare

Most Used Provider

Agent Health Status

Recent Activities

====================================================

RIDE BOOKING PAGE

Purpose:

Allow users to request rides.

Inputs:

Pickup Location

Destination

Vehicle Type

Budget

Priority

Preferred Provider

Travel Time

Button:

Search Best Ride

Display Results:

Provider

Price

ETA

Rating

Reliability

Book Ride Button

====================================================

LIVE AGENT EXECUTION PAGE

Purpose:

Visualize all agent activities in real time.

Display:

SearchAgent

ComparisonAgent

BookingAgent

MonitoringAgent

RecoveryAgent

MemoryAgent

NotificationAgent

AnalyticsAgent

For each agent display:

Current Status

Execution Time

Last Action

Result

Timestamp

====================================================

AGENT WORKFLOW VISUALIZATION

Create a visual workflow panel.

Example:

SearchAgent
      ↓
ComparisonAgent
      ↓
BookingAgent
      ↓
MonitoringAgent
      ↓
RecoveryAgent

Display:

Waiting

Running

Success

Failed

Recovered

====================================================

AGENT LOGS PAGE

Display:

Timestamp

Agent Name

Action

Result

Execution Duration

Status

Support:

Search

Filter

Pagination

Sorting

====================================================

ACTIVE TRIPS PAGE

Display:

Trip ID

Pickup

Destination

Current Provider

Price

Driver

Vehicle

ETA

Booking Status

Ride Status

Recovery Count

====================================================

RIDE HISTORY PAGE

Display:

Past Trips

Provider Used

Total Fare

Trip Duration

Trip Status

Recovery Events

Booking Timestamp

====================================================

RECOVERY CENTER PAGE

Purpose:

Show failure handling.

Display:

Cancellation Events

Booking Failures

Recovery Attempts

Rebooking Events

Recovery Success Rate

Show complete recovery timeline.

Example:

Ride Booked

↓

Driver Cancelled

↓

Recovery Agent Triggered

↓

Alternative Search

↓

New Ride Selected

↓

Ride Rebooked

====================================================

ANALYTICS PAGE

Display:

Trips Per Day

Trips Per Week

Trips Per Month

Average Fare

Provider Usage

Cancellation Trends

Recovery Trends

Ride Success Rate

Most Used Vehicle Type

Most Used Provider

Use:

Recharts

Generate:

Line Charts

Bar Charts

Pie Charts

Area Charts

====================================================

SETTINGS PAGE

Allow user to configure:

Preferred Provider

Preferred Vehicle Type

Budget Limit

Notification Preferences

Travel Preferences

AI Decision Preferences

====================================================

REAL-TIME UPDATES

The frontend must support live updates.

Use:

WebSockets

or

Server-Sent Events

Display updates immediately when:

Agent Starts

Agent Completes

Ride Books

Ride Cancels

Recovery Starts

Recovery Completes

====================================================

STATUS INDICATORS

Use visual indicators.

Running:

Yellow

Completed:

Green

Failed:

Red

Waiting:

Gray

Recovered:

Blue

====================================================

NOTIFICATION CENTER

Display:

Booking Success

Booking Failure

Ride Cancelled

Ride Rebooked

Trip Completed

System Alerts

====================================================

FRONTEND FOLDER STRUCTURE

Generate complete frontend structure.

Example:

frontend/

src/

components/

pages/

hooks/

services/

contexts/

layouts/

routes/

types/

utils/

assets/

====================================================

REUSABLE COMPONENTS

Generate reusable components.

Examples:

Navbar

Sidebar

AgentCard

TripCard

AnalyticsCard

StatusBadge

Timeline

LogTable

NotificationPanel

RecoveryTimeline

Charts

====================================================

RESPONSIVE DESIGN

The dashboard must work on:

Desktop

Tablet

Mobile

====================================================

USER EXPERIENCE

The dashboard should be impressive enough that a recruiter can understand the entire AI workflow within 2 minutes of opening the application.

The frontend must clearly demonstrate:

- Agentic AI
- Multi-Agent Systems
- Autonomous Decision Making
- Failure Recovery
- Workflow Orchestration

without requiring explanation from the developer.

====================================================

OUTPUT REQUIREMENT

Generate:

Complete React Architecture

Component Hierarchy

Page Layouts

Routing Structure

State Management Strategy

API Integration Strategy

WebSocket Integration

Reusable Components

Tailwind Design System

Professional Dashboard UI