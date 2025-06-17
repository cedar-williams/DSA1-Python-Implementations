from Tree234 import Tree234
from Node234 import Node234

user_values = input('Enter insert values with spaces between: ')
print()

# Create a 2-3-4 tree and add the values
tree = Tree234()
for value in user_values.split():
    tree.insert(int(value))

# Display the height after all inserts are complete.
print("2-3-4 tree with " + str(len(tree)) + " keys has height " + str(tree.get_height()))

# Read user input to get a list of values to remove
user_values = input('Enter remove values with spaces between: ')
print()

for value in user_values.split():
    to_remove = int(value)
    print('Remove node ' + value + ': ', end='')
    if tree.remove(to_remove):
        print('2-3-4 tree with ' + str(len(tree)) + ' keys has height ' + str(tree.get_height()))
    else:
        print('*** Key not found. Tree is not changed. ***')
