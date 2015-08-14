LEFT = 0
RIGHT = 1
VALUE = 2
ROOT_VALUE = -1

class BST:

    def __init__(self, key = None):

        self.root = []
        self.len = 0
        if key is None:
            self.sort = lambda x:x
        else:
            self.sort = key

    def insert(self, value):

        sort_key = self.sort(value)
        node = self.root
        while node:
            if sort_key < self.sort(node[ROOT_VALUE]):
                node = node[LEFT]
            else:
                node = node[RIGHT]
        node[:] = [[],[], value]
        self.len += 1

    def delete_node(self, node):
        if node[LEFT]:
            if node[RIGHT]:
                cat = node[RIGHT]
                while cat[LEFT]: cat = cat[LEFT]
                node[VALUE:] = cat[VALUE:] #copy value
                cat[:] = cat[RIGHT]
            else:
                node = node[LEFT]
        else:
            if node[RIGHT]:
                node[:] = node[RIGHT]
            else:
                del node[:]
        self.len -= 1

    def delete_key(self, sort_key):
        node = self.find(sort_key)
        self.delete_node(node)

    def find(self, sort_key):
        node = self.root
        while node:
            if self.sort(node[ROOT_VALUE]) <  sort_key:
                node = node[RIGHT]
            elif self.sort(node[ROOT_VALUE]) > sort_key:
                node = node[RIGHT]
            else: return node
        print("NOT FOUND")

    def ext_node(self, side):
        node = self.root
        while node[side]:
            node = node[side]
        return node

    def maximum(self):
        return self.ext_node(LEFT)[VALUE]

    def minimum(self):
        return self.ext_node(RIGHT)[VALUE]

bt = BST()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(-1)
bt.insert(10)
print(bt.maximum())
print(bt.minimum())