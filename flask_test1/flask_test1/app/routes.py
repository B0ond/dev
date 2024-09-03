from flask import Blueprint
from ..models.models import User
from .extensions import db

user = Blueprint('user_bane', __name__)

@user.route('/user/<name>')
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return 'USer created successfully!'