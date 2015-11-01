from flask.ext.login import login_user, logout_user, login_required, current_user
from flask import render_template, url_for, redirect, flash, request

from app import db
from app.core.models import User
from app.core.forms import LoginForm, RegForm

from . import user

# @user.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     Renders Sgin_In page
#     """
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user, form.remember.data)
#             flash('Welcome ' + form.username.data)
#             return redirect(url_for('index'))
#         flash('Invalid username or password')
#
#         return redirect(url_for('index'))
#     return render_template('login.html', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    """
    Renders Sign_Up  page
    """
    form = RegForm(request.form)
    if form.validate_on_submit():
        user = form.reg_user()
        return redirect(url_for('admin.index'))
    return render_template('register.html', form=form)

# @user.route('/logout')
# @login_required
# def logout():
#     """
#     Renders Logout page
#     """
#     logout_user()
#     flash('You have been logged out.')
#     return redirect(url_for('index'))
