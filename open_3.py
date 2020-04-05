# open a file in reading mode
f = open('reading_lines.txt', 'r')
first_line = f.readline()
print(first_line)
# First line
second_line = f.readline()
print(second_line)
# Second line
third_line = f.readline()
print(third_line)
# Third line

# close the file to avoid running out of file handles
f.close()