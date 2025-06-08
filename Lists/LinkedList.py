class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return_str = '{'
        current_node = self.head
        while current_node is not None:
            return_str += str(current_node.data) + ','
            current_node = current_node.next
        return_str += return_str[:-1] + '}'
        return return_str

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        if current_node == None and self.head != None:
            successor_node = self.head.next
            self.head = successor_node
            if successor_node == None:
                self.tail = None
        elif current_node.next != None:
            successor_node = current_node.next.next
            current_node.next = successor_node
            if successor_node == None:
                self.tail = None

    def insertion_sort(self):
        before_current = self.head
        current_node = self.head.next
        while current_node != None:
            next_node = current_node.next
            position = self._find_insertion_position(current_node.data)
            if position == before_current: # Node is already in the right spot
                before_current = current_node
            else:
                self.remove_after(before_current)
                if position == None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node


    def _find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while (position_b != None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a