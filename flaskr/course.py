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
        elif duration and duration.isdigit():
            duration = int(duration)
            if duration > 100:
                error = 'Duration should be less than 100.'
        
        elif course_title is "":
            error = 'course_title is required.'
            
        course_present = db.execute(
            'SELECT id FROM course WHERE course_title = ? AND user_id = ?', (course_title, g.user['id'])
        ).fetchone()

        if course_present:
            error = 'You already registered for this Instrument.'


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
                flash('Successful!', 'success')
                return redirect(url_for("course.create_course"))

        flash(error,'error')
        return redirect(url_for("course.create_course"))
    elif request.method == 'GET':
        
        print(g.user['id'])
        courses = db.execute(
            'SELECT * FROM course WHERE  user_id = ?', (g.user['id'],)
        ).fetchall()
        
        return render_template('course/create_course.html', courses=courses)
    

@bp.route('/delete_course/<int:course_id>')  # Ensure you have the slash before course_id
@login_required
def delete_course(course_id):
    db = get_db()
    db.execute('DELETE FROM course WHERE id = ?', (course_id,))
    db.commit()  # Make sure to commit the transaction
    return redirect(url_for('course.create_course'))  # Redirect to the create course page

        