from extentions import db


class User(db.Model):
    id = db.COlumn(db.Integer, primary_key=True)
    name = db.COlumn(db.String(50), unique=True)