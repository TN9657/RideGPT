# RideGPT — Autonomous Ride Orchestration Platform

An agentic AI platform that autonomously searches, compares, books, monitors, and recovers rides across Uber, Ola, and Rapido simulators using LangGraph multi-agent workflows.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + Tailwind CSS + React Query |
| Backend | FastAPI + Pydantic + SQLAlchemy |
| Database | MySQL |
| Cache | Redis |
| AI Agents | LangGraph + LangChain |
| LLM Primary | Groq (Llama 3 / DeepSeek / Qwen) |
| LLM Fallback | Google Gemini Free Tier |

---

## Agent Flow

```
User Request → SearchAgent → ComparisonAgent → BookingAgent → MonitoringAgent
                  ▲                                                    │
                  │                                           Cancelled?
                  └──────────── RecoveryAgent ◄───────────────────────┘
                                      │
                             AnalyticsAgent → MemoryAgent → NotificationAgent → END
```

---

## Project Structure

```
ride-gpt/
├── backend/
│   ├── agents/          # SearchAgent, ComparisonAgent, BookingAgent, MonitoringAgent, RecoveryAgent, support_agents
│   ├── tools/           # provider_simulators (Uber, Ola, Rapido)
│   ├── langgraph/       # LangGraph workflow
│   ├── state/           # GraphState (global agent state)
│   ├── models/          # SQLAlchemy DB models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── routes/          # FastAPI route handlers
│   ├── database/        # DB connection + session
│   ├── utils/           # LLM client (Groq + Gemini)
│   ├── main.py          # FastAPI app entry
│   ├── requirements.txt
│   └── .env
└── frontend/
    ├── src/
    │   ├── pages/       # Dashboard, BookRide, RideHistory, Analytics
    │   ├── components/  # Navbar, AgentStatusPanel, ActiveTripPanel, LogsPanel
    │   └── api/         # Axios API client
    └── vite.config.js
```

---

## Setup

### Backend

```bash
cd ride-gpt/backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
# Edit .env with your DB URL and API keys
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd ride-gpt/frontend
npm install
npm run dev
```

### Database

Create a MySQL database named `ridegpt`. Tables are auto-created on startup.

---

## Environment Variables

```
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/ridegpt
GROQ_API_KEY=your_groq_key        # Free at console.groq.com
GEMINI_API_KEY=your_gemini_key    # Free at aistudio.google.com
GROQ_MODEL=llama3-8b-8192
REDIS_URL=redis://localhost:6379
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/ride/request` | Trigger full agent workflow |
| GET | `/api/trips/{user_id}` | Get user's ride history |
| GET | `/api/trip/{trip_id}/logs` | Get agent logs for a trip |
| GET | `/api/analytics/{user_id}` | Get analytics summary |
| GET | `/health` | Health check |

---

## Agents

| Agent | Responsibility |
|---|---|
| SearchAgent | Queries all 3 provider simulators |
| ComparisonAgent | Scores rides (40% reliability, 30% price, 20% ETA, 10% rating) |
| BookingAgent | Books ride with 3-attempt exponential backoff |
| MonitoringAgent | Monitors ride status, detects cancellation |
| RecoveryAgent | Handles cancellation, excludes failed provider, triggers re-search |
| MemoryAgent | Tracks user preferences (provider, vehicle, destination) |
| NotificationAgent | Generates in-app notifications for all ride events |
| AnalyticsAgent | Records trip metrics and outcomes |
