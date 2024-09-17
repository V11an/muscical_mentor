from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('tutor', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
    'SELECT t.id, title, strftime("%Y-%m-%d %H:%M:%S", startTime) as startTime, '
    'strftime("%Y-%m-%d %H:%M:%S", endTime) as endTime, strftime("%Y-%m-%d %H:%M:%S", created) as created, '
    'startDate, endDate, user_id, descriptions, timelineStatus '
    'FROM timeline t JOIN user u ON t.user_id = u.id '
    'ORDER BY created DESC'
).fetchall()

    return render_template('tutor/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        startTime = request.form['start_Time']
        endTime = request.form['end_Time']
        startDate = request.form['start_Date']
        endDate = request.form['end_Date']
        description = request.form['description']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO timeline (title, startTime, endTime, startDate, endDate, descriptions, timelineStatus, user_id)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (title, startTime, endTime, startDate, endDate, description, 'not started', g.user['id'])
            )
            db.commit()
            return redirect(url_for('tutor.index'))

    return render_template('tutor/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def view(id):
    if request.method == 'GET':
        db = get_db()
        db.execute()

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post