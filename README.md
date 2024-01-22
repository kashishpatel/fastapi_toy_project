# FastAPI Toy Project

Created to learn Python's FastAPI web framework, this project contains a simple CRUD APIs centered around an `Item` object.
A simple PostgreSQL database is also created with a `items` table through an initial database migration using Alembic.

# RESTful API
Once the Docker container is running, you can view and test out the API endpoints at `localhost:8000/docs`.

Auth is done via JWT. A token can be retrieved by making a GET request to the `/api/v1/token`.

There are also API endpoints that retrieve data from an another API using `httpx`, transform it, and return it to the user as an exercise in connecting to external resources. There is also in-memory caching in place to prevent unnecessary requests to the API.

# GraphQL API
An GraphQL API with the same operations as the RESTful API for the `Item` object is also created and running. GraphiQL to test this API is available at `/graphql`.

# Setup
This project contains a Dockerfile and is runnable using `docker-compose up --build`.

