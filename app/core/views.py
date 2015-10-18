import pdb

from flask import render_template, flash, redirect, url_for, request, jsonify, Blueprint
from app.core.models import User, Post, Tag, Category
from app.core.models import new_post
from app.core.forms import PostForm


#
# @app.route('/manage/post/new', methods=['GET', 'POST'])
# @login_required
# def post_new():
#     form = PostForm()
#     if form.validate_on_submit():
#         if current_user.is_authenticated() is False:
#             flash('no login no BB')
#             return redirect(url_for('index'))
#
#         tags = map(lambda x:x.strip(' '), form.tags.data.split(','))
#         tags = list(set(tags))
#         if '' in tags:
#             tags.remove('')
#
#         new_post(body=form.body.data, user=current_user._get_current_object(),
#                  tagnames=tags, cates=form.select_category.data,
#                  title=form.title.data, slug=form.slug.data)
#
#         flash('post a new post success')
#         return redirect(url_for('index'))
#     return render_template('post_new.html', form=form)
#
# @app.route('/manage/post/delete/<int:pid>', methods=['GET'])
# @login_required
# def delete_post(pid):
#     post = Post.query.filter(Post.id==pid).first()
#
#     for tag in post.tags:
#         tag.posts.remove(post)
#
#     for cate in post.cates:
#         cate.posts.remove(post)
#
#     db.session.delete(post)
#     db.session.commit()
#
#     flash('delete post success!')
#     return redirect(url_for('index'))
#
# @app.route('/manage/category/get', methods=['POST'])
# @login_required
# def get_category():
#     cate_name = request.form.get('category')
#     if cate_name is None:
#         return jsonify(success=False, html=None)
#     cate = Category.add_category(cate_name)
#     form = PostForm(select_category=cate)
#     html = render_template('select_category.htm', form=form)
#     # pdb.set_trace()
#     return jsonify(success=True, html=html)
