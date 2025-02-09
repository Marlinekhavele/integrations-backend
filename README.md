## Integrations Backend Service
- A robust backend service implementation featuring two main services: a ```Data Provider``` for handling booking/cancellation events and a ```Dashboard Service``` for hotel booking analytics.
- Built with FastAPI, this service follows clean architecture principles with a repository pattern.
### Features:
 ##### Data Provider Service
 - Event management for hotel bookings and cancellations
 - Comprehensive filtering capabilities
 - Data validation and sanitization
 - RESTful API endpoints for event creation and retrieval
 ##### Dashboard Service
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
```shell
  # Ubuntu
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   # macOS
   brew install postgresql

  # Switch to the PostgreSQL user
  sudo -i -u postgres
  # linux
  psql

  # Open PostgreSQL shell Mac
  brew services start postgres
  psql postgres

  # Create a new user
  CREATE USER postgres WITH PASSWORD 'password';

  # Create the database
  CREATE DATABASE ticket_assignment;

  # Grant privileges to the user
  GRANT ALL PRIVILEGES ON DATABASE ticket_assignment TO postgres;

  # Exit the PostgreSQL shell
    \q
```
3. Create and activate a virtual environment: [install pyenv](https://github.com/pyenv/pyenv#installation)

4. Install Dependencies
```bash
poetry install

 ```

5. Run Migrations
```bash
poetry run alembic upgrade head
 ```
6. Run the Application
```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

 ```
7. Running with Docker
```bash
docker-compose up --build
 ```

8. API Documentation
Data Provider:
```GET /events``` - Retrieve events with optional filters
```shell

[
  {
    "hotel_id": 3000,
    "id": 2,
    "rpg_status": 1,
    "night_of_stay": "2025-02-09",
    "timestamp": "2025-02-09T16:59:31.586000+00:00",
    "room_id": 100
  }
]
```
```POST /events``` - Create new event
```shell
{
  "hotel_id": 3000,
  "id": 2,
  "rpg_status": 1,
  "night_of_stay": "2025-02-09",
  "timestamp": "2025-02-09T16:59:31.586000+00:00",
  "room_id": 100
}
```
Dashboard:
```GET /dashboard/{hotel_id}``` - Get booking statistics with customizable periods
```shell
{
  "hotel_id": 3000,
  "period": "day",
  "csv_data": {},
  "event_data": [
    {
      "hotel_id": 3000,
      "id": 2,
      "rpg_status": 1,
      "night_of_stay": "2025-02-09",
      "room_id": 100
    }
  ]
}
```
9. After running the application, access the API docs at:
```bash
OpenAPI: http://localhost:8000/docs

 ```
10. Testing
```bash
poetry run pytest

 ```
11. Linting
```bash
poetry run pre-commit run --all-files
 ```



Docker failed me teribly during testing
I opted on working on separate terminals when i was doing my final testing
use local setup  run each service separately

this command helped me with the issues i was have on dashboard service
export PYTHONPATH=$PYTHONPATH:/Users/marline/Desktop/integrations-backend/dashboard_service/src