from Lists.LinkedList import LinkedList
from Queues.Node import Node

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, item):
        node = Node(item)
        self.list.append(node)

    def dequeue(self):
        dequeued_item = self.list.head.data
        self.list.remove_after(None)
        return dequeued_item


    def peek(self):
        if self.list.head:
            return self.list.head.data
        else:
            return None

    def is_empty(self):
        return self.list.head is None