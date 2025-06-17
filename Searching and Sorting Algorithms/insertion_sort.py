def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        while (j > 0) and (numbers[j] < numbers[j - 1]):
            tmp_value = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = tmp_value
            j -= 1


numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()

insertion_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()