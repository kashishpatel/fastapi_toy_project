# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client and other necessary packages
RUN apt-get update && apt-get install -y postgresql-client

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Set the entrypoint script as the entry point for the container
ENTRYPOINT ["/app/entrypoint.sh"]
