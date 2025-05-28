from BSTNode import BSTNode
from BSTIterator import BSTIterator

class Set:
    def __init__(self, get_key_function = None):
        self.storage_root = None

        # If we want a custom key function we can specify it, otherwise we just use the key
        if get_key_function is None:
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function

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
        """Insert new element into set. Return True if successfully added, return False if already in set."""
        element_key = self.get_key(new_element)

        # Node already exists, exiting early
        if self.node_search(element_key) is not None:
            return False

        # Node doesn't exist already, make it and place it in the right spot
        new_node = BSTNode(new_element, None)

        # Empty tree, insert as root
        if self.storage_root is None:
            self.storage_root = new_node
            return True

        # There's already data here, find where to put the new node
        else:
            node = self.storage_root
            while node is not None:
                # Search left
                if element_key < self.get_key(node.data):
                    if node.left is None:
                        node.left = new_node
                        new_node.parent = node
                        return True
                    else:
                        node = node.left
                # Search right
                else:
                    if node.right is None:
                        node.right = new_node
                        new_node.parent = node
                        return True
                    else:
                        node = node.right

    def remove(self):
        pass

    def search(self):
        pass

    def node_search(self, key):
        """Search for the node. If found return the node, else return None"""
        node = self.storage_root
        # Search through the BST for the node, returning if found
        while node is not None:
            node_key = self.get_key(node.data)
            if node_key == key:
                return node
            elif key > node_key:
                node = node.right
            else:
                node = node.left
        return node