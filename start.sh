#!/bin/sh
# Start cron in foreground
cron -f &

# Start FastAPI server with uvicorn
uvicorn app:app --host 0.0.0.0 --port 8080
