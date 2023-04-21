FROM python:3.8.12-slim-buster

# needed for postgre lib
RUN apt update && apt -y install libpq-dev gcc

ADD Docker/requirements.txt .

RUN pip install -r requirements.txt

ADD . /app/

RUN chmod 777 /app

WORKDIR /app/

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1