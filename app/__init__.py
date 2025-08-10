from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    secret_key = os.urandom(24)
    app.secret_key = os.environ.get("SECRET_KEY", secret_key)

    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app