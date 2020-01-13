# Created by: Aymen Al-Quaiti
# For QCTRL Backend Challenge
# January 2020

# Dockerizes Django app with all required python dependencies


# Build image that have python dependencies through pipenv
FROM python:3.7-alpine as qctrl_app_build
# set work directory
WORKDIR /app

# add user
RUN adduser -D user
RUN chown -R user:user /app && chmod -R 755 /app
# The following commands install dependencies needed for psycopq2
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
# Install dependencies
RUN pip install pipenv
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
# Switch to non root user
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
USER user

