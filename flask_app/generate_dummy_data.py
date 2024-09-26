#adapted from https://github.com/selikapro/FlaskDS

from random import randrange
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from faker import Faker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, User, BlogPost, db

faker = Faker()

# create dummy users
for i in range(200):
    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'
    new_user = User(name=name, address=address, phone=phone, email=email)
    db.session.add(new_user)
    db.session.commit()

# create dummy blog posts
for i in range(200):
    title = faker.sentence(5)
    body = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 200)

    new_blog_post = BlogPost(
        title=title, body=body, date=date, user_id=user_id
    )
    db.session.add(new_blog_post)
    db.session.commit()