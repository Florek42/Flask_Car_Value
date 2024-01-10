from website import base
from flask_login import UserMixin

class user(base.Model, UserMixin):
    id = base.Column(base.Integer, primery_key = True)
    email = base.Column(base.String(25), unique = True)
    password = base.Column(base.String(25))
    nickname = base.Column(base.String(25))


