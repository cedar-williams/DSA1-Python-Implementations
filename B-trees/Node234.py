class Node234:
    def __init__(self, key_A, left_child = None, middle1_child = None):
        self.A = key_A
        self.B = None
        self.C = None
        self.left = left_child
        self.middle1 = middle1_child
        self.middle2 = None
        self.right = None

    def get_child(self, child_index):
        """Return child by index, in range 0-3. If outside range return None"""
        if child_index == 0:
            return self.left
        elif child_index == 1:
            return self.middle1
        elif child_index == 2:
            return self.middle2
        elif child_index == 3:
            return self.right
        else:
            return None

    def get_child_index(self, child):
        """Return index of child, or -1 if not a child"""
        if child is self.left:
            return 0
        elif child is self.middle1:
            return 1
        elif child is self.middle2:
            return 2
        elif child is self.right:
            return 3
        else:
            return -1

    def get_key(self, key_index):
        """Return key and specified index (0-2) or None if index out of bounds"""
        if key_index == 0:
            return self.A
        elif key_index == 1:
            return self.B
        elif key_index == 2:
            return self.C
        return None

    def get_key_index(self, key):
        """Return index (0-2) of key, or -1 if not a key"""
        if key == self.A:
            return 0
        elif key == self.B:
            return 1
        elif key == self.C:
            return 2
        return -1

    def append_key_and_child(self, key, child):
        if self.B is None:
            self.B = key
            self.middle2 = child
        else:
            self.C = key
            self.right = child

    def count_keys(self):
        if self.C is not None:
            return 3
        elif self.B is not None:
            return 2
        else :
            return 1

    def has_key(self, key):
        """Return True if key in node, else False"""
        return (self.A == key) or (self.B == key) or (self.C == key)

    def insert_key(self, key):
        """Insert key in proper place. Precondition: node is a leaf & not full"""
        if key < self.A:
            self.C = self.B
            self.B = self.A
            self.A = key
        elif (self.B is None) or (key < self.B):
            self.C = self.B
            self.B = key
        else:
            self.C = key

    def insert_key_with_children(self, key, left_child, right_child):
        if (key < self.A):
            self.C = self.B
            self.B = self.A
            self.A = key
            self.right = self.middle2
            self.middle2 = self.middle1
            self.middle1 = right_child
            self.right = left_child
        elif (self.B is None) or (key < self.B):
            self.C = self.B
            self.B = key
            self.right = self.middle2
            self.middle2 = right_child
            self.middle1 = left_child
        else:
            self.C = key
            self.right = right_child
            self.middle2 = left_child

    def is_leaf(self):
        """Return True if leaf node, False otherwise"""
        return self.left is None

    def next_node(self, key):
        """Return next node in traversal for specified key"""
        if key < self.A:
            return self.left
        elif (self.B is None) or (key < self.B):
            return self.middle1
        elif (self.C is None) or (key < self.C):
            return self.middle2
        else:
            return self.right

    def remove_key(self, key_index):
        """Removes key A, B, or C by index. Shifts remaining keys/child pointers."""
        if key_index == 0:
            self.A = self.B
            self.B = self.C
            self.C = None
            self.left = self.middle1
            self.middle1 = self.middle2
            self.middle2 = self.right
            self.right = None
        elif key_index == 1:
            self.B = self.C
            self.C = None
            self.middle2 = self.right
            self.right = None
        elif key_index == 2:
            self.C = None
            self.right = None

    def remove_rightmost_child(self):
        removed = None
        if self.right is not None:
            removed = self.right
            self.right = None
        elif self.middle2 is not None:
            removed = self.middle2
            self.middle2 = None
        return removed

    def remove_rightmost_key(self):
        removed = None
        if self.C is not None:
            removed = self.C
            self.C = None
        elif self.B is not None:
            removed = self.B
            self.B = None
        return removed

    def set_child(self, child, child_index):
        """Sets child at specified index (0-3). Does nothing on wrong index"""
        if child_index == 0:
            self.left = child
        elif child_index == 1:
            self.middle1 = child
        elif child_index == 2:
            self.middle2 = child
        elif child_index == 3:
            self.right = child

    def set_key(self, key, key_index):
        if key_index == 0:
            self.A = key
        elif key_index == 1:
            self.B = key
        elif key_index == 2:
            self.C = key