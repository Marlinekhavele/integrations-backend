SERVER_PORT=8000

.PHONY: install setup test lint serve start stop pyclean migrate-local docker-build docker-up docker-down

install:
	poetry install

setup: install
	pre-commit install

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest src/tests --cov=src --cov-report=term-missing --cov-report=xml:.test-reports/coverage.xml --junitxml=.test-reports/test-run.xml

lint:
	poetry run pre-commit run --all-files

serve:
	cd src && poetry run uvicorn app.main:app --reload --port ${SERVER_PORT}

start:
	podman-compose up -d hotel_management-db dashboard_service-db

start-services:
	podman-compose up -d hotel_management dashboard_service

stop:
	podman-compose down

pyclean:
	find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +

migrate-local:
	cd src && poetry run alembic upgrade head

docker-build:
	podman-compose build

docker-up:
	podman-compose up -d

docker-down:
	podman-compose down
