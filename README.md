# FastAPI Toy Project

Created to learn Python's FastAPI web framework, this project contains a simple CRUD API centered around an `Item` object.

Auth is done via JWT. A token can be retrieved by making a GET request to the `/api/v1/token`.

A simple PostgreSQL database is also created with a `items` table through an initial database migration using Alembic.

There are also API endpoints that retrieve data from an external API using `httpx`, transform it, and return it to the user as an exercise of connecting to external resources.

Contains a Dockerfile and is runnable using `docker-compose up --build`.

Once the Docker container is running, you can view and test out the API endpoints at `localhost:8000/docs`.
