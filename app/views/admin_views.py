from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/manage/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('welcome ' + form.username.data)
        return redirect('/')

    return render_template('login.html', form=form)
