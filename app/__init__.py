from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'manage.login'

from views import index_views, admin_views
from models import user_models
