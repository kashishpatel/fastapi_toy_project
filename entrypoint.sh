#!/bin/bash
alembic init alembic

alembic revision -m "Initial Migration" --rev-id=001

cp -r app/migrations/* alembic/versions

# Apply migrations using Alembic
alembic upgrade head

# Start your FastAPI application
python main.py