class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #method used if data['id'] assigned to non-empty tree, evaluate data['id']
    #against node and move to left/right node until insert reaches
    #an empty node
    def _insert_recursive(self,data, node):
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data,node.left)
        elif data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data,node.right)
        #in this case, data['id'] is already in tree
        else:
            return
    
    #insert a data['id'] into tree, assign root if empty, else left/right
    #of the root, to the next available empty node, found recursively
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert_recursive(data,self.root)

    
    def _search_recursive(self,id, node):
        #only root exists, this is a bug if only one node in tree
        if node.left is None and node.right is None:
            return False
        elif id == node.data['id']:
            return node.data
        #left side of the tree
        elif id < node.data['id']and node.left is not None:
            if id == node.left.data['id']:
                return node.left.data
            else:
                return self._search_recursive(id,node.left)
        #right side of the tree
        elif id > node.data['id']and node.right is not None:
            if id == node.right.data['id']:
                return node.right.data
            else:
                return self._search_recursive(id,node.right)
    
            
    def search(self, id):
        id = int(id)
        if self.root is None:
            return False
        
        return self._search_recursive(id,self.root)