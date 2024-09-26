from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('schedule', __name__, url_prefix='/schedule')

@bp.route('/index', methods=('GET', 'POST'))
@login_required
def schedule():
    db = get_db()
    if request.method == 'POST':
        
        course_id = request.form['course_id']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        if not course_id:
            error = 'course_title is required.'
        elif not start_time:
            error = 'start time is required.'
        elif not end_time:
            error = 'end time is required.'
        elif not start_date:
            error = 'start date is required.'
        elif not end_date:
            error = 'end date is required.'
        
        
        error = None

        if error is None:
            try:
                db.execute(
                    "INSERT INTO schedule (user_id, course_id, start_time, end_time, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)",
                    (g.user['id'], course_id, start_time, end_time, start_date, end_date ),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Something Went wrong."
            else:
                return redirect(url_for("schedule.schedule"))

        flash(error)
    elif request.method == 'GET':
        
        courses = db.execute(
            'SELECT id, course_title FROM course WHERE  user_id = ?', (g.user['id'],)
        ).fetchall()
        
        schedules = db.execute(
            '''
            SELECT course_title, start_date, start_time, end_time 
            FROM schedule 
            JOIN course ON course.id = schedule.course_id 
            WHERE course.user_id = ?
            ''', 
            (g.user['id'],)  # Ensure a tuple by adding a comma
        ).fetchall()

        
        return render_template('schedule/index.html', courses=courses, schedules=schedules)