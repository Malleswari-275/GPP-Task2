#!/bin/bash

# Start cron daemon in the background
service cron start

# Start FastAPI with uvicorn
exec python -m uvicorn app:app --host 0.0.0.0 --port 8080
