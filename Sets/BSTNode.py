class BSTNode:
    def __init__(self, data, parent, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def count(self):
        count = 0
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return 1 + count

    def get_successor(self):
        # There is a right child, find successor down
        if self.right is not None:
            successor_node = self.right
            while successor_node.left is not None:
                successor_node = successor_node.left
            return successor_node

        # Successor is up the tree somewhere, find it and return it
        else:
            node = self
            while (node.parent is not None) and (node is node.parent.right):
                node = node.parent
            return node

    def replace_child(self, current_child, new_child):
        if current_child is self.left:
            self.left = new_child
            if self.left is not None:
                self.left.parent = self

        elif current_child is self.right:
            self.right = new_child
            if self.right is not None:
                self.right.parent = self