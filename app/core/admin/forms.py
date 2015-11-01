from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

from flask.ext.wtf import Form

from app.core.models import User
from app import db


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember', default=False)

    def get_user(self):
        user = db.session.query(User).filter_by(username=self.username.data).first()
        self.validate_user(user)
        return user

    # why not override validate_username????
    def validate_user(self, user):
        if user is None:
            raise validators.ValidationError('Invalid user')
        if not user.verify_password(self.password.data):
            raise validators.ValidationError('Invalid password')
