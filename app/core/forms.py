from flask.ext.wtf import Form
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo, Email
from app.core.models import User, Category

def categories():
    return Category.query.all()


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

# how to implement drop-down select lists
# http://wtforms.readthedocs.org/en/1.0.4/ext.html#wtforms.ext.sqlalchemy.fields.QuerySelectField
# http://stackoverflow.com/questions/17887519/how-to-use-queryselectfield-in-flask
# http://stackoverflow.com/questions/17307351/adding-fk-queryselectfield-to-wtform-generated-by-model-form
class PostForm(Form):
    title           = StringField('title')
    slug            = StringField('slug')
    body            = TextAreaField("What's on your mind?", validators=[DataRequired()])
    tags            = StringField('tags')
    add_category    = StringField('newCategory')
    select_category = QuerySelectField(query_factory=categories, get_label='name')
    submit = SubmitField('Submit')
