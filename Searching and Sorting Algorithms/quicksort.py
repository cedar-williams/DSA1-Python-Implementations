def partition(numbers, start_index, end_index):
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    low = start_index
    high = end_index

    done = False
    while not done:
        # Find a pair to swap
        while numbers[low] < pivot:
            low += 1
        while numbers[high] > pivot:
            high -= 1

        # No swap pairs found, low and high partitions have correct numbers
        if low >= high:
            done = True
        # Swap elements and update the indices to keep going
        else:
            temp_value = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp_value
            low += 1
            high -= 1

    # Pass back out the last index for the left partition
    return high

def quicksort(numbers, start_index = 0, end_index = None):
    if end_index is None:
        end_index = len(numbers) - 1

    # Base case
    if end_index <= start_index:
        return

    high = partition(numbers, start_index, end_index)
    quicksort(numbers, start_index, high)
    quicksort(numbers, high + 1, end_index)


# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers)
print('SORTED:', numbers)