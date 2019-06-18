import os
from flask import Flask
from flask_json import FlaskJSON, json_response
from flask_bcrypt import Bcrypt

from config import config


def create_app(config_name):
    app = Flask(__name__)
    FlaskJSON(app)
    app.config.from_object(config[config_name])

    @app.route('/', methods=['GET'])
    def index():
        return json_response(result='yes')

    return app


app = create_app(os.getenv('APP_SETTINGS'))

bcrypt = Bcrypt(app)
