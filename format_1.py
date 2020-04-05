# fixed-point notation rounded off to two decimal places 
print(format(123.45789,'.2f'))
# '123.46'

# percentage rounded off to one decimal place
print(format(0.1569,'.1%'))
# '15.7%'

# hexadecimal number 
print(format(10,'x'))
# 'a'

# exponential notation rounded off two decimal places with sign for both positive and negative numbers
print(format(123.45789,'+.2e'))
# '+1.23e+02'

# number with fill character, width, and right-alignment
print(format(123.45789,'*>30'))
# '*********************123.45789'