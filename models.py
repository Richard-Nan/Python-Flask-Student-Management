from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Studata(db.Model):
    __tablename__ = 'Studata'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    stunumber = db.Column(db.String(10),nullable=False)
    stuname = db.Column(db.String(50), nullable=False)
    grede = db.Column(db.String(10),nullable=False)