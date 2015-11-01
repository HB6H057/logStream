from wtforms import ValidationError
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo, Email

from flask.ext.wtf import Form

from app.core.models import User, Category
from app import db


class RegForm(Form):
    """
    Register form
    """
    username = StringField('username',
                           validators=[DataRequired(), Length(1, 64),
                                       Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Username must have ony letters,\
                                              numbers, dotd or underscores')])
    password = PasswordField('password',
                             validators=[DataRequired(), EqualTo('password2',
                             message='Password must match.')])
    password2 = PasswordField('comfirm password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    nickname = StringField('nickname', validators=[DataRequired()])

    def reg_user(self):
        """
        Register a new user use form.data.
        """
        self.validate_email(self.email)
        self.validate_username(self.username)
        user = User(email=self.email.data, username=self.username.data,
                    password=self.password.data, nickname=self.nickname.data)
        db.session.add(user)
        db.session.commit()
        return user

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email alreay registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('usernae alreay registered.')
