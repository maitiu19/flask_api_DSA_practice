from app import User,BlogPost
from linked_list import LinkedList
from hash_table import HashTable

all_users = User.query.all()
all_users_ll = LinkedList()

for user in all_users:
    all_users_ll.insert_beginning(
        {
            "id" : user.id,
            "name" : user.name
        }
    )

#print((all_users_ll.to_list()))

posts = BlogPost.query.filter_by(user_id=10).all()
print(posts)