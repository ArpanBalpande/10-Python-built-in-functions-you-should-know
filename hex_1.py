# convert the integer 10 into a hexadecimal number
hex_number = hex(10)

print(hex_number)
# 0xa
print(type(hex_number))
# <class 'str'>

# An exception is raised if a float is provided as input
hex_number = hex(10.0)
# TypeError