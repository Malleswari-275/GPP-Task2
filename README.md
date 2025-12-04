Secure PKI + TOTP Authentication Microservice
Overview

This project implements a secure, containerized authentication microservice using RSA 4096-bit PKI and TOTP-based 2FA. It demonstrates enterprise-grade security practices with asymmetric encryption, digital signatures, persistent storage, and cron-based TOTP generation.

Features

Cryptography: RSA-OAEP for encryption/decryption, RSA-PSS for signing

TOTP 2FA: 6-digit codes, 30s window, ±1 period tolerance

REST API Endpoints:

POST /decrypt-seed → decrypts seed

GET /generate-2fa → generates current TOTP

POST /verify-2fa → verifies TOTP

Dockerized: Multi-stage build, UTC timezone, cron job logging

Persistent Storage: /data/seed.txt and /cron/last_code.txt survive container restarts

Access API at http://localhost:8080

Security Notes

Private keys never exposed outside container

Input validation and error handling enforced

UTC timestamps used for all logs and TOTP generation
