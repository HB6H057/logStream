from flask import render_template

from app.core.models import Tag, Category, Post

from . import base

@base.route('/', methods=['GET', 'POST'])
def index():
    """
        Index page
    """
    title    = 'logStream'
    subtitle = 'The cake is a lie!!'

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    # pdb.set_trace()
    # return "Hello World!"
    return render_template('index.html', title=title, subtitle=subtitle,
                                         posts=posts)

@base.route('/M/<string:pslug>')
def post_detail(pslug):
    """
    Renders a page for a valid post.
    :params pslug: slug to look up the post.
    """
    pass

@base.route('/tag/<tslug>')
def tags(tslug):
    """
    Renders a page for a list of post by tag
    :params tslug: slug to look up posts by tag
    """
    tag = Tag.query.filter(Tag.slug == tslug).first()
    return render_template('tag.html', tag=tag)

@base.route('/tag')
def all_tags():
    """
    Renders a page for display all tags
    """
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)


@base.route('/category/<cslug>')
def category(cslug):
    """
    Renders a page for a list of post by category
    params: cslug: slug to look up posts by category
    """
    cate = Category.query.filter(Category.slug == cslug).first()
    return render_template('category.html', cate=cate)

@base.route('/category')
def all_cates():
    """
    Renders a page for all categorys
    """
    cates = Category.query.all()
    return render_template('categorys.html', cates=cates)
