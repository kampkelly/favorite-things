# Favorite Things Application

This repository is for the Favorite Things app consisting of a Python(Flask) backend and a Javascript(Vue) frontend. The application allows users to create an account and add their favorite things.

#### Technologies used:
- Python (Flask)
- SqlAlchemy
- MySQL
- Graphql
- Docker
- AWS

The main url for the app is: `
The following are the API routes available

### Setup and Installation

There are two ways to run the application:
- With Docker (Preferred)
- Directly through folder directories

#### Installation with Docker (Development)

1. First make sure Docker is installed on your machine.
2. Create a .env file in the project root directory using the sample from .env-sample.
3. Then in the project root directory, run `make build`.
4. You should then be able to access the application services via these urls:
 - `http://localhost:7000` for backend API
 - `http://localhost:8080` for frontend

To access the mysql database on your host system e.g for mac. Download TablePlus and connect with:
- host: `127.0.0.1`
- port: 3307
- username: MYSQL_USER
- password: MYSQL_PASSWORD

#### Installation with Docker (Hard Way)

##### For backend API
1. Create a .env file in the project root directory using the sample from .env-sample.
2. Install virtual env with `pip install virtualenv`.
3. Create a virtual environment with `virtualenv venv` and activate with `source .env` in the root directory.
4. Run `cd server` and run `pip install -r requirements.txt`.
5. Run `python server.py`.
6. Access the server on `http://localhost:7000`.

##### For frontend
1. Create a .env file in the project root directory using the sample from .env-sample if not already done from backend steps.
2. Run `cd client`.
3. Run `npm install`.
4. Run `npm run serve`.
5. Access the client on `http://localhost:8080`.



### Running Tests
#### With Docker
Run `make test`

#### Without Docker

1. Deactivate virtualenv with `deactivate`.
2. Go to project root directory and change `APP_SETTINGS` in .env to testing.
3. Run `source .env` and then `cd server`.
4. Run `pytest`