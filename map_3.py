# lists of numbers
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

# multiply the elements of both lists
print(list(map(lambda x, y: x * y, numbers_1, numbers_2)))
# [6, 14, 24, 36, 50]