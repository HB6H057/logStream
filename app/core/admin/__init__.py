from flask.ext.admin import Admin

from app.core.admin.views import (AdminIndexView, AdminUserView, AdminPostView,
                                  AdminCategoryView, AdminTagView)
from app.core.models import User, Post, Category, Tag
from app import db

def create_admin(app=None, db=None):
    admin = Admin(app, 'logStream', index_view=AdminIndexView(),
                  base_template='admin/my_master.html')
    admin.add_view(AdminUserView(User, db.session))
    admin.add_view(AdminPostView(Post, db.session))
    admin.add_view(AdminCategoryView(Category, db.session))
    admin.add_view(AdminTagView(Tag, db.session))
