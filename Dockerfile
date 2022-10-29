FROM python:alpine

WORKDIR /app

ADD requirements.txt requirements.txt

RUN apk update
# install psycopg2 dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY . .

# CMD ["python", "create_db.py"]
# CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host=127.0.0.1", "--reload"]