from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    @property
    def password(self):
        raise AttributeError('GlaDOS:"What are you doing?\
                              (password is not a readable attribute)"')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        "GlaDOS: \"(User: %s)That was genuinely mildly impressive.\""
