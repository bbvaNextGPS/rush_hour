from flask import Flask

from app.routes import root


def create_app():

    appBuilder = Flask(__name__)
    appBuilder.register_blueprint(root)

    return appBuilder


app = create_app()
