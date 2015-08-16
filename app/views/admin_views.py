from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm


@app.route('/manage/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('welcome ' + form.username.data)
        return redirect('/')

    return render_template('login.html', form=form)


@app.route('/manage/register', methods=['GET', 'POST'])
def register():
    Form = RegistrationForm()
    if Form.validate_on_submit():
        user = User(email=Form.email.data, username=Form.username.data,
                    password=Form.password.data, nickname=Form.nickname.data)
        db.session.add(user)
        flash('You can login Now !')
        return redirect(url_for('/'))
    return render_template('register.html', form=Form)
