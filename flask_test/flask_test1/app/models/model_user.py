from datetime import datetime, timezone

from ..extensions import db


    # модель регистрации
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='user', nullable=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    login = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    avatar = db.Column(db.String(200), nullable=True)
