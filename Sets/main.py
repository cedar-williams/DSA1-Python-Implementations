from Set import Set

my_set1 = Set()
my_set2 = Set()

# Only in set 1 - 10 11 12
my_set1.add(10)
my_set1.add(11)
my_set1.add(12)

# Both Sets - 13 14 15
my_set1.add(13)
my_set2.add(13)
my_set1.add(14)
my_set2.add(14)
my_set1.add(15)
my_set2.add(15)

# Only in set 2 - 16 17 18
my_set2.add(16)
my_set2.add(17)
my_set2.add(18)

print(my_set1)
print(my_set2)

print('Difference:', my_set1.difference(my_set2))
print('Filter (x < 12):', my_set1.filter(lambda x: x < 12))
print('Map (x * 3):', my_set1.map(lambda x: x * 3))
print('Intersection:', my_set1.intersection(my_set2))
print('Union:', my_set1.union(my_set2))

my_set1.remove(10)
print(my_set1)