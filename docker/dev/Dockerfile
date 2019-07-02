# ubuntu base image configuration
FROM ubuntu:latest as ubuntu_base

WORKDIR /src/

COPY server /src/app/server

COPY client /src/app/client

COPY .env /src/app

COPY .env /src/app/server

COPY client/.env /src/app/client

COPY /docker/dev/dependencies.sh /src

RUN chmod +x ./dependencies.sh

RUN ./dependencies.sh
