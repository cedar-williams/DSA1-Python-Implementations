def quickselect(numbers, start_index, end_index, k):
    if start_index >= end_index:
        return numbers[start_index]

    low_last_index = partition(numbers, start_index, end_index)
    if k <= low_last_index:
        return quickselect(numbers, start_index, low_last_index, k)
    return quickselect(numbers, low_last_index + 1, end_index, k)

# Provided code
def partition(numbers, start_index, end_index):
    # select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the current list partition
    # and move towards each other.
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1

        # If low and high have not crossed each other, swap
        # the elements; otherwise the loop is done.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1

    # "high" is the last index in the left partition.
    return high

# The test program begins here. A random-looking list is created, and
# quickselect() is called with a user-supplied value for k.
unsorted_list = [6, 2, 12, 8, 4, 3, 19, 17, 22, 41, 7, 1, 15]
print("Original list:", unsorted_list)

k = int(input())
kth_value = quickselect(unsorted_list, 0, len(unsorted_list) - 1, k)

# Display results, and compare to sorted list.
print("After quickselect(%d):" % k, unsorted_list)
print("quickselect(%d) result: %d" % (k, kth_value))

print()
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)