def merge(numbers, i, j, k):
    merged_size = k - i + 1
    merged_numbers = [0] * merged_size

    merge_pos = 0
    left_pos = i
    right_pos = j + 1

    # Add the smallest element from the left OR right to merged_numbers
    while (left_pos <= j) and (right_pos <= k):
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    # If left or right aren't empty put them into the merged list
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    # Put the merged list back into the numbers list
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]


def merge_sort(numbers, i = 0, k = None):
    if k is None:
        k = len(numbers) - 1

    j = 0
    if i < k:
        j = (i + k) // 2

        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        merge(numbers, i, j, k)


# Create a list of unsorted values
numbers = [61, 76, 19, 4, 94, 32, 27, 83, 58]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to merge_sort
merge_sort(numbers)

# Print sorted list
print('SORTED:', numbers)