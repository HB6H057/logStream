from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    nickname      = db.Column(db.String(64))
    username      = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

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
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
