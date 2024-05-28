FROM python:3.12-slim

COPY ./zscaler.crt /usr/local/share/ca-certificates/zscaler.crt
RUN update-ca-certificates

ENV REQUESTS_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt
ENV POETRY_VIRTUALENVS_CREATE=false

# Create a non-root user (UGNAME means user and group name)
ARG USER_UID=1000
ARG GROUP_GID=1000
ARG UGNAME=example_backend


# Install the system and Python packages
RUN set -eux \
    && apt-get update \
    && apt-get install -y \
    sed openssl libssl-dev ca-certificates libffi-dev gcc \
    libc6-dev make musl-dev python3-dev python3-freetype vim \
    && apt-get clean \
    \
    && pip install --upgrade pip setuptools wheel poetry>=1.8.1 \
    && rm -rf /root/.cache/pip \
    \
    && addgroup --system --gid ${GROUP_GID} ${UGNAME} \
    && adduser --system --disabled-password --home /home/${UGNAME} --uid ${USER_UID} --ingroup ${UGNAME} ${UGNAME}


WORKDIR /app

COPY poetry.lock pyproject.toml /code/

COPY . /app/

RUN poetry install

HEALTHCHECK CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000

# Run the app with non-root user
USER ${UGNAME}
ENTRYPOINT ["make", "run"]
