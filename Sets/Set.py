from BSTNode import BSTNode
from BSTIterator import BSTIterator

class Set:
    def __init__(self, get_key_function = None):
        self.storage_root = None

        # If we want a custom key function we can specify it, otherwise we just use the key
        if get_key_function is None:
            self.get_key_function = lambda el: el
        else:
            self.get_key_function = get_key_function

    def __iter__(self):
        # If storage root is empty don't bother finding min_node
        if self.storage_root is None:
            return BSTIterator(None)

        # Find min node and iterate on it
        min_node = self.storage_root
        while min_node.left is not None:
            min_node = min_node.left
        return BSTIterator(min_node)

    def add(self, new_element):
        pass

    def remove(self):
        pass

    def search(self):
        pass
