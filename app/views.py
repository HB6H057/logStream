import pdb

from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, Post, Tag
from app.models import post_new
from app.forms import LoginForm, RegistrationForm, PostForm


@app.route('/', methods=['GET', 'POST'])
def index():
    title    = 'logStream'
    subtitle = 'The cake is a lie!!'
    form     = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated() is False:
            flash('no login no BB')
            return redirect(url_for('index'))
        tags = map(lambda x:x.strip(' '), form.tags.data.split(','))
        tags = list(set(tags))
        if '' in tags:
            tags.remove('')

        post_new(body=form.body.data, user=current_user._get_current_object(), tagnames=tags)

        pdb.set_trace()
        flash('post a new post success')
        return redirect(url_for('index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title=title, subtitle=subtitle,
                            form=form, posts=posts)


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

@app.route('/tag/<tag_slug>')
def tags(tag_slug):
    tag = Tag.query.filter(Tag.slug == tag_slug).first()
    return render_template('tag.html', tag=tag)
