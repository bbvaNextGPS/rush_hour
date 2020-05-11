from flask import Flask
from flask_cors import CORS

from app.routes import root


def create_app():

    appBuilder = Flask(__name__)
    appBuilder.register_blueprint(root)
    CORS(appBuilder, resources={r"/api/*": {"origins": "*"}})

    return appBuilder


app = create_app()
