from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_course():
    db = get_db()
    if request.method == 'POST':
        course_title = request.form['course_title']
        duration = request.form['duration']
        description = request.form['description']
        
        error = None

        if not course_title:
            error = 'course_title is required.'
        elif not duration:
            error = 'duration is required.'
        elif not description:
            error = 'description is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO course (user_id, course_title, duration, description) VALUES (?, ?, ?, ?)",
                    (g.user['id'], course_title, duration, description ),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Something Went wrong."
            else:
                return redirect(url_for("course.create_course"))

        flash(error)
    elif request.method == 'GET':
        
        print(g.user['id'])
        courses = db.execute(
            'SELECT * FROM course WHERE  user_id = ?', (g.user['id'],)
        ).fetchall()
        
        return render_template('course/create_course.html', courses=courses)
        