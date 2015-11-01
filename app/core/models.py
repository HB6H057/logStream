import pdb
import re
from datetime import datetime

from xpinyin import Pinyin
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
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

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
    # @staticmethod
    # def add_category(name):
    #     slug = name2slug(name)
    #     cate  = db.session.query(Category).filter(Category.slug==slug).first()
    #     if not cate:
    #         cate = Category(name=name, slug=slug)
    #         cate.save()
    #     return cate
    #
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

# 1.Tags are separated by commas.
# 2.Slug must be lowercase and must not contain letters and '-' character outside
# def _add_tag(name):
#     slug = name2slug(name);
#     tag  = db.session.query(Tag).filter(Tag.slug==slug).first()
#     if not tag:
#         tag = Tag(name, slug)
#         tag.save()
#     return tag

# test: a post a categroy
# def new_post(user, title, slug, body, cates, tagnames=[]):
#     cates = db.session.query(Category).filter(Category.slug==cates.slug).first()
#     # if cates is None......
#     # pdb.set_trace()
#     post = Post(title=title, slug=slug, body=body, user=user)
#     post.cates.append(cates)
#     for tagname in tagnames:
#         tag = _add_tag(tagname)
#         post.tags.append(tag)
#     post.cates.append(cates)
#     post.save()
#     return post

def name2slug(name):
    '''
        1. chinese to pinyin.
        2. to lower.
        3. remove special character. (except: '-',' ')
        4. to convert ' ' into '-'
        5. fix special case of slug.
            I.  multi '-', eg: 'GlaDOS's block' ---> 'gladoss--blog'
            II. ...
    '''
    name = Pinyin().get_pinyin(name)
    pattern = re.compile(r'[^a-zA-z0-9\-]')
    slug = re.sub(pattern, '', name.lower().replace(' ', '-'))
    slug = re.sub('-+', '-', slug)
    return slug
