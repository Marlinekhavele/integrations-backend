Integrations Backend Service
Project Overview
This project implements two services:

Data Provider - Handles booking and cancellation events.
Dashboard Service - Provides insights into bookings per hotel.
The project follows a repository pattern, uses FastAPI, manages migrations with Alembic, and utilizes Poetry for dependency management.

Features
Data Provider
Provides booking and cancellation events for a hotel.
Exposes RESTful APIs:
GET /events - Fetches filtered booking/cancellation events.
POST /events - Creates a new event with validation.
Dashboard Service
Provides statistical insights into hotel bookings.
Exposes RESTful APIs:
GET /dashboard - Fetches booking statistics (monthly/daily).


Tech Stack
FastAPI - API framework
Poetry - Dependency management
Alembic - Database migrations
Docker & Docker Compose - Containerization
PostgreSQL - Database
Pytest - Testing framework


Installation & Setup
Pre-requisites
Ensure you have Docker, Poetry, and Python (>=3.8) installed.

Clone the Repository
git clone <repository_url>
cd integrations-backend

Install Dependencies
poetry install


Run Migrations

poetry run alembic upgrade head

Run the Application
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


Running with Docker
docker-compose up --build

API Documentation
After running the application, access the API docs at:

OpenAPI: http://localhost:8000/docs

Testing
poetry run pytest



