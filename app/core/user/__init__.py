from flask import Blueprint

user = Blueprint('auth', __name__)

from . import views
