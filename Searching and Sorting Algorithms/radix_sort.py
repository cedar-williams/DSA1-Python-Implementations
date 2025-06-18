def radix_get_max_length(numbers):
    max_digits = 0
    for number in numbers:
        digits = radix_get_length(number)
        if digits > max_digits:
            max_digits = digits
    return max_digits

def radix_get_length(number):
    if number == 0:
        return 1
    digits = 0
    while number != 0:
        digits += 1
        number = number // 10
    return digits

def radix_sort(numbers):
    buckets = []
    for i in range(10):
        buckets.append([])

    max_digits = radix_get_max_length(numbers)

    pow_10 = 1
    for digit_index in range(max_digits):
        # Split numbers into buckets
        for number in numbers:
            bucket_index = (abs(number) // pow_10) % 10
            buckets[bucket_index].append(number)

        # All numbers are in buckets, clear the list and add the buckets back to the list
        # Clearing the buckets as empty them
        numbers.clear()
        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()

        # Go to the next power of 10 for the next loop
        pow_10 = pow_10 * 10

    negatives = []
    non_negatives = []
    for number in numbers:
        if number < 0:
            negatives.append(number)
        else:
            non_negatives.append(number)
    negatives.reverse()
    numbers.clear()
    numbers.extend(negatives + non_negatives)

# Create a list of unsorted values
numbers = [47, 81, 13, 5, 38, 96, 51, 64]

# Print unsorted list
print('UNSORTED:', numbers)

# Call radix_sort to sort the list
radix_sort(numbers)

# Print sorted list
print('SORTED:', numbers)