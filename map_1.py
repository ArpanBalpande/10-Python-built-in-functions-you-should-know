# list of numbers
numbers = [1, 2, 3, 4, 5]

# add 1
print(list(map(lambda x: x + 1, numbers)))
# [2, 3, 4, 5, 6]

# multiply by 2
print(list(map(lambda x: x * 2, numbers)))
# [2, 4, 6, 8, 10]

# obtain the cube
print(list(map(lambda x: x ** 3, numbers)))
# [1, 8, 27, 64, 125]