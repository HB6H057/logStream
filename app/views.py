from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm


@app.route('/')
def index():
    title    = 'logStream'
    subtitle = 'The cake is a lie!!'
    return render_template('index.html', title=title, subtitle=subtitle)


@app.route('/manage/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            flash('welcome ' + form.username.data)
            return redirect(url_for('index'))
        flash('Invalid username and password')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/manage/register', methods=['GET', 'POST'])
def register():
    Form = RegistrationForm()
    if Form.validate_on_submit():
        user = User(email=Form.email.data, username=Form.username.data,
                    password=Form.password.data, nickname=Form.nickname.data)
        db.session.add(user)
        db.session.commit()
        flash('You can login Now !')
        return redirect(url_for('index'))
    return render_template('register.html', form=Form)

@app.route('/manage/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))
