The [specification](https://github.com/avito-tech/mi-trainee-task) for the task itself (Техническое задание).

# Fastapi-onetimesecret
A small API-service for generating one-time secrets

## Getting Started

### Dependencies
Python 3.10, FastAPI

### Installing
For local development I used [poetry](https://python-poetry.org/docs/). I'm aware that it may have some issues with Docker,
that's why for image making I used requirements.txt instead of pyproject.toml

To install this project on a local machine, clone this repo, and download all the dependencies by using `poetry install` command:

```
git clone
```

```
pip install poetry
```

```
poetry install
```

### Running the project locally
To run local server use:
```
poetry run uvicorn main:app --reload
```
Flag --reload will automatically reload the server if any changes occures in the app.
The app will run on http://127.0.0.1:8000 using uvicorn.

Alternative way to run the project is to use Docker which will run it using gunicorn. The command is:

```
docker-compose up
```
The app will be available  on http://127.0.0.1:7000