from . import db
from sqlalchemy.sql import func
from. import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(init(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvotes= db.relationship('Downvote', backref='user', lazy='dynamic')
    

