# check if an object is of type list

numbers = [1, 2, 3, 4, 5]

print(isinstance(numbers, list))
# True

print(isinstance(numbers, float))
# False

print(isinstance(numbers, (list, float)))
# True