from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
        
    def _removemin(self, node):
        if node.left == None:
            return node.right
        else:
            node.left = self._removemin(node.left)
        node.size = node.size - 1
        return node
    
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        #  Should return a subtree whose root is  but without
        #       the node whose key is 

        if not node: 
            raise KeyError
    
        if node.key < key:
            node.right = self._remove(node.right, key)
        elif node.key > key:
            node.left = self._remove(node.left, key)
            
        #find node    
        else:
            #one child -> replace node with child
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            #if node has two children
            y = node
            def min(nd):
                if nd.left == None:
                    print("found min")
                    return nd
                else:
                    nd.left = min(nd.left)
            node = min(y.right)
            node.right = self._removemin(y.right)
            node.left = y.left
            
        node.size = self._size(node.left) + self._size(node.right) + 1;    
        return node

    @staticmethod
    def _size(node):
        return node.size if node else 0
        


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree 
        self.traversalType = traversalType
        self.traversal = []
        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.INORDER:
            self.inorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(self.tree)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= (len(self.traversal)-1):
           raise StopIteration
        else: 
            self.index +=1
            return self.traversal[self.index]

    def inorder(self, bst: BSTTable):
        def recursive(nd):
            if nd.left is not None:
                recursive(nd.left)
                #append
            self.traversal.append(nd)
            if nd.right is not None:
                recursive(nd.right)
        recursive(bst._root)

    def preorder(self, bst: BSTTable):
        #node
        #self.postorder(node.left)   
        #self.postorder(node.right)
        def recursive(nd):
            self.traversal.append(nd)
            if nd.left is not None:
                recursive(nd.left)
                #append
            if nd.right is not None:
                recursive(nd.right)
        recursive(bst._root)

    def postorder(self, bst: BSTTable):
        #self.postorder(node.left)   
        #self.postorder(node.right)
        #node
        def recursive(nd):
            if nd.left is not None:
                recursive(nd.left)
                #append
            if nd.right is not None:
                recursive(nd.right)
            self.traversal.append(nd)
        recursive(bst._root)