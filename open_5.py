# create a new file in writing mode
f = open('new_file.txt', 'w')
f.write('This is a new file!')

# close the file to avoid running out of file handles
f.close()