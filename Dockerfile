FROM python:3.14.0a3-alpine3.20

ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

ENV MQTT_BROKER_PASSWORD ""
LABEL authors="tomer.klein@gmail.com"

RUN apt -yqq update && \
    apt -yqq install fping && \
    rm -rf /var/lib/apt/lists/*
    
RUN pip install --upgrade pip --no-cache-dir && \
    pip install --upgrade setuptools --no-cache-dir

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /app/config

COPY app /app

WORKDIR /app

ENTRYPOINT python app.py