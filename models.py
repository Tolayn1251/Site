from app import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default= datetime.now())
    title= db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False)
    userpassword = db.Column(db.Text(), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.now())
    content = db.Column(db.Text(), nullable=False)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))