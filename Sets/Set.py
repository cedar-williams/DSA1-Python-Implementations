from BSTNode import BSTNode
from BSTIterator import BSTIterator

class Set:
    def __init__(self, get_key_function = None):
        self.storage_root = None

        # If we want a custom key function we can specify it, otherwise we just use the key
        # We will use self.get_key as a reference to functon this later on
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

    def __len__(self):
        if self.storage_root is None:
            return 0
        else:
            return self.storage_root.count()

    def __str__(self):
        return_string = '{ '
        for element in self:
            return_string += str(element) + ' '
        return  return_string + '}'

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

    def difference(self, other_set):
        pass

    def filter(self, predicate):
        pass

    def intersection(self, other_set):
        pass

    def union(self, other_set):
        pass

    def map(self, map_function):
        result = Set(self.get_key)
        for element in self:
            new_element = map_function(element)
            result.add(new_element)
        return result

    def remove(self, key):
        self.remove_node(self.node_search(key))

    def remove_node(self, node_to_remove):
        if node_to_remove is not None:
            # Case 1 - internal node with 2 children
            if (node_to_remove.left is not None) and (node_to_remove.right is not None):
                successor = node_to_remove.get_successor()
                node_data = successor.data
                self.remove_node(successor)
                node_to_remove.data = node_data

            # Case 2 - root node with 0 or 1 child
            elif node_to_remove is self.storage_root:
                if node_to_remove.left is not None:
                    self.storage_root = node_to_remove.left
                elif node_to_remove.right is not None:
                    self.storage_root = node_to_remove.right

                if self.storage_root is not None:
                    self.storage_root.parent = None

            # Case 3 - internal node with left child only
            elif node_to_remove.left is not None:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)

            # Case 4 - internal node with right child only OR leaf node
            else:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

    def node_search(self, key):
        """Search for and return node matching key, or None if no node found"""
        node = self.storage_root
        while node is not None:
            node_key = self.get_key(node.data)
            if node_key == key:
                return node
            elif node_key < key:
                node = node.left
            else:
                node = node.right
        return node

    def search(self, key):
        """Search for and return data associated with node"""
        # First find the node
        node = self.node_search(key)

        # Then return its data
        if node is not None:
            return node.data
        return None

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