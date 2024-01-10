from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

base = SQLAlchemy()
DB_NAME = "baza.db" 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Forek42'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    base.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Info
    crt_db(app)

    return app


def crt_db(app):
        if not path.exists('website/' + DB_NAME):
              base.create_all(app=app)
              