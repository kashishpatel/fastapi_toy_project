import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.config.settings import settings

# Secret key for JWT encoding/decoding
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
TOKEN_EXPIRATION = timedelta(hours=1)

# Function to generate a JWT token
def create_jwt_token(username: str):
    expiration = datetime.utcnow() + TOKEN_EXPIRATION
    data = {"sub": username, "exp": expiration}
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Function to verify the JWT token
def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
