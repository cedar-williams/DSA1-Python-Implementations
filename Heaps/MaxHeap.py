from numbers import Number


class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index) -> None:
        """Percolate up the node at the specified index"""

        # Run until we hit the root node, unless we exit early elsewhere
        while node_index > 0:
            parent_index = (node_index - 1) // 2

            # Check if child/parent nodes violate max-heap properties
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                return # They don't, exiting func
            else: # They do, swap child with parent
                tmp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = tmp

                node_index = parent_index


    def percolate_down(self, node_index) -> None:
        """Percolate down the node at the specified index"""

        # Starting values, these will change during iterations below
        child_index = (node_index * 2) + 1
        value = self.heap_array[node_index]

        # Run until we hit the last node value, unless we exit early elsewhere
        while child_index < len(self.heap_array):
            max_value = value
            max_index = -1
            i = 0
            # Find which child is largest if any
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i = i + 1

            # Any further swaps would violate the rules of the heap, exit the func
            if max_value == value:
                return
            # Swap with child node, update the current nodes to repeat iteration down the tree
            else:
                tmp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = tmp

                node_index = max_index
                child_index = (node_index * 2) + 1


    def insert(self, value) -> None:
        """Insert new value at end of heap_array, then percolate it up"""
        self.heap_array.append(value)
        self.percolate_up(len(self.heap_array) - 1)


    def remove(self) -> float:
        """Remove and return the max value of the heap, balance with percolate_down"""
        max_value = self.heap_array[0]

        # Place end value at start, then percolate down
        replacement_value = self.heap_array.pop()
        # Make sure there's an array to trickle down to
        if len(self.heap_array) > 0:
            self.heap_array[0] = replacement_value
            self.percolate_down(0)

        return max_value



if __name__ == "main":
    # Test code from the textbook
    h = MaxHeap()
    input_list = [ 10, 2, 5, 18, 22 ]
    for item in input_list:
        h.insert(item)
        print('   --> array: %s\n' % h.heap_array)
    while len(h.heap_array) > 0:
        removed_value = h.remove()
        print('   --> removed %d, array: %s\n' % (removed_value, h.heap_array))
    print()