# Build image that have python dependencies through pipenv
FROM python:3.7-alpine as qctrl_app_build
# set work directory
WORKDIR /app
# The following commands install dependencies needed for psycopq2
# Based on https://gist.github.com/LondonAppDev/58bcfd9b6267a60beda660aa91df6ddd
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
# Install dependencies
RUN pip install pipenv
# Delete Cached dependencies for building psycopq2
RUN apk del .tmp-build-deps
# Copy Pipfile and Pipfile.lock
COPY ./app/Pipfile* ./
RUN  pipenv install --system --deploy --ignore-pipfile

#---------------------------------------------------------------------------------------------------------------------

# Build image that contains django project
FROM qctrl_app_build as qctrl_app
# This environment setting force python stdout and stderr to flush without buffering
ENV PYTHONUNBUFFERED 1
# This environment settings instructs python not to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1
# Setting directory with app files exists
WORKDIR /app
# Copy All app files to working directory
COPY ./app .
# Adds user so the container won't have root privildges
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN groupadd -r app && useradd --no-log-init -r -g app app
USER app

