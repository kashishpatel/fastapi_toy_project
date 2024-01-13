from fastapi import FastAPI
import uvicorn
from app.main import app as app1

# Create an instance of the FastAPI project-level app
project_app = FastAPI()

# Include individual FastAPI apps (app1 and app2) into the project-level app
project_app.include_router(app1)

# Additional project-wide configurations
# ...

if __name__ == "__main__":
    # Run the ASGI server for the project-level app
    uvicorn.run(project_app, host="0.0.0.0", port=8000)