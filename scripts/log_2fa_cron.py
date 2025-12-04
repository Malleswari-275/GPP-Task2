#!/usr/bin/env python3
import sys
import os
from datetime import datetime

# Add /app to Python path so totp_utils can be imported
sys.path.append('/app')

try:
    from totp_utils import generate_totp
except ImportError:
    print(f"{datetime.utcnow()} - ERROR: Could not import totp_utils")
    raise

# 1. Read hex seed from persistent storage
seed_file = "/data/seed.txt"
try:
    with open(seed_file, "r") as f:
        hex_seed = f.read().strip()
except FileNotFoundError:
    hex_seed = None
    print(f"{datetime.utcnow()} - ERROR: Seed file not found")

# 2. Generate TOTP code if seed exists
if hex_seed:
    try:
        code = generate_totp(hex_seed)

        # 3. Get current UTC timestamp
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # 4. Output formatted line
        print(f"{timestamp} - 2FA Code: {code}")
    except Exception as e:
        print(f"{datetime.utcnow()} - ERROR: {e}")
