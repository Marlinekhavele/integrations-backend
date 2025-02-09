FROM python:3.13

WORKDIR /app

# Install system dependencies and Poetry
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry and set up permissions for all required directories
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && useradd -m -u 1000 appuser \
    && mkdir -p /usr/local/lib/python3.13/site-packages \
    && mkdir -p /usr/local/include/python3.13 \
    && chown -R 1000:1000 /app \
    && chown -R 1000:1000 /usr/local/lib/python3.13 \
    && chown -R 1000:1000 /usr/local/include/python3.13 \
    && chown -R 1000:1000 /usr/local/bin \
    && chown -R 1000:1000 $POETRY_HOME \
    && chmod -R 755 /usr/local/bin

# Create a virtual environment directory that the non-root user can access
RUN mkdir -p /.venv && chown -R 1000:1000 /.venv

# Set Poetry to not create virtual environments
ENV POETRY_VIRTUALENVS_CREATE=false

# Switch to non-root user
USER appuser

# Copy project files with correct ownership
COPY --chown=appuser:appuser pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root --only main

# Copy the application code
COPY --chown=appuser:appuser ./src /app/src

ENV PYTHONPATH=/app

CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
