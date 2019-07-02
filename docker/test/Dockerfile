# ubuntu base image configuration
FROM ubuntu:latest as ubuntu_base

WORKDIR /src/

COPY server /src/app/server

COPY .env /src/app

COPY .env /src/app/server

COPY /docker/test/dependencies.sh /src

COPY /docker/tests.sh /src

RUN chmod +x ./dependencies.sh

RUN chmod +x ./tests.sh

RUN ./dependencies.sh
