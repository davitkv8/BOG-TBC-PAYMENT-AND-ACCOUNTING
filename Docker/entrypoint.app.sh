#!/bin/sh

# wait for Postgres to start
wait-for-it -t 30 -s banking__postgresql:5432

python startup_script.py

uvicorn app:app --host 0.0.0.0 --port 8000
