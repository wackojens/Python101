def readLinesDay1():
    temp = []

    file1 = open("inputDay1.txt", "r")
    lines = file1.readlines()

    for line in lines:
        temp.append(line.strip())
    return temp



def readLinesDay2():
    temp = []

    file1 = open("inputDay2.txt", "r")
    lines = file1.readlines()

    for line in lines:
        temp.append(line.strip())
    return temp



def readLinesDay3():
    temp = []

    file1 = open("inputDay3.txt", "r")
    lines = file1.readlines()

    for line in lines:
        temp.append(line.strip())
    return temp



def readLinesDay4Board():
    from itertools import filterfalse
    temp = []

    file1 = open("inputDay4BoardNumbers.txt", "r")
    lines = file1.readlines()
    lines = str(lines)
    lines = lines.replace('\n', '')
    lines = lines.replace('n', '')
    lines = lines.replace('\\', '')
    lines = lines.replace("'", '')
    lines = lines.replace(',', '')
    lines = lines.replace('[', '')
    lines = lines.replace(']', '')
    lines = list(lines)
    for i in range(len(lines)-1):
        if lines[i-1] == ' ' and lines[i+1] == ' ':
            lines[i] = lines[i]
        if lines[i] != ' ' and lines[i+1] != ' ':
            lines[i] = lines[i] + lines[i+1]
        if lines[i-1] != ' ' and lines[i+1] == ' ':
            lines[i] = ' '
        if i == len(lines)-2 and lines[i] != ' ' and lines[i+1] != ' ':
            lines[i+1] = ' '
 
    lines = [*filterfalse(lambda i: i == ' ', lines)]
        

    for line in lines:
        temp.append(line)
    return temp