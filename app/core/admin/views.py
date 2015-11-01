from wtforms import validators
from flask import redirect, url_for, request
from flask.ext.admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask.ext.admin import Admin
from flask.ext.admin import expose, helpers, AdminIndexView
from flask.ext.login import current_user, login_user, logout_user
from app.core.models import User, UserInfo, Tag, Post, Category

from .forms import LoginForm


class AdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login'))
        return super(AdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('auth.register') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout(self):
        logout_user()
        return redirect(url_for('.index'))

class AdminUserView(sqla.ModelView):
    column_display_pk = True
    can_create = False
    inline_models = (UserInfo,)
    column_list = ('id', 'username', 'nickname', 'email')

    # column_list = ('id', 'username', 'nickname', 'email', 'password')
    # column_labels = dict(id='Id', username='UserName', nickname='NickName', email='Mail', password='Password')
    # def is_accessible(self):
    #     return current_user.is_authenticated


class AdminPostView(sqla.ModelView):
    column_exclude_list = ['body']
    column_sortable_list = ('id', 'title', ('user', 'user.username'), 'timestamp', )
    column_list = ('id', 'title', 'user.username', 'timestamp', )

    column_filters = ('user',
                  'title',
                  'timestamp',
                  filters.FilterLike(Post.title, 'Fixed Title', options=(('test1', 'Test 1'), ('test2', 'Test 2'))))

    form_args = dict(text=dict(label='Big Text', validators=[validators.required()]))
    form_ajax_refs = {'user': {'fields': (User.username, User.email)}}

class AdminCategoryView(sqla.ModelView):
    column_list = ('id', 'name', 'slug', )

class AdminTagView(sqla.ModelView):
    column_list = ('id', 'name', 'slug', )
