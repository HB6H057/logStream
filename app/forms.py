from flask.ext.wtf import Form
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo, Email
from app.models import User


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember', default=False)
    submit   = SubmitField('Log In')

class RegistrationForm(Form):
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

    submit = SubmitField('register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email alreay registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('usernae alreay registered.')

class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')
