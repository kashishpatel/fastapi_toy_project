# FastAPI Toy Project

Created to learn Python's FastAPI web framework, this project contains a simple CRUD API centered around an `Item` object.

Auth is done via JWT. A token can be retrieved by making a GET request to the `/api/v1/token`.

A simple PostgresQL database is also created with a `items` table and an initial database migration use Alembic.

Contains a Dockerfile and is runnable using `docker-compose up --build`
