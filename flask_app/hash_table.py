class Node:
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class HashTable:
    #HashTable takes in a value for table size
    #create list called hash_table of len(table_size)
    def __init__(self, table_size) -> None:
        self.table_size = table_size
        self.hash_table = [None] * table_size

    #create a hash code for each given value
    #ord() assigns an decmial value for each ASCII provided
    #modulo by table_size ensures the hash_value doesn't exceed index
    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value


    #created a hashed key and add to hashed table index 
    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key,value),None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node is not None:
                node = node.next_node
            node.next_node = Node(Data(key,value),None)



    #retrieve data value from hash table
    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        #if hkey in htable, check if next node is none
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            #if nextnode is none return node, otherwise search til found
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if node.data.key == key:
                    return node.data.value
                node = node.next_node
            if key == node.data.key:
                return node.data.value
            else:
                 return None

    def print_ht(self):
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node is not None:
                    while node.next_node is not None:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> None"
                        )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")

ht= HashTable(7)
ht.add_key_value("acegiklferuenbuienbibebneti", "added_1st")
ht.add_key_value("tiiuyuvt", "added_2nd")
ht.add_key_value("zbyuyuuuuuuuu", "added_3rd")
ht.add_key_value("f", "added_4th")
ht.add_key_value("t", "added_5th")
ht.add_key_value("p", "added_6th")
ht.print_ht()
