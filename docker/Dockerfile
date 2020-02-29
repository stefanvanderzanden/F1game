FROM python:3.7

# Define environment variable
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

RUN apt update && apt install -y gettext libgettextpo-dev postgresql-client

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

RUN pipenv lock
RUN pipenv install --system --dev --ignore-pipfile

COPY . .
