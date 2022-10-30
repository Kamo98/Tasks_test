FROM python:alpine

WORKDIR /app

ADD requirements.txt requirements.txt

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY . .