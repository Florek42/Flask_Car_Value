from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base = SQLAlchemy()
DB_NAME = "baza.db" 






def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Forek42'
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
