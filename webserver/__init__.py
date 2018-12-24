import os
from flask import Flask

from app import api_bp
from Model import db
import settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.APP_SETTINGS)

    app.register_blueprint(api_bp, url_prefix="/api")

    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

