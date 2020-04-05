import copy

# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = copy.deepcopy(numbers)

# both list have different id numbers
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 1836112528648, new_numbers id: 1836112763528

# we can also check that both variables point to different objects with the identity operator is
print(numbers is new_numbers)
# False