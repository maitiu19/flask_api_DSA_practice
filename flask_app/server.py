from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request,jsonify
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

#define the app
app = Flask(__name__)

#configure the app
app.config["SQLALCHRMY_DATABASE_URI"] = "sqlite:sqlitedb.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0

#configure sqlite3 to enfore foriegn key contraints

#setup some basic models
class User(db.Model):
    __tblename__ = "users"
    id = db.Column(db.integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(64))
    posts = db.relationship("BlogPost")