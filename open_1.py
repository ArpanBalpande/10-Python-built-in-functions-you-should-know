# open a file in reading mode 
f = open('reading_file.txt', 'r')
content = f.read()
print(content)
# Successful file reading!

# close the file to avoid running out of file handles
f.close()