FROM python:3.11.0b3-slim

COPY project /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

#RUN pip list

ENV FLASK_APP=routes.py

CMD flask run --host=0.0.0.0
