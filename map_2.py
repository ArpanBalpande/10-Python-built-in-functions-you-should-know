# list of numbers
numbers = [1, 2, 3, 4, 5]

# add 1 funtion - regular function
def add_one(element):
    return element + 1 

# add 1 to each element of the list
print(list(map(add_one, numbers)))
# [2, 3, 4, 5, 6]