FROM python:3.9

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry is in PATH
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
