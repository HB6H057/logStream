from flask import Flask
from flask.ext.login import LoginManager

from app.core.models import db
from app.core.admin import create_admin

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    init_db(app)
    init_login(app)
    init_blueprint(app)
    create_admin(app, db)

    return app

def init_blueprint(app):
    from app.core.base import base
    app.register_blueprint(base)
    from app.core.auth import auth
    app.register_blueprint(auth)
    from app.core.api import api
    app.register_blueprint(api)

def init_db(app):
    db.init_app(app)
    db.app = app

def init_login(app):
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'manage.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.core.models import User
        return User.query.get(int(user_id))
