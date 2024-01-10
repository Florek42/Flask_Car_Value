from website import base
from flask_login import UserMixin
from sqlalchemy.sql import func 

class model(base.Model):
    id = base.Column(base.Integer, primery_key = True)
    text = base.Column(base.String(50))
    date = base.Column(base.DateTime(timezone=True), default=func.now())
    user_id = base.Column(base.Integer, base.ForeignKey('user.id'))

class user(base.Model, UserMixin):
    id = base.Column(base.Integer, primery_key = True)
    email = base.Column(base.String(25), unique = True)
    password = base.Column(base.String(25))
    nickname = base.Column(base.String(25))


