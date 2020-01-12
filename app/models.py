from . import db
from sqlalchemy.sql import func
from. import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(init(user_id))

class User(UserMixin,db.Model):
    

