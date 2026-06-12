import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import init_db
from routes.ride_routes import router

app = FastAPI(title="RideGPT Agentic AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup():
    try:
        init_db()
    except Exception as e:
        print(f"[WARNING] DB init failed: {e}")
        print("[WARNING] Server starting without DB — fix DATABASE_URL in .env")


@app.get("/health")
def health():
    return {"status": "ok", "service": "RideGPT"}
