from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
import os
from linked_list import LinkedList
from flask_migrate import Migrate
from hash_table import HashTable
import random
from binary_search_tree import BinarySearchTree

#define the app
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    #configure the app
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        "sqlite:///" + os.path.join(basedir,"data.sqlite")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.app_context():
        db = SQLAlchemy(app)
        db.create_all()
        migrate = Migrate(app, db)
    return app,db

app, db = create_app()

#setup some basic models
class User(db.Model):
    __tblename__ = "users"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(64))
    posts = db.relationship("BlogPost")

    def __repr__(self):
        return f"User\t name: {self.name},\n\t email: {self.email},\n\t phone: {self.phone}\n"

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(500))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer(),db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return '<BlogPost %r>' % self.title

#create routes
@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email'],
        address=data['address'],
        phone=data['phone']
        )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" : "User created"}), 200

#returns all used ascending by id using linked list
@app.route("/user/ascending_id", methods=['GET'])
def get_all_users_asc():
    users = User.query.all()
    all_users_ll = LinkedList()

    for user in users:
        all_users_ll.insert_end(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "phone" : user.phone,
                "address" : user.address
            }
        )
    return jsonify(all_users_ll.to_list()), 200


#returns all unders descending by id using linked list
@app.route("/user/descending_id", methods=['GET'])
def get_all_users_desc():
    users = User.query.all()
    all_users_ll = LinkedList()
    #populate the linked list by populating at beginning
    for user in users:
        all_users_ll.insert_beginning(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "phone" : user.phone,
                "address" : user.address
            }
        )
    return jsonify(all_users_ll.to_list())


@app.route("/user/<user_id>", methods=['GET'])
def get_user(user_id):
    users = User.query.all()
    all_users_ll = LinkedList()
    for user in users:
        all_users_ll.insert_beginning(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "phone" : user.phone,
                "address" : user.address
            }
        )
    user = all_users_ll.get_user_by_id(user_id)
    return jsonify(user), 200



@app.route("/user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    pass

@app.route("/blog_post/<user_id>", methods=['POST'])
def create_blog_post(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message" : "user not found"}),400

    ht = HashTable(10)
    ht.add_key_value("title", data["title"])
    ht.add_key_value("body", data["body"])
    ht.add_key_value("date", datetime.now())
    ht.add_key_value("user_id", user_id)

    new_post = BlogPost(
            title = ht.get_value('title'),
            body = ht.get_value('body'),
            date = ht.get_value('date'), 
            user_id=ht.get_value('user_id'))
    
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message" : "Blog post created"}), 200
    

@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def get_blog_post(blog_post_id):
    blogs = BlogPost.query.all()
    random.shuffle(blogs)

    bst = BinarySearchTree()
    for post in blogs:
        bst.insert({
            'id' : post.id,
            'title' : post.title,
            'body' : post.body,
            'user_id' : post.user_id
        })

    post = bst.search(blog_post_id)

    if not post:
        return jsonify({"message" : "post not found"})
    
    return jsonify(post)


@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def delete_blog_posts(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)