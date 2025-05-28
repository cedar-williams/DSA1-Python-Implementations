
def max_heap_percolate_down(node_index, heap_list, list_size) -> None:
    """Perform a percolate down, restrict size of heap affected to not touch already sorted values"""

    child_index = (node_index * 2) + 1
    value = heap_list[node_index]

    while child_index < list_size:
        max_value = value
        max_index = -1
        i = 0
        # Find which child is largest if any
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > max_value:
                max_value = heap_list[i + child_index]
                max_index = i + child_index
            i = i + 1

        # Any further swaps would violate the rules of the heap, exit the func
        if max_value == value:
            return

        # Swap with child node, update the current nodes to repeat iteration down the tree
        else:
            tmp = heap_list[node_index]
            heap_list[node_index] = heap_list[max_index]
            heap_list[max_index] = tmp

            node_index = max_index
            child_index = (node_index * 2) + 1


def heap_sort(numbers) -> None:
    """Perform a heap sort on the passed list"""

    # Heapify the number list
    i = len(numbers) // 2 - 1
    while i >= 0:
        max_heap_percolate_down(i, numbers, len(numbers))
        i -= 1

    # Use the heapified list to create a sorted list
    i = len(numbers) - 1
    while i > 0:
        tmp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = tmp
        max_heap_percolate_down(0, numbers, i)
        i -= 1


# Testing
numbers = [82, 36, 49, 82, 34, 75, 18, 9, 23]
print("UNSORTED:", numbers)

heap_sort(numbers)
print("SORTED:  ", numbers)
