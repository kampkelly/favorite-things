
FROM node:10 as client

WORKDIR /src/client

COPY client/package.json /src/client

COPY .env /src/client

COPY client /src/client

RUN npm install

FROM python:3 as api

WORKDIR /src/server

COPY server/requirements.txt /src/server

RUN pip install -r requirements.txt

COPY .env /src/server
