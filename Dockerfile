# ============================
# Stage 1: Builder
# ============================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================
# Stage 2: Runtime
# ============================
FROM python:3.11-slim

ENV TZ=UTC
WORKDIR /app

# Install cron + timezone support
RUN apt-get update && apt-get install -y cron tzdata && \
    rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

# Copy application code
COPY . .

# Install Python dependencies again in runtime
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Set permissions for cron file
RUN chmod 0644 cron/totp-cron
RUN crontab cron/totp-cron

# Create volume directories
RUN mkdir -p /data /cron

EXPOSE 8080

CMD ["./start.sh"]
