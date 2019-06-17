import os
import sys
from flask import Flask
from flask_json import FlaskJSON, json_response
from livereload import Server

sys.path.append(os.getcwd())

from config import config # noqa


def create_app(config_name):
    app = Flask(__name__)
    FlaskJSON(app)
    app.config.from_object(config[config_name])

    @app.route('/', methods=['GET'])
    def index():
        return json_response(result='yes')

    return app


app = create_app(os.getenv('APP_SETTINGS'))
print(os.getenv('APP_SETTINGS'))
server = Server(app.wsgi_app)


if __name__ == '__main__':
    server.serve(port=7000, host='0.0.0.0')
