# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = numbers

# both list have the same id number
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 1836112528136, new_numbers id: 1836112528136

# we can also check that they refer to the same object with the identity operator is
print(numbers is new_numbers)
# True