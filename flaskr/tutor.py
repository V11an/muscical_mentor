from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('tutor', __name__, url_prefix='/tutor')

@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    tutor = db.execute(
        'SELECT * FROM user WHERE id = ?', (g.user['id'],)
    ).fetchone()
    # fetch all students 
    students = db.execute(
        'SELECT * FROM user WHERE userType = ?', ('student', )
    ).fetchall()
    
    students_count = len(students)
    
    courses = db.execute(
        'SELECT * FROM course WHERE user_id = ?', (g.user['id'],)
    ).fetchall()
    
    courses_count = len(courses)

    bookings = db.execute(
        'SELECT * FROM booking JOIN user ON booking.tutor_id = user.id JOIN course ON booking.course_id = course.id WHERE booking.user_id = ?',(g.user['id'],)
    ).fetchall()
    
    bookings_count = len(bookings)
    
    # return render_template('tutor/dashboard.html', tutor = tutor,  students_count = students_count, courses=courses, courses_count = courses_count, bookings_count = bookings_count, bookings = bookings)

    return render_template('tutor/dashboard.html', tutor = tutor,  courses=courses, courses_count = courses_count, bookings_count = bookings_count, bookings = bookings)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    print("create course")
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

@bp.route('/profile')
def profile():
    db = get_db()
    myprofile = db.execute(
        'SELECT firstname, secondname, userType, email FROM user WHERE id = ?', (g.user['id'],)  # Note the comma
    ).fetchone()
    db.commit()
    
    mybookings = db.execute(
        'SELECT * FROM course WHERE user_id = ?', (g.user['id'],)
    ).fetchall()

    return render_template('tutor/profile.html', myprofile=myprofile , mybookings=mybookings)

@bp.route('/schedule'  , methods=('GET', 'POST'))
def schedule():
    if request.method == 'POST':
        user_id  = g.user['id']
        course_id  = request.form['course_id']
        startTime   = request.form['start_time']
        endTime     = request.form['end_time']
        startDate  = request.form['start_date']
        endDate    = request.form['end_date']

        db =  get_db()
        db.execute(
            'INSERT INTO schedule (user_id, course_id, start_time, end_time, start_date,  end_date)'
            ' VALUES (?, ?, ?, ?, ?)',
            (user_id, course_id, startTime, endTime, startDate,  endDate))
        db.commit()
        return redirect(url_for('tutor.schedule'))
    else:
        db = get_db()
        schedule = db.execute(
            'SELECT user_id, course_id startTime, endTime, startDate, endDate FROM schedule where  user_id=?', (g.user['id'])
            ).fetchall()
        return render_template('tutor/schedule.html', schedule=schedule)
    
# @bp.route('/profile/<int:id>', methods=('GET', 'POST'))
# def profile(id):
#     if request.method == 'GET':
#         db = get_db()
#         tutor =  db.execute(
#             'SELECT id, firstname, secondname, userType, email FROM user where id=?', (g.user['id'])
#         )
#         return render_template('tutor.profile', tutor=tutor)
