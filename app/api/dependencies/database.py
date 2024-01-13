import sys
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

# Function to get a database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        sys.stdout.write("Database connection established\n")
        yield db
    finally:
        db.close()