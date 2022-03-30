FROM python:3.9-alpine

COPY project /app

RUN ls -tralh /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

RUN pip list

ENV FLASK_APP=routes.py

CMD flask run --host=0.0.0.0
