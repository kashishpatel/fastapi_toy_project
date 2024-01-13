from sqlalchemy.orm import Session
from app.db.database import SessionLocal

# Function to get a database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()