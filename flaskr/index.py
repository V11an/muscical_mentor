from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('index', __name__ )

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

    return render_template('index.html', posts=posts)