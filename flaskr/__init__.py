import os

from flask import Flask
from . import db
from . import auth
from . import tutor
from . import student
from . import course
from . import index
from . import schedule


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(tutor.bp)
    app.register_blueprint(student.bp)
    app.register_blueprint(course.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(schedule.bp)
    app.add_url_rule('/', endpoint='index')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app