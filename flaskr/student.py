from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    student = db.execute(
        'SELECT * FROM user WHERE id = ?', (g.user['id'],)
    ).fetchone()

    bookings = db.execute(
        'SELECT * FROM booking JOIN user ON booking.tutor_id = user.id JOIN course ON booking.course_id = course.id WHERE booking.user_id = ?',(g.user['id'],)
    ).fetchall()

    courses_count = len(bookings)

    status = db.execute(
        # 'SELECT * FROM booking JOIN user ON booking.tutor_id = user.id JOIN course ON booking.course_id = course.id WHERE booking.status = status',('approve',)
        'SELECT * FROM booking JOIN user ON booking.tutor_id = user.id JOIN course ON booking.course_id = course.id WHERE booking.user_id = ?',(g.user['id'],)

    ).fetchall()

    status_count = len(status)
    
    return render_template('student/dashboard.html', student=student, bookings=bookings, courses_count = courses_count, status=status, status_count = status_count)

@bp.route('/profile')
@login_required
def student_profile():
    db = get_db()
    myprofile = db.execute(
        'SELECT firstname, secondname, userType, email FROM user WHERE id = ?', (g.user['id'],)  # Note the comma
    ).fetchone()
    db.commit()
    
    mybookings = db.execute(
        'SELECT * FROM booking JOIN user ON booking.user_id = user.id JOIN course ON booking.course_id = course.id  WHERE user.id = ?', (g.user['id'],)
    ).fetchall()
    

    return render_template('student/profile.html', myprofile=myprofile, mybookings=mybookings)