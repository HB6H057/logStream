from app import db, login_manager
from datetime import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

    def __init__(self, name, slug):
            self.name = name
            self.slug = slug

    def save(self):
        db.session.add(self)
        db.session.commit()


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

class Category(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(63), index=True, unique=True)
    posts = db.relationship('Post', secondary=category_posts_table,
                            backref=db.backref('cates', lazy='dynamic'),
                            )

    def save(self):
        db.session.add(self)
        db.session.commit()


def _add_tag(name):
    slug = name.lower().replace(' ', '-')
    tag  = db.session.query(Tag).filter(Tag.slug==slug).first()
    if not tag:
        tag = Tag(name, slug)
        tag.save()
    return tag

def post_new(user, body, tagnames=[]):
    post = Post(body=body, user=user)
    for tagname in tagnames:
        tag = _add_tag(tagname)
        post.tags.append(tag)
    post.save()
    return post
