FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    curl


ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/
EXPOSE 8000
EXPOSE 587
WORKDIR /app/src/
CMD ["uvicorn", "config.asgi:application", "--reload", "--host", "0.0.0.0", "--port", "8000"]
