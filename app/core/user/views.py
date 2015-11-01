from flask import render_template, url_for, redirect, flash, request

from app import db
from app.core.models import User
from app.core.forms import LoginForm, RegForm

from . import auth

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Renders Sign_Up  page
    """
    form = RegForm(request.form)
    if form.validate_on_submit():
        user = form.reg_user()
        return redirect(url_for('admin.index'))
    return render_template('register.html', form=form)
