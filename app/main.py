import os
from flask import Flask
from app.controller.score_controller import controller_blueprint
from app.service.measure_factory import MeasureModule
from flask_injector import FlaskInjector


def create_app():
    measure_app = Flask(__name__)

    FlaskInjector(app=measure_app, modules=[MeasureModule()])

    # Register the controller blueprint to the Flask app
    measure_app.register_blueprint(controller_blueprint)

    return measure_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True if os.environ.get("FLASK_ENV") == "development" else False)
