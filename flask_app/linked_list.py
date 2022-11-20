class Node:
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node

    #insert into empty list, new node is both head and last
    #otherwise, new node has next node of current head, resassign head
    def insert_beginning(self, data):
        if self.head is None:
            new_node = Node(data,self.head)
            self.head = new_node
            self.last_node = new_node
        else:
            new_node = Node(data,self.head)
            self.head = new_node

    #insert a node at end of list, use insert beginning if empty
    def insert_end(self, data):
        #if empty, insert at beginning
        if self.head is None:
            self.insert_beginning(data)
            return
        #code below not needed since last node is tracked at beginning
        # #if last node is not set
        # if self.last_node is None:
        #     node = self.head
        #     while node.next_node:
        #         print('iter data')
        #         node = node.next_node
        #     node.next_node = Node(data,None)
        #     self.last_node = node.next_node

        #moving out of commented out elseif statement
        #if last node set, then assign its next node, reset last node
        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node

    def __repr__(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} --> "
            node = node.next_node
        
        ll_string += "None"
        return ll_string
