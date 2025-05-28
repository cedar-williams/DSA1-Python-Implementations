class BSTIterator:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        if self.node is None:
            raise StopIteration
        else:
            current_data = self.node.data
            self.node = self.node.get_successor()
            return current_data