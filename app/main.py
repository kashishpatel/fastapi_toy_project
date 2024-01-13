from fastapi import APIRouter
from app.api.routes.items import router as items_router
from app.api.routes.auth import router as auth_router
from app.config.settings import settings

# Create an instance of the FastAPI app for this module
app = APIRouter(prefix=settings.API_PREFIX)


# Define your API routes and handlers here
@app.get("/")
async def read_root():
    return {"message": "Hello from the app!"}

# Additional route definitions and configurations specific to this app
# ...
app.include_router(items_router)
app.include_router(auth_router)
