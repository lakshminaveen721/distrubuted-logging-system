# 📊 Distributed Logging System

A real-time distributed logging system using Kafka, Redis, FastAPI, and WebSocket with Docker support.

## Features
- Simulates real-time logs using Kafka producers
- Stores logs in Redis with 1-hour expiry
- FastAPI for metrics and alert APIs
- WebSocket server for live updates to UI
- Docker Compose orchestration for all services

## How to Run

### Prerequisites
- Docker and Docker Compose installed

### Steps
1. Start the system:
```bash
docker-compose up --build
```

2. Services:
- FastAPI: http://localhost:8000
- WebSocket: ws://localhost:8080
- Kafka: localhost:9092
- Redis: localhost:6379

3. API endpoints:
- `/logs`: Get all recent logs
- `/metrics`: Count logs by severity
- `/alerts`: Simulate a log alert