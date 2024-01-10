from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
#from .models import User, Info

base = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Forek42'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    base.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

  
    
    with app.app_context():
        base.create_all()

    return app

def crt_db(app):
    if not path.exists('instance/' + DB_NAME):
        base.create_all(app=app)
       
