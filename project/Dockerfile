# pull official base image
FROM python:3.12.4-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --reload"]
