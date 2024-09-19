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
    
    return render_template('student/stud_dash.html', student=student)
