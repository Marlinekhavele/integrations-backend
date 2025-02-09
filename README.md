## Integrations Backend Service
- A robust backend service implementation featuring two main components: a Data Provider for handling booking/cancellation events and a Dashboard Service for hotel booking analytics. Built with FastAPI, this service follows clean architecture principles with a repository pattern.
### Features
#### Data Provider Service
- Event management for hotel bookings and cancellations
- Comprehensive filtering capabilities
- Data validation and sanitization
- RESTful API endpoints for event creation and retrieval
#### Dashboard Service
- Real-time booking statistics and insights
- Flexible time-based aggregation (daily/monthly)
- Customizable reporting periods
### Tech Stack
- FastAPI - API framework
- Poetry - Dependency management
- Alembic - Database migrations
- Docker & Docker Compose - Containerization
- PostgreSQL - Database
- Pytest - Testing framework
### Installation & Local setup
- Ensure you have Docker or Podman, Poetry, and Python (3.13) installed.
1. Clone the Repository
```bash
git clone https://github.com/Marlinekhavele/integrations-backend
cd integrations-backend
 ```
2. Set up PostgreSQL database:
  # Ubuntu
   - sudo apt-get update
   - sudo apt-get install postgresql postgresql-contrib
   # macOS
   - brew install postgresql

  # Switch to the PostgreSQL user
  - sudo -i -u postgres
  # linux
  - psql

  # Open PostgreSQL shell Mac
  -  brew services start postgres
  -  psql postgres

  # Create a new user
  - CREATE USER postgres WITH PASSWORD 'password';

  # Create the database
  - CREATE DATABASE ticket_assignment;

  # Grant privileges to the user
  - GRANT ALL PRIVILEGES ON DATABASE ticket_assignment TO postgres;

  # Exit the PostgreSQL shell
   - \q

3. Create and activate a virtual environment: [install pyenv](https://github.com/pyenv/pyenv#installation)

4. Install Dependencies
- poetry install

5. Run Migrations

- poetry run alembic upgrade head

6. Run the Application
- poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

7. Running with Docker
- docker-compose up --build

8. API Documentation
add here
After running the application, access the API docs at:
- OpenAPI: http://localhost:8000/docs

Testing
- poetry run pytest



