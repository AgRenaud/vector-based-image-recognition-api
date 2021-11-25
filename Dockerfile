# `python-base` sets up all our shared environment variables
FROM python:3.8.10-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install -y python3-opencv

# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base

RUN apt update && apt install --no-install-recommends -y \
    curl \
    build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev --no-root

# `production` image used for runtime
FROM python-base as production
ENV FASTAPI_ENV=production
ENV APP_PATH="/app"
ENV CONFIG_PATH="$APP_PATH/default_config.yaml"
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY ./app /app/
CMD ["uvicorn", "app.api:create_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
EXPOSE 8000
