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