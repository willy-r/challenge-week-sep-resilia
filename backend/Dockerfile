# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-buster

ARG APP_DIR=/app
ARG APP_PORT=5001

WORKDIR ${APP_DIR}

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE ${APP_PORT}

CMD [ "unvicorn", "app.main:app", "--port", "${APP_PORT}"]
