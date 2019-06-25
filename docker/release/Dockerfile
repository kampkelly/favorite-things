FROM node:10 as client

WORKDIR /src/client

COPY client/package.json /src/client

COPY .env /src/client

COPY client /src/client

RUN npm install && npm run build

FROM nginx as nginx


COPY --from=client /src/client/dist /src/client

COPY docker/nginx.conf /etc/nginx/nginx.conf

FROM python:3 as api

WORKDIR /src/server

COPY server/requirements.txt /src/server

COPY .env /src/server

COPY server /src/server

RUN pip install -r requirements.txt

RUN ls -al
