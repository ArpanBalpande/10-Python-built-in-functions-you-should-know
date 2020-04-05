# open a file in reading mode
f = open('reading_lines.txt', 'r')
content = f.readlines()
print(content)
# ['First line\n', 'Second line\n', 'Third line\n']

# close the file to avoid running out of file handles
f.close()