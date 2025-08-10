from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    secret_key = os.urandom(24)
    app.secret_key = os.environ.get("SECRET_KEY", secret_key)

    app.config['SECRET_KEY'] = secret_key

    from . import routes
    app.register_blueprint(routes.bp)

    return app