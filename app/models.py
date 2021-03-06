from . import app
from flask_sqlalchemy import SQLAlchemy
import datetime
import os


# SQLAlchemy setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, '../data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Software(db.Model):
    """
    Entity class for an item of software submitted for assessment
    """
    __tablename__ = 'software'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    version = db.Column(db.Text)
    submitter = db.Column(db.Text)
    submitted = db.Column(db.DateTime, default=datetime.datetime.now())
    url = db.Column(db.Text)
    scores = db.relationship('Score', backref='software', lazy='dynamic')


class Score(db.Model):
    """
    Entity class for the result of running a metric against an item of software
    """
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))
    name = db.Column(db.Text)
    identifier = db.Column(db.Text)
    category = db.Column(db.Text)
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    interactive = db.Column(db.Boolean)
    value = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    category_importance = db.Column(db.Integer)
    metric_importance = db.Column(db.Integer)
    updated = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.current_timestamp())

    def __init__(self, software_id, name, identifier, category, short_description, long_description, interactive, value,
                 feedback, category_importance=1, metric_importance=1):
        self.software_id = software_id
        self.name = name
        self.identifier = identifier
        self.category = category
        self.short_description = short_description
        self.long_description = long_description
        self.interactive = interactive
        self.value = value
        self.feedback = feedback
        self.category_importance = category_importance
        self.metric_importance = metric_importance


# Create database if required
if not os.path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
    app.logger.info("Creating tables in ./data.sqlite")
    db.create_all()
