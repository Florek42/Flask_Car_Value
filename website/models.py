from website import base
from flask_login import UserMixin
from sqlalchemy.sql import func 

class Info(base.Model):
    id = base.Column(base.Integer, primary_key=True)
    data = base.Column(base.String(25))
    date = base.Column(base.DateTime(timezone=True), default=func.now())
    user_id = base.Column(base.Integer, base.ForeignKey('user.id'))

class User(base.Model, UserMixin):
    id = base.Column(base.Integer, primary_key=True)
    email = base.Column(base.String(25), unique=True)
    password = base.Column(base.String(25))
    first_name = base.Column(base.String(25))
    info = base.relationship('Info')


    


