from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth.auth import login_required
from flaskr.db import get_db
from . import queries as q
bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = q.get_posts(get_db())
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            q.create_post(get_db(), title, body, g.user['id']) 
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = q.get_post(get_db(), id)

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/', methods=('GET',))
def post_details(id):
    post = q.get_post(get_db(), id)
    
    if post is None:
        abort(404, "The page doesn't exist!")

    return render_template('blog/single_post.html', post=post)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            q.update_post(get_db(), title, body, id)
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    q.delete_post(get_db(), id)
    return redirect(url_for('blog.index'))