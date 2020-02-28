FILE_ADDRESS = "C:/Users/cp253/OneDrive/Documents/School/Data Structures/Programming Assignments/Project 3/3358_2_Pitts_Christopher_PG3.cpp"
MAX_LINE_LENGTH = 80

currentLine = 1

for line in open(FILE_ADDRESS, 'r').readlines():
    while line[0] == ' ':
        line = line[1:]
    if len(line) > MAX_LINE_LENGTH:
        print("Line %i exceeds max characters" % currentLine)
        print("Characters %i" % len(line))
        print("Line Text: %s" % line)
        print('\n')
    currentLine = currentLine + 1
