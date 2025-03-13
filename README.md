# Token API

## Overview
This is a FastAPI-based token authentication service using PostgreSQL as the database. The application is designed to run both locally and in a Dockerized environment.

## Running Locally
To run the application locally, follow these steps:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the PostgreSQL database using Docker:
   ```bash
   docker-compose up -d db
   ```

3. Start the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Running with Docker
To run the application in a Docker container, execute the following commands:

1. Stop and remove any existing containers and volumes:
   ```bash
   docker-compose down -v
   ```

2. Build the Docker images:
   ```bash
   docker-compose build
   ```

3. Start the containers:
   ```bash
   docker-compose up --force-recreate
   ```

## Running Tests
To run the test suite using Pytest with code coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

## Environment Variables
The application expects the following environment variables:

- `DATABASE_URL`: The connection string for the PostgreSQL database.
- `DOCKER_ENV`: Set to `1` when running in Docker to ensure correct database hostname resolution.

## Notes
- A Postman collection (`token_api.postman_collection.json`) is included in the repository to test API routes easily.
- The application automatically detects if it is running in a Docker container and adjusts the database hostname accordingly.
- The API documentation is available at `http://localhost:8000/docs` when the application is running.
- The database schema is automatically created using `Base.metadata.create_all()` during startup—no manual migrations required.
