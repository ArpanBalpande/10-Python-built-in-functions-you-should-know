# the with statement automatically closes the file after the nested block of code is executed.
with open('reading_lines.txt', 'r') as f:
    content = f.readlines()
    print(content)
    # ['First line\n', 'Second line\n', 'Third line\n']