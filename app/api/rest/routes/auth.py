from fastapi import APIRouter
from app.utils.jwt_auth import create_jwt_token
from ...schemas.auth import UserLogin

router = APIRouter(tags=["JWT Token"])

# Endpoint to generate a JWT token for authentication
@router.post("/token")
async def login_for_access_token(user: UserLogin):
    # In a real application, you would verify the user's credentials here.
    # For this example, we'll assume a valid user.
    
    # Create a JWT token
    token_data = {"sub": user.username}
    token = create_jwt_token(token_data)
    
    return {"access_token": token, "token_type": "bearer"}
