from app import User
from linked_list import LinkedList
from flask import jsonify

all_users = User.query.all()
all_users_ll = LinkedList()

for user in all_users:
    all_users_ll.insert_beginning(
        {
            "id" : user.id,
            "name" : user.name
        }
    )


print((all_users_ll.to_list()))