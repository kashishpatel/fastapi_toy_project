#!/bin/bash

# Initialize Alembic
alembic init alembic

# Create initial migration
alembic revision -m "Initial Migration" --rev-id=001

# Copy existing migrations
cp -r app/migrations/* alembic/versions

# Apply migrations using Alembic
alembic upgrade head

# Start the FastAPI application
python main.py