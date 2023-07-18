FROM python:3.10-slim as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base as builder-base
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    vim \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.5.1
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} && \
    chmod a+x /opt/poetry/bin/poetry

WORKDIR $PYSETUP_PATH
COPY ./pyproject.toml ./

RUN poetry install --no-root --verbose 

WORKDIR /app
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]