from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bp.route('/student')
@login_required
def bookings():
    db = get_db()
    courses = db.execute(
        'SELECT course.id as course_id, course_title,firstname,secondname, user.id as tutor_id, description, duration FROM course JOIN user ON course.user_id = user.id'
    ).fetchall()
        
    return render_template('booking/index.html', courses=courses)

@bp.route('/sessionBooking/<int:course_id>/<int:tutor_id>')
@login_required
def sessionBooking(course_id,tutor_id):
    db = get_db()
    error = None
    book_present = db.execute(
        'SELECT * FROM booking WHERE course_id = ?', (course_id,)
    ).fetchone()
    
    if book_present:
        error = 'You have already booked this course'
        
    if error is None:
        try:
            db.execute(
                "INSERT INTO booking (user_id,tutor_id,course_id) VALUES (?,?,?)",
                (g.user['id'],tutor_id,course_id),
            )
            db.commit()
        except db.IntegrityError:
            error = f"Something Went wrong."
        else:
            return redirect(url_for("bookings.bookings"))
        return f"Details for Course ID: {course_id}"
    flash(error)
    return redirect(url_for("bookings.bookings"))

@bp.route('/tutor')
@login_required
def bookingTutor():
    db = get_db()
    bookings = db.execute(
        'SELECT * FROM booking JOIN user ON booking.user_id = user.id JOIN course ON booking.course_id = course.id'
    ).fetchall()
    
    # JOIN user ON course.user_id = user.id
    
    return render_template('booking/tutor.html', bookings=bookings)


@bp.route('/approve/<int:booking_id>')
@login_required
def approve(booking_id):
    db = get_db()
    error = None
    print(booking_id)
    if error is None:
        try:
            db.execute(
                "UPDATE booking SET status = ? WHERE id = ?",
                ('approve', booking_id) 
            )
            db.commit()
        except db.IntegrityError:
            error = f"Something Went wrong."
        else:
            return redirect(url_for("bookings.bookingTutor"))
        return f"Details for Course ID: {booking_id}"
    flash(error)
    return redirect(url_for("bookings.bookingTutor"))


@bp.route('/deny/<int:booking_id>')
@login_required
def deny(booking_id):
    db = get_db()
    error = None
    print(booking_id)
    if error is None:
        try:
            db.execute(
                "UPDATE booking SET status = ? WHERE id = ?",
                ('deny', booking_id) 
            )
            db.commit()
        except db.IntegrityError:
            error = f"Something Went wrong."
        else:
            return redirect(url_for("bookings.bookingTutor"))
        return f"Details for Course ID: {booking_id}"
    flash(error)
    return redirect(url_for("bookings.bookingTutor"))

@bp.route('/booked')
@login_required
def  booked():
    db = get_db()
    bookings = db.execute(
        'SELECT * FROM booking JOIN user ON booking.tutor_id = user.id JOIN course ON booking.course_id = course.id'
    ).fetchall()
    
    return render_template('booking/student.html', bookings=bookings)