# api configuration
FROM python:3 as api_test

WORKDIR /app/server

COPY server /app/server

COPY .env /app/server

# ubuntu base image configuration
FROM ubuntu:latest as ubuntu_base_test

WORKDIR /src/

COPY --from=api_test /app/server /src/app/server

COPY .env /src/app

COPY /docker/test/dependencies.sh /src

COPY /docker/tests.sh /src

RUN chmod +x ./dependencies.sh

RUN chmod +x ./tests.sh

RUN ./dependencies.sh
