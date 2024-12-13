from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(11),nullable=False)
    register_date = db.Column(db.DateTime,nullable=False)

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    available = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer,default=0)