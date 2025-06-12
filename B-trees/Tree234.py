from Node234 import Node234

class Tree234:
    def __init__(self):
        self.root = None

    def insert(self, key, node = None, parent_node = None):
        """Insert new key into the tree, provided key doesn't already exist"""

        # Special case - the tree is empty
        if self.root is None:
            self.root = Node234(key)
            return self.root

        # If node is none recursively call with root node
        if node is None:
            return self.insert(key, self.root, None)

        # Check if key is duplicate
        if node.has_key(key):
            return key

        # Preemptively split full nodes
        if node.C is not None:
            node = self.split(node, parent_node)

        if not node.is_leaf():
            if key < node.A:
                return self.insert(key, node.left, node)
            elif (node.B is None) or (key < node.B):
                return self.insert(key, node.middle1, node)
            elif (node.C is None) or (key < node.C):
                return self.insert(key, node.middle2, node)
            else:
                return self.insert(key, node.right, node)

        # I'm a leaf node with room! Stick the key in here
        node.insert_key(key)
        return node

    def search(self, key):
        """Find and return node with key, or None if not found"""
        return self._search_recursive(key, self.root)

    def _search_recursive(self, key, node):
        """Search helper function"""
        if node is None:
            return None
        if node.has_key(key):
            return node

        if key < node.A:
            return self._search_recursive(key, node.left)
        elif (node.B is None) or (key < node.B):
            return self._search_recursive(key, node.middle1)
        elif (node.C is None) or (key < node.C):
            return self._search_recursive(key, node.middle2)
        else:
            return self._search_recursive(key, node.right)

    def split(self, node, node_parent):
        """Split a full node, moving center key into the parent node. Return resulting parent node"""
        split_left = Node234(node.A, node.left, node.middle1)
        split_right = Node234(node.C, node.middle2, node.right)

        if node_parent is not None:
            node_parent.insert_key_with_children(node.B, split_left, split_right)
        else:
            split_parent = Node234(node.B, split_left, split_right)
            self.root = split_parent

        return node_parent

    def fuse(self, parent, left_node, right_node):
        """Fuses parent and 2 child nodes into 1. Precondition: Each node must only have 1 key"""
        # Parent is root, use a special function
        if (parent is self.root) and (parent.count_keys() == 1):
            return self.fuse_root()

        left_node_index = parent.get_child_index(left_node)
        middle_key = parent.get_key(left_node_index)
        fused_node = Node234(left_node.A)
        fused_node.B = middle_key
        fused_node.C = right_node.A
        fused_node.left = left_node.left
        fused_node.middle1 = left_node.middle1
        fused_node.middle2 = right_node.left
        fused_node.right = right_node.middle1
        key_index = parent.get_key_index(middle_key)
        parent.remove_key(key_index)
        parent.set_child(fused_node, key_index)
        return fused_node

    def fuse_root(self):
        """Fuses the tree root with its children"""
        old_left = self.root.left
        old_middle1 = self.root.middle1
        self.root.B = self.root.A
        self.root.A = old_left.A
        self.root.C = old_middle1.A
        self.root.left = old_left.left
        self.root.middle1 = old_left.middle1
        self.root.middle2 = old_middle1.left
        self.root.right = old_middle1.middle1
        return self.root

    def get_min_key(self, node):
        """Find and return minimum key in a subtree"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def key_swap(self, node, existing, replacement):
        """Find and replace one key with another. Key must already be known to not violate the 2-3-4 tree"""
        if node is None:
            return False

        key_index = node.get_get_index(existing)

        # Key not in node, keep looking
        if key_index == -1:
            next = node.next_node(existing)
            return self.key_swap(next, existing, replacement)

        # Key in node, swap
        if key_index == 0:
            node.A = replacement
        elif key_index == 1:
            node.B = replacement
        else:
            node.C = replacement

        return True

    def merge(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        right_sibling = node_parent.get_child(node_index + 1)

        if (left_sibling is not None) and (left_sibling.count_keys() >= 2):
            self.rotate_right(left_sibling, node_parent)
        elif (right_sibling is not None) and (right_sibling.count_keys() >= 2):
            self.rotate_left(right_sibling, node_parent)
        else:
            if left_sibling is None:
                node = self.fuse(node_parent, node, right_sibling)
            else:
                node = self.fuse(node_parent, left_sibling, node)

        return node

    def remove(self, key):
        # Special case if tree has only 1 key
        if (self.root.is_leaf()) and (self.root.count_keys() == 1):
            if self.root.A == key:
                self.root.A = None
                return True
            else:
                return False

        # Locate the node
        current_parent = None
        current = self.root
        while current is not None:
            # If we hit a node with a key count of 1 merge it
            if (current.count_keys() == 1) and (current is not self.root):
                current = self.merge(current, current_parent)

            # Check if current node has key
            key_index = current.get_key_index(key)
            if key_index != -1:
                if current.is_leaf():
                    current.remove_key(key_index)
                    return True

                # Not a leaf, have to do the successor shuffle
                tmp_child = current.get_child(key + 1)
                tmp_key = self.get_min_key(tmp_child)
                self.remove(tmp_key)
                self.key_swap(self.root, key, tmp_key)
                return True

            # Node not found, update pointers and look down a level
            current_parent = current
            current_parent = current.next_node(key)

        # We couldn't find the key at all
        return False

    def rotate_left(self, node, node_parent):
        # Get the left sibling
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)

        # Get parent key that'll be rotated to left sibling
        key_for_left_sibling = node_parent.get_key(node_index - 1)

        left_sibling.append_key_and_child(key_for_left_sibling, node.left)

        # Add the node's key to the parent
        node_parent.set_key(node.A, node_index - 1)

        # Remove the key added to the parent from the current node
        node.remove_key(0)

    def rotate_right(self, node, node_parent):
        # Get the right sibling
        node_index = node_parent.get_child_index(node)
        right_sibling = node_parent.get_child(node_index + 1)

        # Get parent key that'll be rotated to right sibling
        key_for_right_sibling = node_parent.get_key(node_index)

        # Shift key and child references in right sibling to prepare for transfer
        right_sibling.C = right_sibling.B
        right_sibling.B = right_sibling.A
        right_sibling.right = right_sibling.middle2
        right_sibling.middle2 = right_sibling.middle1
        right_sibling.middle1 = right_sibling.left

        # Put rotated parent keys into right sibling
        right_sibling.A = key_for_right_sibling
        right_sibling.left = node.remove_rightmost_child()

        # Replace parent key with key rotated up from current node
        node_parent.set_key(node.remove_rightmost_key(), node_index)
