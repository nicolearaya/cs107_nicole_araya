class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        if node is None:
            return BSTNode(key, val)
        else:
            if node.key < key:
                node.right = self._put(node.right, key, val)
                node.size += 1
            else:
                node.left = self._put(node.left, key, val)
                node.size += 1
        return node

    def _get(self, node, key):
        if node is None or node.key == key:
            return node.val

        if node.key < key:
            return(self._get(node.right, key))
        return self._get(node.left, key)

        raise KeyError('key not found')

    @staticmethod
    def _size(node):
        return node.size if node else 0