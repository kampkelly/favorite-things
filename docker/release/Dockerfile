# api configuration
FROM python:3 as api

WORKDIR /app/server

COPY server /app/server

COPY .env /app/server

# client configuration
FROM node:10 as client

WORKDIR /app/client

COPY client/package.json /src/client

COPY .env /app/client

COPY client /app/client

# ubuntu base image configuration
FROM ubuntu:latest as ubuntu_base

WORKDIR /src/

COPY --from=api /app/server /src/app/server

COPY --from=client /app/client /src/app/client

COPY .env /src/app

COPY /docker/release/dependencies.sh /src

COPY /docker/release/nginx.conf /src

RUN chmod +x ./dependencies.sh

RUN ./dependencies.sh
