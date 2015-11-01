import pdb
from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

post_tags_table = db.Table('post_tags',
            db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
            db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
            )

category_posts_table = db.Table('category_tag',
            db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
            db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
            )


class Post(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    title     = db.Column(db.String(120))
    slug      = db.Column(db.String(120))
    body      = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags      = db.relationship('Tag', secondary=post_tags_table,
                                backref=db.backref('posts', lazy='dynamic'),
                                )
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Tag(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(64), index=True, unique=True)
    slug  = db.Column(db.String(64), index=True, unique=True)

    # def __init__(self, name, slug):
    #         self.name = name
    #         self.slug = slug
    #


class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    nickname      = db.Column(db.String(64))
    username      = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts         = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('GlaDOS:"What are you doing?\
                              (password is not a readable attribute)"')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.nickname

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64))

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='info')

    def __unicode__(self):
        return '%s - %s' % (self.key, self.value)

class Category(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(63), index=True, unique=True)
    posts = db.relationship('Post', secondary=category_posts_table,
                            backref=db.backref('cates', lazy='dynamic'),
                            )
