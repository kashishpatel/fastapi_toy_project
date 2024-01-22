from fastapi import FastAPI
import uvicorn
from app.main import app as rest_api
from app.api.graphql.main import app as graphql_api

# Create an instance of the FastAPI project-level app
project_app = FastAPI()

# Include individual FastAPI apps (app1...) into the project-level app
project_app.include_router(rest_api)
project_app.include_router(graphql_api)

# Additional project-wide configurations
# ...

if __name__ == "__main__":
    # Run the ASGI server for the project-level app
    uvicorn.run(project_app, host="0.0.0.0", port=8000)