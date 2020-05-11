from flask import Flask
from flask_cors import CORS

from app.routes import root


def create_app():

    appBuilder = Flask(__name__)
    appBuilder.register_blueprint(root)
    CORS(appBuilder)

    return appBuilder


app = create_app()
