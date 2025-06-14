from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/")
def root():
    return {"message": "Log Monitoring API"}

@app.get("/logs")
def get_logs():
    keys = r.keys("log:*")
    logs = []
    for key in sorted(keys, reverse=True):
        log = r.get(key)
        if log:
            logs.append(json.loads(log))
    return logs

@app.get("/metrics")
def log_metrics():
    keys = r.keys("log:*")
    level_count = {}
    for key in keys:
        log = json.loads(r.get(key))
        level = log.get("level", "UNKNOWN")
        level_count[level] = level_count.get(level, 0) + 1
    return level_count

@app.get("/alerts")
def trigger_alert():
    return {"status": "Alert triggered!", "example": "CRITICAL log detected"}